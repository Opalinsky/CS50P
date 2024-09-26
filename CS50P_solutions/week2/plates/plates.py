import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if (s[0:2].isnumeric()) == True:
             return False
        else:
            if s.isalpha() == False and (s[-2:].isnumeric()) == True:
                if s[-2] != "0":
                    for i in range(len(s)):
                        if s[i] in string.punctuation:
                            return False
                        else:
                            continue
                    return True
                else:
                    return False
            else:
                if s.isalpha() == True:
                    for i in range(len(s)):
                        if s[i] in string.punctuation:
                            return False
                        else:
                            continue
                    return True
                else:
                    return False
    else:
        return False

main()
