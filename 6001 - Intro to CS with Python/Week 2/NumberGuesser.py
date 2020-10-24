# This program uses bisection search and user input to hone in on a number between 0-99


low = 0
high = 100

print("Please think of a number between 0-100!")

while (1):
    guess = int ((low+high)/2)
   
    print("Is your secret number " + str(guess) + "?")

    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low.", end=" ")
    x = input("Enter 'c' to indicate I guessed correctly. ")
    

    if(x == 'h'):
        high = guess
        continue
    elif(x == 'l'):
        low = guess
        continue

    elif(x == 'c'):
        print("Game over. Your secret number was: " + str(guess))
        break

    else:
        print("Sorry, I did not understand your input.")
        continue

    
        
