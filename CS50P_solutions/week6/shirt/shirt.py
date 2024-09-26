import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        before = sys.argv[1].lower()
        after = sys.argv[2].lower()
        before_ext = before.split(".")[-1]
        after_ext = after.split(".")[-1]
        if before_ext != "jpg" and before_ext != "png" and before_ext != "jpeg":
            sys.exit("Invalid input")

        if before_ext != after_ext:
            sys.exit("Input and output have different extensions")
        image(before,after)

def image(before,after):
    try:

        img = Image.open(before)
        shirt_img = Image.open("shirt.png")
        size = shirt_img.size
        img = ImageOps.fit(img, size)
        img.paste(shirt_img, shirt_img)
        img.save(after)



    except FileNotFoundError:
        sys.exit(f"Could not read {before}")

if __name__ == "__main__":
    main()
