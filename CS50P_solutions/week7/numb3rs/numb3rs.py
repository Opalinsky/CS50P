import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.search(pattern, ip)
    if match:
        for i in range(1, 4):
            if int(match.group(i)) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
