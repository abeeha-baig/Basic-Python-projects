import math

def add(x, y):
    return x + y
def subtract (x, y):
    return x - y
def multiply (x, y):
    return x * y
def divide (x, y):
    return (x / y)
def square (x):
    return x ** 2
def cube (x):
    return x ** 3
def square_root (x):
    return math.sqrt(x)
def cube_root (x):
    return x ** (1/3)

while True:
    print("which operation do you want to choose?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. cube")
    print("7. square root")
    print("8. cube root")
        
    choice = input("enter your choice of operation (1-8)? ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
        if choice != '5' and choice != '6' and choice != '7' and choice != '8':
            a = int(input("enter first number: "))
            b = int(input("enter second number: "))

            if choice == '1':
                print(a, "+", b, "=", add(a, b))
            elif choice == '2':
                print(a, "-", b, "=", subtract(a, b))
            elif choice == '3':
                print(a, "*", b, "=", multiply(a, b))
            elif choice == '4':
                print(a, "/", b, "=", divide(a, b) )
        elif choice == '5':
            num = float(input("Enter a number: "))
            print("Square of", num, "=", square(num))
        elif choice == '8':
            num = float(input("enter a number: "))
            print("cube root of", num, "=", cube_root(num))
        elif choice == '6':
            num = float(input("enter a number: "))
            print("The cube of", num, "=", cube(num))
        else:
            num = float(input("Enter a number: "))
            print("square root of", num, "=", square_root(num))

        repeat = input("do you want to perform more calculations? (yes/no): ")

        if repeat.lower() == "no":
            break
    else:
        print("invalid input: Try Again!")