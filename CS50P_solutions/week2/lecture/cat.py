# #keywords while,
# i = 3
# while i <= 3:
#     print("meow", i)
#     i = i+1 #or i += 1

#for loop, list
# for i in [0,1,2]:
#     print("meow")

#better way
# for _ in range(3): #you can use underscore for counter if you dont need it
#     print("meow")

#pythonic way
# print("meow\n" * 3, end='')#omg

# while True:
#     n = int(input("Give me a positive value: "))
#     if n > 0:
#         break#breaking the iteration and coming back to beginning of loop

# for i in range(n):
#     print("meow")

#
def main():
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


main()
