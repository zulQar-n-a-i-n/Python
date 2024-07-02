# function to print square of a given number

def sqr(n):
    print(f"Square of {n} is {n**2}")


sqr(4)

# default parameters
def show(name = "Ali"):
    print(f"My name is {name}")

show("hamza")
show()

# list as parameter
def func(l):
    for i in l:
        print(i)

list1 = [1,2,3]
func(list1)