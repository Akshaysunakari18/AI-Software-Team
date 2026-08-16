from pathlib import Path
import subprocess
import sys

from langchain_ollama import ChatOllama


class TestingAgent:

    def __init__(self):
        self.llm = ChatOllama(
            model="qwen2.5-coder:3b",
            temperature=0
        )

    def generate_tests(self, project):

        project_text = ""

        for filename, code in project.items():

            project_text += f"""
==============================
FILE: {filename}
==============================

{code}

"""

        # Find Python source files
        python_files = [
            Path(filename).stem
            for filename in project.keys()
            if filename.endswith(".py")
        ]

        imports = ""

        for module in python_files:
            imports += f"from workspace.{module} import *\n"

        prompt = f"""
You are a professional Python testing engineer.

Here is the Python project:

{project_text}

Create pytest tests for this project.

IMPORTANT RULES:

1. Test every important function.
2. Test normal cases.
3. Test important edge cases.
4. The application files are located inside the workspace package.
5. You MUST import the application functions.
6. Use these imports at the beginning of the test file:

{imports}

7. If testing division by zero and the requirement says ValueError,
   use pytest.raises(ValueError).
8. Return ONLY valid Python pytest code.
9. Do not use markdown.
10. Do not use ```python.
11. Do not provide explanations.
12. The tests must be runnable directly with pytest.

Return ONLY the complete pytest code.
"""

        response = self.llm.invoke(prompt)

        tests = response.content.strip()

        # Remove markdown code fences
        if tests.startswith("```python"):
            tests = tests[len("```python"):].strip()

        if tests.startswith("```"):
            tests = tests[3:].strip()

        if tests.endswith("```"):
            tests = tests[:-3].strip()

        # Safety check:
        # Make sure the generated tests actually import the project.
        if python_files:

            required_import = f"from workspace.{python_files[0]} import *"

            if "from workspace." not in tests:

                tests = (
                    required_import
                    + "\n\n"
                    + tests
                )

        return tests

    def save_tests(self, tests):

        tests_folder = Path("tests")
        tests_folder.mkdir(exist_ok=True)

        test_file = tests_folder / "test_project.py"

        test_file.write_text(
            tests,
            encoding="utf-8"
        )

        return test_file

    def run_tests(self):

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "-v"
            ],
            capture_output=True,
            text=True
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout + result.stderr
        }