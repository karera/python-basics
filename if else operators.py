# if (test expression)
if 10 +10 ==20:
    print("nelius")
#if its false it jumps to else
if 10+10 ==22:
    print("nelius")
else:
   print ("10+10 !=22")
#elif statement
marks = int(input("Enter Your Marks"))
if marks>=80 and marks <=100:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=60:
    print("Grade C")
elif marks>=50:
    print("Grade D")
elif marks>=0 and marks<=50:
    print("FAIL")
else:
    print("INVALID MARKS")

