import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    before = sys.argv[1]
    after = sys.argv[2]
    getting_list(before,after)

def getting_list(before, after):
    try:
        with open(before, "r") as before, open(after, "w") as after:
            reader = csv.DictReader(before)
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(after, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow(
                    {
                        "last": last,
                        "first": first,
                        "house": row["house"]

                    }
                )

    except FileNotFoundError:
        sys.exit(f"Could not read {before}")

if __name__ == "__main__":
    main()
