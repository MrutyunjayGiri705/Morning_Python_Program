def square(num):
    """This function returns the square of the given number."""
    return num ** 2

number = int(input("Enter a number to find its square: "))
result = square(number) 
print(f"The square of {number} is {result}")
print(square.__doc__)