"""2. String comparison
a) Define the project_name variable and store the value 'DevOps-Project-A' in it.
b) Read another project name from the user as input and store it in a variable
`new_project_name`.
c) Compare if both values are the same and print "Project already exists", if they are
same. Else print "New project added to inventory."
d) Note: "PROJECT-A" and "project-a" are the same as far as your application is
concerned. So keep this in mind while doing the comparison.
"""
project_name = "DEVOPS-Project-A"
project = ["DEVOPS-Project-A"]
new_project_name = input("Please suggest a new project? ")
if project_name.casefold() == new_project_name.casefold():
    print("This project already exists")
else:
    print("New project added to inventory.")
    project.append(new_project_name)
print(project)