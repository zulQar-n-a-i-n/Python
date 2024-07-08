even=0
odd=0
list1=[]
while(True):
    num=int(input("to terminate input enter -1 otherwise something else : "))
    if num !=-1:
        list1.append(num)
    else:
        break

for i in list1:
    if i%2==0:
        even+=1
    else:
        odd+=1


print("Even numbers : ",even)
print("odd numbers : ",odd)
