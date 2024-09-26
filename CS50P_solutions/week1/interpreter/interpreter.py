def Main():
    Expression = input("Expression: ")
    Expression = Expression.split(" ")
    x = int(Expression[0])
    y = Expression[1]
    z = int(Expression[2])
    Result = Operation(x, z, y)

def Operation(Val1, Val2, Opr):
    if Opr == "+":
        Result = Val1 + Val2
    elif Opr == "-":
        Result = Val1 - Val2
    elif Opr == "/":
        Result = Val1/Val2
    elif Opr == "*":
        Result = Val1 * Val2
    else:
        print("Give valid operator!")
    return print(f"{Result:.1f}")

Main()
