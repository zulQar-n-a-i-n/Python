lst = [0,1]
for i in range(1,50):
    if lst[i]+lst[i-1] <= 50:
        lst.append(lst[i]+lst[i-1])
    else :
        break

print(lst)