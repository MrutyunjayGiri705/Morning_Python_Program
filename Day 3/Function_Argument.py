def average(a=9, b=11):
    return (a + b) / 2



result1 = average()
print("Average with default arguments:", result1)
result2 = average(5, 15)
print("Average with provided arguments:", result2)
result3 = average(20)
print("Average with one provided argument:", result3)
result4 = average(b=25)
print("Average with one named argument:", result4)
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")

def func(*args):
    for arg in args:
        print(arg)  
        print(len(args))


func(1, 2, 3, 4, 5)