def password_checker(password):
    validity = ""
    symblos = "$#@"
    if 6<=len(password)<=16:
        validity += "v"
        for i in password:
            if i.isdigit:
                validity += "a"
                break
        if validity=="va":
            for i in password:
                if i in symblos:
                    validity += "l"
                    break
        if validity=="val":
            for i in password:
                if i.isalpha():
                    if i.islower():
                        validity+="i"
                        break
        if validity=="vali":
            for i in password:
                if i.isalpha():
                    if i.isupper():
                        validity+="d"
                        break             
    else:
        print("Minimum lenght 6 characters\nMaximum length 16 characters")
    return validity

password = input("Enter password : ")
validity = password_checker(password)
if validity=="valid":
    print("Password is valid")
else:
    print("Password is invalid")