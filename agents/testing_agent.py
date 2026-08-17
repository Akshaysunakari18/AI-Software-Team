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

    # ==========================================
    # GENERATE TESTS
    # ==========================================

    def generate_tests(self, project):

        project_text = ""

        for filename, code in project.items():

            project_text += f"""
==============================
FILE: {filename}
==============================

{code}

"""

        # ==========================================
        # FIND PYTHON PROJECT FILES
        # ==========================================

        python_files = [
            Path(filename).stem
            for filename in project.keys()
            if filename.endswith(".py")
        ]

        # ==========================================
        # CREATE IMPORTS
        # ==========================================

        imports = ""

        for module in python_files:

            imports += (
                f"from workspace.{module} import *\n"
            )

        # ==========================================
        # TESTING AGENT PROMPT
        # ==========================================

        prompt = f"""
You are a professional Python testing engineer.

Your job is to create reliable pytest tests for the
Python project provided below.

PROJECT:

{project_text}

=========================================
TESTING RULES
=========================================

1. Test every important function and class.

2. Test normal/valid inputs.

3. Test important edge cases.

4. Test empty collections where appropriate.

5. Test boundary cases where appropriate.

6. The application files are located inside
   the workspace package.

7. You MUST import the application code.

Use these imports:

{imports}

8. If you use pytest.raises(), you MUST include:

import pytest

9. NEVER assume a specific exception type unless
   the ORIGINAL USER REQUIREMENT explicitly
   specifies that exception type.

10. Do NOT automatically assume invalid input
    must raise ValueError.

11. Do NOT automatically assume invalid input
    must raise TypeError.

12. Do NOT invent validation requirements that
    are not present in the user's requirement.

13. If the requirement does not specify what
    should happen for an invalid input, do not
    create a test requiring a specific exception.

14. Tests must reflect the ORIGINAL USER REQUIREMENT.

15. Calculate ALL expected numeric values yourself.

16. NEVER guess expected numeric values.

17. For an average, calculate:

    sum(values) / number_of_values

18. Example:

    Values = 85, 92, 78

    Sum = 85 + 92 + 78
        = 255

    Average = 255 / 3
            = 85.0

    Therefore:

    assert average == 85.0

    NOT:

    assert average == 85.33333333333333

19. Verify arithmetic before creating assertions.

20. Do NOT modify correct application behavior
    simply to satisfy an incorrect expected value.

21. Do not create tests for functionality that
    was not requested by the user.

22. Keep the test suite focused on the actual
    software requirement.

23. Tests must be independent from each other.

24. Tests must be runnable using:

    python -m pytest -v

25. Return ONLY valid Python pytest code.

26. Do NOT use markdown.

27. Do NOT use ```python.

28. Do NOT provide explanations.

29. Do NOT provide comments outside the Python code.

30. Return the COMPLETE test file.

=========================================

Return ONLY the pytest code.
"""

        # ==========================================
        # CALL OLLAMA
        # ==========================================

        response = self.llm.invoke(prompt)

        tests = response.content.strip()

        # ==========================================
        # REMOVE MARKDOWN CODE FENCES
        # ==========================================

        if tests.startswith("```python"):

            tests = tests[
                len("```python"):
            ].strip()

        if tests.startswith("```"):

            tests = tests[3:].strip()

        if tests.endswith("```"):

            tests = tests[:-3].strip()

        # ==========================================
        # SAFETY CHECK 1
        # ENSURE PYTEST IMPORT
        # ==========================================

        if (
            "pytest." in tests
            or "pytest.raises" in tests
        ):

            if "import pytest" not in tests:

                tests = (
                    "import pytest\n\n"
                    + tests
                )

        # ==========================================
        # SAFETY CHECK 2
        # ENSURE APPLICATION IMPORT
        # ==========================================

        if python_files:

            required_import = (
                f"from workspace.{python_files[0]} "
                f"import *"
            )

            if "from workspace." not in tests:

                tests = (
                    required_import
                    + "\n\n"
                    + tests
                )

        return tests

    # ==========================================
    # SAVE TESTS
    # ==========================================

    def save_tests(self, tests):

        tests_folder = Path("tests")

        tests_folder.mkdir(
            exist_ok=True
        )

        test_file = (
            tests_folder
            / "test_project.py"
        )

        test_file.write_text(
            tests,
            encoding="utf-8"
        )

        return test_file

    # ==========================================
    # RUN TESTS
    # ==========================================

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
            "output": (
                result.stdout
                + result.stderr
            )
        }