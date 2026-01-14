import json

with open("task2.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    grades = student["grades"]
    student["avg_grade"] = round(sum(grades) / len(grades))

with open("task2_ans.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4)
print(students)
