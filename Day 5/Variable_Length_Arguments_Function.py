#*args
def numbers(*args):
    print(args)



numbers(1, 2, 3, 4, 5)




#**kwargs
def MyDetails(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key} : {value}")


MyDetails(name="John", age=30, city="New York")