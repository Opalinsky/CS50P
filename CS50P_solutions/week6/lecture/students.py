import csv

name = input("What's your name? ")
home = input("Where is your home? ")

with open("students.csv", "a") as file: #opening in append mode
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name" : name, "home" : home})
