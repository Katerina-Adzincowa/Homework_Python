"""Implement a program with calculator functionality for operations on two numbers."""

print("--- CALCULATOR ---")


try:
    num_1 = float(input("Enter first number: "))
    operation = input("Operation implementation (+, -, *, /): ")
    num_2 = float(input("Enter second number: "))

    if operation == '+':
        print(f"Answer: {num_1 + num_2}")

    elif operation == '-':
        print(f"Answer: {num_1 - num_2}")

    elif operation == '*':
        print(f"Answer: {num_1 * num_2}")

    elif operation == '/':
        if num_2 == 0:
            print("Error! You can't devide by zero!!!")
        else:
            print(f"Aswer: {num_1 / num_2}")

    else:
        print("Not correct operation!")

except ValueError:
    print("Error! You have to input numbers!")