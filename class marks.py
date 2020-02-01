math =int(input("enter marks"))
english =int(input("enter marks"))
kiswahili =int(input("enter marks"))

if math >100  or english >100 or  kiswahili >100:
    print("INVALID")
else:
    print("enter values <=100")
Total =math+english+kiswahili
avarage =Total/3
print("your Total marks",Total)
print("Total avarage",avarage)
if avarage>=80 and avarage <=100:
    print("Grade A")
elif avarage >=70 and avarage<=79:
    print("Grade B")
elif avarage >=60 and avarage <=69:
    print("Grade c")