def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(word):
    text_after = []
    for char in word:
        if char.lower() not in 'aeiou':
            text_after.append(char)
    return ''.join(text_after)

if __name__ == "__main__":
    main()
