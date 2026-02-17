x=10
def My_function():
    y=5
   
    print(y)



My_function()
print(x)


x=10
def My_function1():
    global x
    x=20
    y=5
   
    print(y)



My_function1()
print(x)