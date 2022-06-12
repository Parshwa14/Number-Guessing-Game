n = 88
guess = " "
guess_count = 1
print("YOU HAVE 9 CHANCES TO GUESS THE NUMBER")

while guess_count <= 9 and guess != int(n):
    # taking input from user and converting it to integer
    guess = int((input("ENTER YOUR GUESS:\n")))
    
    if guess > int(n):                                
        print("ENTER A SMALLER NUMBER\n")
    
    elif guess < int(n):
        print("Your Guess is Too Low, Enter a Bigger Number\n")
    
    else:
        print("YOU WON!!!\n")
        print("It took you", guess_count, "Tries to Guess The Number")
        break                   # if guess = the secret number the process will stop              
    
    guess_count = guess_count + 1
    print("You Have Left", 10 - guess_count, "Guesses")
    
    if guess_count > 9:           # if number of guesses will be more than 9 it will print game over and the program ends
        print("GAME OVER")
