# count letters of string except vowels

given = input("Enter string : ")

length = 0
for i in given:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
        continue
    length += 1

print(f"Number of letters in {given} is {length}")
