import random

mynum = random.randint(1,9)

step = 3
while(step>0):
    num = int(input("enter your guess you between 1-9:"))
    if num == mynum:
        print("Your guess is right")
        break
    else:
        step-=1
        print(f"Your guess is wrong now you have {step} tries left")
print(mynum)