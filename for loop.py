numbers=[1,2,3,4,5]
#each-reps our variable||numbers in our sequence
for each_item in numbers:
    if each_item%2==0:
        print(each_item ,"is even")
    else:
       print(each_item,"is odd")

    #addding one to each element in the string


    #checking if each item is even or odd

for i in range(1,101):
    if (i % 3 == 0) and (i % 5 == 0):
        print(i, "fizzbuzz")
    elif (i%3==0) :
        print(i,"fizz")
    elif(i%5==0):
            print(i,"buzz")
    else:
            print(i)

