try:
    x = int(input())
    y = int(input())
    print(x / y)
except (ZeroDivisionError, ValueError):
    print("Invalid input or division by zero")
