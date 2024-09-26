import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d{1,2}):?(\d{2})?\s(AM|PM)\sto\s(\d{1,2}):?(\d{2})?\s(AM|PM)$",s):
        try:
            hour_1 = int(matches.group(1))
            minute_1 = matches.group(2) if matches.group(2) else "00"
            hour_2 = int(matches.group(4))
            minute_2 = matches.group(5) if matches.group(5) else "00"

            if minute_1 and int(minute_1) > 59:
                raise ValueError("Minutes must be between 00 and 59")
            if minute_2 and int(minute_2) > 59:
                raise ValueError("Minutes must be between 00 and 59")

            if matches.group(3) == "AM" and matches.group(1) == "12":
                hour_1 = 0
            if matches.group(6) == "AM" and matches.group(4) == "12":
                hour_1 = 0
            if matches.group(3) == "PM" and matches.group(1) != "12":
                hour_1 += 12
            if matches.group(6) == "PM" and matches.group(4) != "12":
                hour_2 += 12
            return f"{hour_1:02}:{minute_1} to {hour_2:02}:{minute_2}"
        except ValueError:
            raise ValueError("Invalid time format")
    else:
        raise ValueError("Invalid input format")

if __name__ == "__main__":
    main()
