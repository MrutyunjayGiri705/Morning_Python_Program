# While creating a function, pass a * before the parameter name while defining the function. 
# The function accesses the arguments by processing them in the form of tuple.
def add(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    print("The sum is:", sum)
add(2, 3)
add(5, 10, 15)




# While creating a function, pass a * before the parameter name while defining the function. 
# The function accesses the arguments by processing them in the form of dictionary.
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Ku.", lname = "Giri", fname = "Mrutyunjay")