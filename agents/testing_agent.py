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

    def generate_tests(self, code, filename):

        module_name = Path(filename).stem

        prompt = f"""
You are a professional Python testing engineer.

SOURCE FILE:
workspace/{filename}

SOURCE CODE:
{code}

Create complete pytest test cases for this code.

IMPORTANT:
1. Import the functions from the source file using:
   from workspace.{module_name} import function_name
2. Test every function.
3. Test normal cases.
4. Test edge cases.
5. Test division by zero if a divide function exists.
6. If divide by zero is supposed to raise ValueError, use:
   with pytest.raises(ValueError):
7. Return ONLY valid Python pytest code.
8. Do not use markdown.
9. Do not provide explanations.
10. Make sure every function used by the tests is imported.

Return only the complete pytest code.
"""

        response = self.llm.invoke(prompt)

        tests = response.content.strip()

        if tests.startswith("```python"):
            tests = tests[len("```python"):].strip()

        if tests.startswith("```"):
            tests = tests[3:].strip()

        if tests.endswith("```"):
            tests = tests[:-3].strip()

        return tests

    def save_tests(self, tests, filename):

        tests_folder = Path("tests")
        tests_folder.mkdir(exist_ok=True)

        test_file = tests_folder / f"test_{filename}"

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