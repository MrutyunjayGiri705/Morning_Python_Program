try:
    x = int("abc")
except:
    print("Something went wrong")


try:
    x=int(input("Enter a number: "))
    y=10/x
except :
    print("Error: Division by zero is not allowed.")
