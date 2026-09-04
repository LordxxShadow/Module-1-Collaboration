# Marvelours Ojeyemi
# M02_Case_Study.py
# This program accepts student names and GPAs and determines whether
# each student qualifies for the Dean's List or Honor Roll.
while True:
    last_name = input("Enter the student's last name (ZZZ to quit): ")

    if last_name == "ZZZ":
        break

    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")

    if gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")
        # GitHub Repository: https://github.com/LordxxShadow/Module-1-Collaboration
        