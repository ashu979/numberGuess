import sys
import os 
import time
import datetime
import math
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.\n\nChoose a difficulty level : ")

flag = True

while(flag):
    
    print("\n\nPlease select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n4. To Quit!")
    
    num = random.randint(1,100)

    print("\nEnter your choice: ")

    userInput = sys.stdin.readline().strip()

    if int(userInput) == 1 :
        print("Great! You have selected the Easy difficulty level.\nLet's start the game!\n\n")
        numOfItr = 10
    elif int(userInput) == 2:
        print("Great! You have selected the Medium difficulty level.\nLet's start the game!\n\n")
        numOfItr = 5
    elif int(userInput) ==3 :
        print("Great! You have selected the Hard difficulty level.\nLet's start the game!\n\n")
        numOfItr = 3
    elif int(userInput) ==4 :
        quit()
    else:
        print("Enter Valid Number !!")
        quit()

    startTime = time.time()
    cnt = 1

    while(numOfItr>0):
        print("Enter your guess (between 1 to 100): ")
        guess  = sys.stdin.readline().strip()

        if int(guess) == num : 
            print(f"\nCongratulations! You guessed the correct number in {cnt} attempts.")
            print(f"Total time taken by you to guess the number : {round((time.time()-startTime),3)} seconds")
            break
        elif int(guess) < num:
            print(f"Incorrect! The number is greater than {guess}.\n")
        else :
            print(f"Incorrect! The number is less than {guess}.\n")
        
        cnt+=1
        numOfItr-=1


    if numOfItr<=0 :
        print("Oops, you lost the Game !!")
    

    print("\nYou want to play Again! \n   Enter 1 for yes \n   Enter 2 to Quit!!")

    decision = sys.stdin.readline().strip()
    if int(decision) ==2 :
        print("Thank You Playing!")
        quit()
    elif int(decision) ==1 :
        flag == True
        pass

    
        
    