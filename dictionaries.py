
myList =(1023,43546,678345,54767)
print(max(myList))
myList =(1,2,3,4,5,6,7,8,9,10)
list_b=[]
list_b.append(myList[0])
list_b.append(myList[8])
print(list_b)
#print mylist into 2 parts
x=1,2,3,4,5,6,7,8,9,10
print(x[0],x[1],x[2],x[3],x[4])
print (x[5],x[6],x[7],x[8],x[9])

print(x[0:5])
first_half =(x[0:5])
second_half =(x[5:])
first_to_string =str(first_half)
second_to_string =str(second_half)
print(first_to_string.strip("()"))
print(second_to_string.strip("()"))

