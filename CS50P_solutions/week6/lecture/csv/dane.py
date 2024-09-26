import csv
import random
with open("przykladowe_dane.csv", "r") as file, open("analysis.csv", "w") as analysis: #second argument - reading mode, giving temp name "file"
    reader = csv.DictReader(file)
    #writer = csv.DictWriter(analysis, fieldnames=["Name","Surname","Position","Wage"])
    writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["Pensja"])
    writer.writeheader()
    for row in reader:
        minimal_wage = 4650
        pensja =random.randint(minimal_wage, 10000)
        writer.writerow(#signing the names of the row based on reader
            {
                "Imię": row["Imię"],
                "Nazwisko": row["Nazwisko"],
                "Wiek": row["Wiek"],
                "Miasto": row["Miasto"],
                "Stanowisko": row["Stanowisko"],
                "Pensja": pensja,
            }
        )
