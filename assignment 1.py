string1 = "nelius"
print(string1)
print(len(string1))

#write python program to cal length of program
# Write a Python program to count the occurrences of the word "python" in a given sentence
sentence ="We are learning how to program in python. I find python programming fun"
occ =sentence.count ("python")
print(occ)

#data sets ways of managing data in memeory
# in python 1 list-represented

# creating a list in python- list are mutable
myNumbers =[1,2,3,4,5,6,7,8,9]
myFloats =[10.0,12.1,134.1,14.9,13.5]
myPets =["chicken","dog","cat","pigeon"]
myBool =[True,True,False,False,True]
mixedType =[1,"dog",10.9,True]
list_of_list =[[1,2,3,4],[10,"10",True],[10.5],[9,9, False]]
#list indexing
print("get number7",myNumbers[-2])
# list slicing
x =myNumbers
sliceChars =myNumbers[1:4]
#another slicing method
print("+slicing",myNumbers[1:5])

print(sliceChars)
#list reversing
x =myNumbers
print(myNumbers[::-9])
#another method
print("reversed",myNumbers[::-2])
#get true only from list of list
print(list_of_list[1][2])
print(list_of_list[3][2])


