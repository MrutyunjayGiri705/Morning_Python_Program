def multiple_returns(a,b):
    return a+b, a-b, a*b, a/b


result = multiple_returns(10, 5)
print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Quotient:", result[3])
