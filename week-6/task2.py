import json

with open("task2.json.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    grades = student["grades"]
    student["average_grade"] = sum(grades) / len(grades)

with open("task2.json.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4)
