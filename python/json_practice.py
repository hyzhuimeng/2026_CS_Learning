"""import json
students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
]
with open("students.json","w",encoding="utf-8") as f:
    json.dump(students,f,ensure_ascii=False,indent=2)
"""
import json
with open("students.json","r",encoding="utf-8") as f:
    students =json.load(f)
for i in students:
    print(i["name"])