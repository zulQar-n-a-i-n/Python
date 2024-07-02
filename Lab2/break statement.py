# break loop at first vowel

given = input("Enter string : ")

length = ""
for i in given:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' :
        break
    length += i

print(f"First vowel comes after substring \"{length}\"")