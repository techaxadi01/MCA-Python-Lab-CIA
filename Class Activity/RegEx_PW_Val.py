# Password Validation - Password should contain at least 8 char, 1 Upper case, 1 lower case, 1 digit, 1 spl char

import re

while True:
    pw = input("Enter Password : ")

    print("Method 1 :")

    try:
        low = re.search(r"[a-z]", pw)
        upp = re.search(r"[A-Z]", pw)
        dig = re.search(r"[0-9]", pw)
        spl = re.search(r"[^A-Za-z0-9]", pw)

        if len(pw) >= 8 and low and upp and dig and spl:
            print("Valid Password")
            break
        else:
            print("Invalid Password. Try again.")
            print("Password must contain at least 8 characters, 1 uppercase, 1 lowercase, 1 digit, and 1 special character.")


        print("Method 2 :")
        ptt = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d]).{8,}$"

        if re.match(ptt,pw):
            print("Valid Password")
            break
        else:
            print("Invalid Password. Try again.")
            print("Password must contain at least 8 characters, 1 uppercase, 1 lowercase, 1 digit, and 1 special character.")
        
    except Exception as err:
        print("Error : ", err)
        print("An Error Occured Try Again")