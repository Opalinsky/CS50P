import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #using search
    matches = re.search(r"^<iframe src=\"(https?://)?(www\.)?youtube\.com/embed/(.+)$", s)
    #yt = re.sub(r"^(https://)?(www\.)?youtube\.com/embed/", "", s)
    #re.sub replace some value with some expression
    if matches:
        return ("https://youtu.be/" + matches.group(3).split('"')[0])
    else:
        return "None"

if __name__ == "__main__":
    main()
