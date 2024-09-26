import inflect
p = inflect.engine()
list = []
while True:
    try:
        name = input("Name: ")
        list.append(name)
    except EOFError:
        lista = (p.join(list))
        print(f"Adieu, adieu, to {lista}")
        break
