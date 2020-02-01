username ="mark"
email = "mark@gmail.com"
password= "1234567"

print("welcome to facebook")

usr =input("enter username:")
if usr==  username:
    em= input ("enter email:")
    if em== email:
        passw =int(input("enter password"))
        if passw==password:
            print("login successfull")
            pass

        else:
            print("incorrect password")
    else:
        print("incorrect email")
else:
    print("incorrect username")







