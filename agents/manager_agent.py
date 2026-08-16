from agents.coding_agent import CodingAgent
from agents.testing_agent import TestingAgent


class ManagerAgent:

    def __init__(self):

        self.coding_agent = CodingAgent()
        self.testing_agent = TestingAgent()

        self.max_attempts = 3

    def run(self, requirement):

        print("\n================================")
        print("        MANAGER AGENT")
        print("================================")

        # ==========================================
        # CODING AGENT
        # ==========================================

        print("\n[1] Sending requirement to Coding Agent...")

        try:

            project = self.coding_agent.generate_project(
                requirement
            )

            saved_files = self.coding_agent.save_project(
                project
            )

            print("[✓] Coding Agent completed the project.")

            print("\nGenerated files:")

            for file in saved_files:
                print("   ", file)

        except Exception as e:

            print("\n❌ Coding Agent failed:")
            print(e)

            return {
                "success": False,
                "project": None
            }

        # ==========================================
        # TESTING + FIX LOOP
        # ==========================================

        for attempt in range(1, self.max_attempts + 1):

            print("\n================================")
            print(
                f"      TESTING AGENT - ATTEMPT {attempt}"
            )
            print("================================")

            try:

                tests = self.testing_agent.generate_tests(
                    project["files"]
                )

                test_file = self.testing_agent.save_tests(
                    tests
                )

                print(
                    f"[✓] Tests saved: {test_file}"
                )

            except Exception as e:

                print("\n❌ Testing Agent failed:")
                print(e)

                return {
                    "success": False,
                    "project": project
                }

            # ==========================================
            # RUN TESTS
            # ==========================================

            result = self.testing_agent.run_tests()

            print("\n===== TEST RESULTS =====")

            print(result["output"])

            # ==========================================
            # TESTS PASSED
            # ==========================================

            if result["success"]:

                print("\n================================")
                print("       ✅ PROJECT APPROVED")
                print("================================")

                return {
                    "success": True,
                    "project": project
                }

            # ==========================================
            # TESTS FAILED
            # ==========================================

            print("\n❌ Tests failed.")

            if attempt >= self.max_attempts:

                print("\nMaximum attempts reached.")

                print(
                    "\n❌ PROJECT REJECTED"
                )

                return {
                    "success": False,
                    "project": project
                }

            # ==========================================
            # SEND FAILURE BACK TO CODING AGENT
            # ==========================================

            print(
                "\n[Manager] Sending failure "
                "feedback to Coding Agent..."
            )

            failure_prompt = f"""
Fix the Python project based on the failed tests.

ORIGINAL REQUIREMENT:
{requirement}

CURRENT PROJECT:
{project["files"]}

TEST FAILURE:
{result["output"]}

Create the corrected complete project.

Return ONLY valid JSON in this format:

{{
    "files": {{
        "filename.py": "complete corrected Python code"
    }}
}}

Rules:

1. Keep all necessary project files.
2. Fix the actual cause of the test failure.
3. Follow the original requirement.
4. Do not return tests.
5. Return ONLY JSON.
"""

            try:

                project = self.coding_agent.generate_project(
                    failure_prompt
                )

                saved_files = self.coding_agent.save_project(
                    project
                )

                print(
                    "[✓] Coding Agent submitted "
                    "a corrected project."
                )

                print("\nUpdated files:")

                for file in saved_files:
                    print("   ", file)

            except Exception as e:

                print("\n❌ Coding Agent failed to fix project:")
                print(e)

                return {
                    "success": False,
                    "project": project
                }

        return {
            "success": False,
            "project": project
        }