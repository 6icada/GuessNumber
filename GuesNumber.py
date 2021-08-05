#Code by 6icada
#Please do not copy code


#Adding libraries
import random

#Adding vars
Lvl1Number = random.randint(1, 10) #Ganarating random number from 1 to 10
y = 1

#MSG
print("[Level 1][MSG]: Guess number in 1-10!")
print("[Level 1][WARN]: You have only 3 chanses!\n")

#With this i am giving user 3 chances to guess Lvl1Number
while y <= 3:
    #User input
    userInput = int(input("[Level 1][MSG]: Guess: "))

    if userInput == Lvl1Number:
        #MSG if user won
        print("[Level 1][MSG]: You won!")

        #Going to Level 2
        #MSG
        print("[MSG]: Now guess number in 1-20")
        print("[Level 1][WARN]: You have only 3 chanses!\n")

        #Adding vars
        Lvl2Number = random.randint(1, 20) #Generating random number from 1 to 20
        y = 1

        #Giving user 3 chances to guess number
        while y <= 3:
            #User input
            userInput = int(input("[Level 2][MSG]: Guess: "))

            if userInput == Lvl2Number:
                #MSG if user won
                print("[Level 2][MSG]: You won!")

                #Breaking program
                break
            else:
                #Warning
                print("[Level 2][MSG]: Try again!")
            
            y += 1
        
        if userInput != Lvl2Number:
            #MSG if user lose
            print("[Level 2][MSG]: You failed!")
            print(f"[Level 2][MSG] Number was {Lvl2Number}")
        
        #Breaking program
        break
    else:
        #MSG
        print("[Level 1][MSG]: Try again!")
    
    y += 1

if userInput != Lvl1Number:
    #MSG if user lose
    print("[Level 1][MSG]: You failed!")
    print(f"[Level 1][MSG]: Number was: {Lvl1Number}")