def main():
    length = int(input("Give the length of the pyramide: "))
    pyramide(length)

def pyramide(size):
    for i in range(size):
        print("#"*(i+1))

main()
