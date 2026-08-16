from agents.manager_agent import ManagerAgent


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


print("\n================================")
print("     AI SOFTWARE TEAM")
print("================================")


manager = ManagerAgent()

result = manager.run(requirement)


if result["success"]:

    print("\n🎉 Manager Agent says:")
    print("PROJECT IS READY FOR GITHUB.")

else:

    print("\n⚠️ Manager Agent says:")
    print("PROJECT NEEDS MORE WORK.")