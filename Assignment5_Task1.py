students = {"Alice": 85, "Rohan": 78, "Rahul": 92, "Vishal": 88}

name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")
