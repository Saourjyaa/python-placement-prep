student = {"name": "Aarav", "course": "Computer Science", "score": 82}
print(student["name"])
student["score"] = 86
student["city"] = "Pune"
del student["city"]
for key, value in student.items():
    print(f"{key}: {value}")
