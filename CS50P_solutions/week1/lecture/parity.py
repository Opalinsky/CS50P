# x = int(input("What's x? "))
# if x % 2 == 0:
#     print("Even")
# else:
#     print("odd")
def main():
    x = int(input("What's x? "))
    if is_even(x): #if our function return true => print
        print("Even")
    else:
        print("Odd")

def is_even(n):
    # if n % 2 == 0:
    #     return True #returning boolean value
    # else:
    #     return False

    #if else shorter version
    # return True if n % 2 == 0 else False

    #if shortest version
        return n % 2 == 0
main()

