from tools.git_tools import (
    git_status,
    git_add_all,
    git_commit,
    git_push_developer
)


class GitHubAgent:

    def __init__(self):
        self.branch = "developer"

    def push_changes(self):

        print("\n================================")
        print("         GITHUB AGENT")
        print("================================")

        # --------------------------------
        # STEP 1: CHECK STATUS
        # --------------------------------

        print("\n[1] Checking Git status...")

        status = git_status()

        print(status["output"])

        if not status["success"]:

            print("❌ Git status failed.")

            return False

        # --------------------------------
        # STEP 2: ADD FILES
        # --------------------------------

        print("\n[2] Adding project files...")

        result = git_add_all()

        print(result["output"])

        if not result["success"]:

            print("❌ Git add failed.")

            return False

        # --------------------------------
        # STEP 3: COMMIT
        # --------------------------------

        print("\n[3] Creating commit...")

        result = git_commit(
            "AI team: approved code"
        )

        print(result["output"])

        if not result["success"]:

            # Nothing to commit is not necessarily an error
            if "nothing to commit" in result["output"].lower():

                print("No new changes to commit.")

            else:

                print("❌ Git commit failed.")

                return False

        # --------------------------------
        # STEP 4: PUSH
        # --------------------------------

        print("\n[4] Pushing to developer branch...")

        result = git_push_developer()

        print(result["output"])

        if not result["success"]:

            print("❌ Git push failed.")

            return False

        print("\n================================")
        print("      ✅ GITHUB PUSH SUCCESS")
        print("================================")

        print("\nBranch:", self.branch)

        return True