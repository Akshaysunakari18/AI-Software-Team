from agents.coding_agent import CodingAgent
from agents.testing_agent import TestingAgent


class ManagerAgent:

    def __init__(self):

        self.coding_agent = CodingAgent()
        self.testing_agent = TestingAgent()

    def run(self, requirement):

        print("\n================================")
        print("        MANAGER AGENT")
        print("================================")

        # --------------------------------
        # STEP 1: CODING AGENT
        # --------------------------------

        print("\n[1] Sending requirement to Coding Agent...")

        code = self.coding_agent.generate_code(
            requirement
        )

        self.coding_agent.save_code(
            code,
            "calculator.py"
        )

        print("[✓] Coding Agent completed the code.")

        # --------------------------------
        # STEP 2: TESTING LOOP
        # --------------------------------

        max_attempts = 5

        for attempt in range(1, max_attempts + 1):

            print(
                f"\n[2] Testing Agent - Attempt {attempt}"
            )

            # Generate tests
            tests = self.testing_agent.generate_tests(
                code,
                "calculator.py"
            )

            # Save tests
            test_file = self.testing_agent.save_tests(
                tests,
                "calculator.py"
            )

            print(
                f"[✓] Tests saved: {test_file}"
            )

            # Run pytest
            result = self.testing_agent.run_tests()

            print("\n===== TEST RESULTS =====")
            print(result["output"])

            # --------------------------------
            # TESTS PASSED
            # --------------------------------

            if result["success"]:

                print("\n================================")
                print("       ✅ PROJECT APPROVED")
                print("================================")

                return {
                    "success": True,
                    "code": code,
                    "test_output": result["output"]
                }

            # --------------------------------
            # TESTS FAILED
            # --------------------------------

            print("\n❌ Tests failed.")

            if attempt < max_attempts:

                print(
                    "\n[Manager] Sending failure "
                    "back to Coding Agent..."
                )

                # Ask Coding Agent to fix code
                code = self.coding_agent.fix_code(
                    code,
                    result["output"],
                    requirement
                )

                # Save corrected code
                self.coding_agent.save_code(
                    code,
                    "calculator.py"
                )

                print(
                    "[✓] Coding Agent fixed the code."
                )

            else:

                print(
                    "\n[Manager] Maximum attempts reached."
                )

        # --------------------------------
        # PROJECT REJECTED
        # --------------------------------

        print("\n================================")
        print("       ❌ PROJECT REJECTED")
        print("================================")

        return {
            "success": False,
            "code": code,
            "test_output": result["output"]
        }