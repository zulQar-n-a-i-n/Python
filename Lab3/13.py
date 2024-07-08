given = input("Enter string : ")
digit = 0 
letters = 0

for i in given:
    if i != " ":
        if i.isdigit():
            digit+=1
        elif i.isalpha():
            letters+=1
        else:
            continue


print(f"Digits = {digit} \nLetters = {letters}")