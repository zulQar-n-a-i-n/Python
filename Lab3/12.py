def to_decimal(n):
    sum = 0
    j=3
    for i in n:
        sum += int(i)*(2**j)
        j-=1
    return sum
# print(to_decimal('1010'))
    
list1 = []
print("Enter sequence of 4 digit binary numbers : to stop enter blank line")
while(True):
    num = input()
    if num != "":
        list1.append(num)
    else:
        break
list2 = []
for i in list1:
    list2.append(to_decimal(i))

list3 =[]
j=0
for i in list2:
    if i%5==0:
        list3.append(list1[j])
        j+=1

print(list3)

