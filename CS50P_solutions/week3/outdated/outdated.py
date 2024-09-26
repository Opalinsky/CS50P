def main():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True:
        try:
            date = input("Date: ").strip()

            if date[0].isalpha():
                # Przetwarzanie formatu "Month Day, Year"
                month_day_year = date.split(" ")
                if len(month_day_year) != 3 or month_day_year[1][-1] != ',':
                    raise ValueError

                month = month_day_year[0]
                day = month_day_year[1][:-1]  # Usunięcie przecinka
                year = month_day_year[2]

                if month not in months:
                    raise ValueError

                month_num = str(months[month]).zfill(2)
                day = day.zfill(2)
                

                if int(month) > 12 or int(day) > 31:
                    raise ValueError

                print(f"{year}-{month_num}-{day}")
                break

            else:
                # Przetwarzanie formatu "MM/DD/YYYY"
                if "/" not in date:
                    raise ValueError

                month, day, year = date.split("/")

                if len(month) > 2 or len(day) > 2 or len(year) != 4:
                    raise ValueError

                month = month.zfill(2)
                day = day.zfill(2)

                if int(month) > 12 or int(day) > 31:
                    raise ValueError

                print(f"{year}-{month}-{day}")
                break

        except ValueError:
            pass

main()
