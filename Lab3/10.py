from numpy import *
rows = int(input("Enter number of rows : "))
col = int(input("Enter number of columns : "))

arr =array([[0 for i in range(col)] for j in range(rows)])
# print(arr)
for i in range(rows):
    for j in range(col):
        arr[i][j] = i*j


print(arr)