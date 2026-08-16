from agents.manager_agent import ManagerAgent
from agents.github_agent import GitHubAgent


# ==========================================
# PROJECT REQUIREMENT
# ==========================================

requirement = """
Create a Python calculator with four functions:

1. add(a, b)
2. subtract(a, b)
3. multiply(a, b)
4. divide(a, b)

Requirements:

- add(a, b) returns the sum.
- subtract(a, b) returns the difference.
- multiply(a, b) returns the product.
- divide(a, b) returns the division result.
- divide(a, b) MUST raise ValueError when b is zero.
"""


# ==========================================
# START AI SOFTWARE TEAM
# ==========================================

print("\n================================")
print("       AI SOFTWARE TEAM")
print("================================")


# ==========================================
# MANAGER AGENT
# ==========================================

manager = ManagerAgent()

result = manager.run(requirement)


# ==========================================
# IF TESTS PASS → GITHUB
# ==========================================

if result["success"]:

    print("\n🎉 Manager Agent:")
    print("PROJECT IS READY FOR GITHUB.")

    print("\nSending approved project to GitHub Agent...")

    github_agent = GitHubAgent()

    github_success = github_agent.push_changes()

    if github_success:

        print("\n================================")
        print("       🚀 DEPLOYMENT COMPLETE")
        print("================================")

        print("\nProject successfully pushed to:")
        print("GitHub → developer branch")

    else:

        print("\n❌ GitHub push failed.")

else:

    print("\n================================")
    print("       ❌ PROJECT REJECTED")
    print("================================")

    print("\nThe project was NOT pushed to GitHub.")
    print("The tests must pass before GitHub upload.")


print("\n================================")
print("          TEAM FINISHED")
print("================================")