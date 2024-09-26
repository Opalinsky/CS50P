def main():
    Ans = input("What time is it? ")
    ConvertedTime = convert(Ans)
    if 7 <= ConvertedTime <= 8:
        print("breakfast time")
    elif 12 <= ConvertedTime <= 13:
        print("lunch time")
    elif 18 <= ConvertedTime <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes) / 60
    return hours + minutes


if __name__ == "__main__":
    main()
