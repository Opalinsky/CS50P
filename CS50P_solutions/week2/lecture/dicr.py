# #dictionary is combined two values together: key with value

# #using currly braces in dicts
# students = {
#     "Hermione":"Gryfindor",
#     "Harry":"Gryfindor",
#     "Ron": "Gryfindor",
# }

# # print(students["Hermione"])

# #using for loop in dict it itterate over the keys
# for student in students:
#     print(student, students[student], sep=",")
# #cause student name is a key



#list od dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}#keyword None this represent the absence of the value
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", c  ")
