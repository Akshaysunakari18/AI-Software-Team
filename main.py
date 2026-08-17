from agents.manager_agent import ManagerAgent
from agents.github_agent import GitHubAgent


# ==========================================
# GET REQUIREMENT FROM USER
# ==========================================

print("\n================================")
print("       AI SOFTWARE TEAM")
print("================================")

print("\nEnter your software requirement.")
print("Example:")
print("Build a Python student marks management system.")

requirement = input("\nRequirement: ").strip()


# ==========================================
# VALIDATE REQUIREMENT
# ==========================================

if not requirement:

    print("\n❌ Requirement cannot be empty.")
    raise SystemExit


# ==========================================
# MANAGER AGENT
# ==========================================

manager = ManagerAgent()

result = manager.run(requirement)


# ==========================================
# PROJECT APPROVED
# ==========================================

if result["success"]:

    print("\nSending approved project to GitHub Agent...")

    github_agent = GitHubAgent()

    github_success = github_agent.push_changes()

    if github_success:

        print("\n================================")
        print("       🚀 PROJECT COMPLETE")
        print("================================")

        print("\nProject successfully pushed to:")
        print("GitHub → developer branch")

    else:

        print("\n❌ GitHub push failed.")


# ==========================================
# PROJECT REJECTED
# ==========================================

else:

    print("\n================================")
    print("       ❌ PROJECT REJECTED")
    print("================================")

    print("\nThe project was NOT pushed to GitHub.")

    print(
        "The Coding Agent must fix the project "
        "until the tests pass."
    )


# ==========================================
# FINISHED
# ==========================================

print("\n================================")
print("          TEAM FINISHED")
print("================================")