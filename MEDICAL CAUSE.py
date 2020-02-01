ex = int(input("number of classes attended"))
les =int(input("number of classes held"))
yesChoice =["yes","y"]
noChoice =["no","n"]
md=(input("do you have a medical cause? (Y/N)")).lower()

percantage= (ex/les)*100
print(percantage)

if percantage >100:
    print("invalid")
    if ex > 75:
        if md in yesChoice and ex < 75:
            print("you qualify for exams")
        elif md in noChoise and ex<75:
            print("you do not qualify for exams")







