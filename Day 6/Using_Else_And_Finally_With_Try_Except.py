try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Division performed successfully.")
finally:
    print("Execution completed.")