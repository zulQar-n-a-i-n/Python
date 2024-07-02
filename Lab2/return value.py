def myfunction():
    num = int(input("Enter num : "))
    count = 0
    for i in range(num+1):
        count+=i

    return count


print("Sum of numbers upto given number is ",myfunction())