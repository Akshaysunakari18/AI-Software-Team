from pathlib import Path
import json
import re

from langchain_ollama import ChatOllama


class CodingAgent:

    def __init__(self):
        self.llm = ChatOllama(
            model="qwen2.5-coder:3b",
            temperature=0
        )

    def clean_response(self, response):

        text = response.strip()

        if text.startswith("```json"):
            text = text[len("```json"):].strip()

        if text.startswith("```"):
            text = text[3:].strip()

        if text.endswith("```"):
            text = text[:-3].strip()

        return text

    def generate_project(self, requirement):

        prompt = f"""
You are a senior Python software engineer.

USER REQUIREMENT:
{requirement}

Design and implement a complete small Python project.

Return ONLY valid JSON.

The JSON must have exactly this structure:

{{
    "files": {{
        "filename.py": "complete Python source code",
        "another_file.py": "complete Python source code"
    }}
}}

RULES:

1. Create all files necessary for the project.
2. Keep the project simple and runnable.
3. Use Python.
4. Put application source files inside the "workspace" folder.
5. Do NOT put tests in the response.
6. The Testing Agent will create the tests separately.
7. Every Python file must contain valid Python code.
8. Do not use markdown.
9. Do not use ```json.
10. Do not include explanations.
11. Return ONLY the JSON object.

Example:

{{
    "files": {{
        "calculator.py": "def add(a, b):\\n    return a + b\\n"
    }}
}}
"""

        response = self.llm.invoke(prompt)

        text = self.clean_response(response.content)

        try:
            project = json.loads(text)

        except json.JSONDecodeError:

            # Try to extract JSON if the model added extra text
            match = re.search(
                r'\{.*\}',
                text,
                re.DOTALL
            )

            if not match:
                raise ValueError(
                    "Coding Agent did not return valid JSON."
                )

            project = json.loads(match.group(0))

        if "files" not in project:
            raise ValueError(
                "Coding Agent response does not contain 'files'."
            )

        return project

    def save_project(self, project):

        workspace = Path("workspace")
        workspace.mkdir(exist_ok=True)

        saved_files = []

        for filename, content in project["files"].items():

            # Prevent the AI from creating files outside workspace
            safe_name = Path(filename).name

            file_path = workspace / safe_name

            file_path.write_text(
                content,
                encoding="utf-8"
            )

            saved_files.append(file_path)

        return saved_files