try:
    x=int(input("Enter a number: "))
    y=10/x
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
