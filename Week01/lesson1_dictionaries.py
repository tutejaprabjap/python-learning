student = {
    "name": "Prabjap Tuteja",
    "major": "Management Information Systems",
    "graduation_year": 2028,
    "gpa": 3.8,
    "skills": ["Python", "SQL", "Data Analysis"]
}

print(f"My name is {student["name"]} and my GPA is {student["gpa"]}")

student["certificate"] = "FinTech"
student["gpa"] = 4.0

for key,value in student.items():
    print(key,":",value)