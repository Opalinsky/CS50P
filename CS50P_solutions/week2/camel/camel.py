# camelCase = input("camelCase: ")
# size = len(camelCase)
# snake_case = [None] * size
# for a in range(len(camelCase)):
#     counter = 0
#     a = a + counter
#     print(a)

#     if a == 0 and camelCase[a].isupper():
#         snake_case[a] = camelCase[a].lower()
#         continue
#     if camelCase[a].isupper() == True:
#         snake_case[a+1] = camelCase[a]
#         snake_case[a] = '_'
#         counter = counter + 1
#         print("licznik to",counter)
#         print(a)
#         print(snake_case[a])
#         print(snake_case[a+1])
#         continue
#     print("a to", a)
#     print("counter to", counter)
#     snake_case[a]=camelCase[a]
#     print(a, snake_case[a])

# print(snake_case)
# mySeparator = ''
# x = mySeparator.join(snake_case)
# print(x)
camelCase = input("camelCase: ")
snake_case = []
for a in range(len(camelCase)):
    letter = camelCase[a]
    if a == 0:
        letter = letter.lower()

    if camelCase[a].isupper() == True:
        snake_case.append("_")
        letter = letter.lower()

    snake_case.append(letter)

mySeparator = ''
x = mySeparator.join(snake_case)
print(x)
