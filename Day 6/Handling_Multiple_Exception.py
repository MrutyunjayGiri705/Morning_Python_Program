try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")