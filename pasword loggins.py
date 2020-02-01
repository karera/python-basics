password = (input("Enter My Password"))
if len(password)<5:
    print("to short")
elif len(password)>10:
    print("to long")
elif len(password)>5 and len(password)<10:
    print("loggin successfull")






