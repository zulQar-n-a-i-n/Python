word = ""
while(True):
    txt=input("Enter lines : ")
    if txt!="":
        word+=txt.lower()+"\n"
    else:
        break
print(word)
