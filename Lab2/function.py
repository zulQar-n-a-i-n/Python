# def keyword is used to define function in python

# function to give factorial of a number

def fact():
    num = int(input("Enter number : "))

    fact = 1

    for i in range(1,num+1):
        fact*=i

    print(f"Factorial of {num} is ",fact)


# calling function
fact()
    