import  random
n= random.randint(1,20)
number_of_guesses=1
print("I am guessing a number between 1 and 20 ")



while (number_of_guesses <= 9) :

    guess_number = int(input("Guess the number: \n"))
    if guess_number< n:
        print("Your guess is too low \n")

    elif guess_number > n :
        print("Your Guess is too high\n")
    else:
        print(" Hurrah! You have Guessed the Correct Number")
        print("You won the game")
        print("You took",number_of_guesses, "to guess the correct number")


        break




    print(9 - number_of_guesses , "number of guesses left\n")
    # print("Guess the number again: ", end=" ")
    number_of_guesses= number_of_guesses +1

if number_of_guesses>9 :
    print("You lost the game\n")
    print("Game Over")









