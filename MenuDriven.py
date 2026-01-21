def area():
    a = int(input("Enter side of cube: "))
    print("Area of cube =", 6 * a * a)


def add():
    b = int(input("Enter first number: "))
    c = int(input("Enter second number: "))
    print("Sum =", b + c)


def fibo():
    n = int(input("Enter number of terms: "))
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def check_num():
    n = int(input("Enter a number: "))
    ch = int(input("1. Even/Odd\n2. Prime\nEnter choice: "))

    if ch == 1:
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")

    elif ch == 2:
        if n <= 1:
            print("Not Prime")
        else:
            for i in range(2, int(n/2) + 1):
                if n % i == 0:
                    print("Not Prime")
                    return
            print("Prime")

    else:
        print("Invalid Choice")


while True:
    print("\nMENU")
    print("1. Area of Cube")
    print("2. Add Two Numbers")
    print("3. Fibonacci Series")
    print("4. Check Even/Odd or Prime")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        area()
    elif choice == 2:
        add()
    elif choice == 3:
        fibo()
    elif choice == 4:
        check_num()
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
