# declaretion
student = {
    "name": "ron",
    "age": 34,
    "grades": [100, 85, 35, 90, 89, 24, 100, 89, 99]
}

patient = {
    "name": "dana",
    "age": 35,
    "diagnosis": ["diabetes", "flu"]
}

doctor = {
    "name": "dr mohamad",
    "age": 40,
    "id": 20003332,
    "specialization": "orthopedist",
    "seniority": 15
}

# print
print(student)
for key, value in student.items():
    print(f"key= {key} value= {value}")

print(student["name"])
print(student.get("age"))

for key in student.keys():
    print(f"key:{key}")

for value in student.values():
    print(f"value:{value}")

print(f"before change\n{student}")
student["name"] = "David"
print(f"after change:\n{student}")

grades = student["grades"]
max = 0;
min = 101
sum = 0
for i in grades:
    if i > max:
        max = i
    if i < min:
        min = i
    sum += i

print(f"max grade: {max}")
print(f"min grade: {min}")
print(f"avg of grades: {sum / len(grades)}")
