#creating a class
# class Car:
#     make ='toyota'
#
# car1 =Car()
# car1.yom =2012
#
# car2 =Car()
#
# print(car1.yom)

# class Laptop:
#     make ="HP"
#
#     #switch on
#     def switch_on(self):
#         print("-----LOADING----")
#         #type
#     def type(self):
#          print("----typing---")
#
# elitebook=Laptop()
# elitebook.RAM="2GB"
# elitebook.HDD ="500GB"
# elitebook.screen_size ="15.6 inch"
# print(elitebook.make)
# print(elitebook.HDD)
# elitebook.switch_on()
# elitebook.type()
#
# pavillion=Laptop()
# pavillion.RAM="8GB"
# pavillion.HDD ="500GB"
# pavillion.screen_size ="15.6 inch"
#
# envy=Laptop()
# envy.RAM="4GB"
# envy.HDD ="500GB"
# envy.screen_size ="15.6 inch"




class Person:

    #creating a constructor
    def __init__(self,name,age,kgs):
        self.theName = name
        self.theAge = age
        self.theKgs = kgs
        #update the age
    def update_age(self,newAge):
        self.theAge=newAge
    def update_name(self,newName):
        self.theName=newName


nelius = Person("nelius",12,65)

print("initial age:", nelius.theAge)
nelius.update_age(14)
print("current age:", nelius.theAge)

print("initial name:", nelius.theName)
nelius.update_name("Karera")
print("current name:", nelius.theName)



