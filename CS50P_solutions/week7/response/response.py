from validator_collection import checkers

def main():
    print(response(input("What's your email address? ")))


def response(s):
    if email_address := checkers.is_email(s):
        return f"Valid"
    else:
        return f"Invalid"

if __name__ == "__main__":
    main()
