sum=lambda a,b: a+b
difference=lambda a,b: a-b

sum_result = sum(10, 5)
print("Sum:", sum_result)
difference_result = difference(10, 5)
print("Difference:", difference_result)






l=[11,21,3,4,-3,12,-2,-5,-9,8,-7]
a=list(filter(lambda x: x>0, l))
print("Positive numbers:", a)