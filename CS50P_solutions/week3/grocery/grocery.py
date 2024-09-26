def main():
    dict = {}
    i = 1
    while True:
        try:
            product = input()
            product = product.upper()
            if product in dict.keys():
                i+=i
            dict[product] = i

        except EOFError:
                print()
                break

    for key in sorted(dict.keys()):
        print(dict[key],key)

main()
