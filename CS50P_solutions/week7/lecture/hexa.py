import re

def main():
    code = input("Hexadecimal colour code: ")

    pattern = r"^#[0-9A-Fa-f]{6}"#raw string not to interpretate in a wrong way
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")
main()
