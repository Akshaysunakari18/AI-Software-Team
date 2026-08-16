from pathlib import Path

from langchain_ollama import ChatOllama


class CodingAgent:

    def __init__(self):
        self.llm = ChatOllama(
            model="qwen2.5-coder:3b",
            temperature=0
        )

    def clean_code(self, code):

        code = code.strip()

        if code.startswith("```python"):
            code = code[len("```python"):].strip()

        if code.startswith("```"):
            code = code[3:].strip()

        if code.endswith("```"):
            code = code[:-3].strip()

        return code

    def generate_code(self, requirement):

        prompt = f"""
You are a professional Python software developer.

ORIGINAL REQUIREMENT:
{requirement}

Write a complete Python implementation that satisfies the requirement.

IMPORTANT:
1. Implement EVERY function mentioned in the requirement.
2. Handle all specified edge cases.
3. The divide function MUST raise ValueError when the second argument is zero.
4. Return ONLY valid Python code.
5. Do not use markdown.
6. Do not use ```python.
7. Do not provide explanations.
"""

        response = self.llm.invoke(prompt)

        return self.clean_code(response.content)

    def save_code(self, code, filename):

        workspace = Path("workspace")
        workspace.mkdir(exist_ok=True)

        file_path = workspace / filename

        file_path.write_text(
            code,
            encoding="utf-8"
        )

        return file_path

    def fix_code(self, code, test_output, requirement):

        prompt = f"""
You are a senior Python developer responsible for fixing failed code.

ORIGINAL REQUIREMENT:
{requirement}

CURRENT CODE:
{code}

TEST FAILURE:
{test_output}

YOUR TASK:
Fix the CURRENT CODE so that ALL tests pass.

IMPORTANT:
1. Carefully inspect the current code.
2. Identify the exact reason for the test failure.
3. Preserve functionality that is already working.
4. Implement the missing or incorrect behavior.
5. The divide function MUST raise ValueError when the second argument is zero.
6. Return the COMPLETE corrected Python source code.
7. Return ONLY Python code.
8. Do NOT use markdown.
9. Do NOT use ```python.
10. Do NOT provide explanations.
11. Make sure all required functions are present.

Return only the corrected Python source code.
"""

        response = self.llm.invoke(prompt)

        return self.clean_code(response.content)