
#while True:
   # print("its true")
#while False:
    #print("its true")
    #executes continually ass long as the expression is true
#i=10
#while i>0:
    #print(i)#it will print out an infinite loop
    #i-=1#i=i+1 cancels out the loop


import random
random_num =random.randint(1,21)
print(random_num)
start =1
name=input("hello,what is your name?")
print(name +",am thinking of a number between 1-30?.can you guess the number?")

while start <=5:

    guess=int(input("guess a number:"))
    start +=1
    print(start)
    guessLeft = 5-start
    if guess<random_num:
        guessleft =str(guessleft)
        print("your guess is to low! you have"+guessLeft+"guesses left")
    elif guess>random_num:
        guessleft =str(guessleft)
        print("your guess is to high! you have"+guessLeft+"guesses left")
    else:
        pass
        break

    if guess== random_num:
        start =str(start)
        print("good job!!!you have guessed correct")


    elif guess!=random_num:
        start =str(start)
        print("sorry ")















