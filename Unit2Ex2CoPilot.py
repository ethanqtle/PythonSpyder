# The program works as follows: you (the user) thinks of an integer 
# between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, 
# and you give it input - is its guess too high or too low? Using bisection
# search, the computer will guess the user's secret number!

# All values should be integers!
# Initialize variables
numGuesses = 0
low = 0
high = 100
ans = (high + low) // 2

# Print initial message
print("Please think of a number between 0 and 100!")

# Loop until the user indicates that the guess is correct
while high > low:
    # Calculate the midpoint of the current range
    ans = (high + low) // 2
    # Ask for user input on whether the guess is too high, too low, or correct
    print("Is your secret number " + str(ans) + "?")
    userInput = input("Enter 'h' to indicate the guess is too high. " +
                        "Enter 'l' to indicate the guess is too low. " +
                        "Enter 'c' to indicate I guessed correctly. ")
    # If the guess is too low, set the lower bound to the guess
    if userInput == "l":
        low = ans
    # If the guess is too high, set the upper bound to the guess
    elif userInput == "h":
        high = ans
    # If the guess is correct, set the result to the guess and break
    elif userInput == "c":
        result = ans
        break
    # If the user input is invalid, print an error message
    else:
        print("Your input was invalid. Please try again.")

# Print the result
print("Game over. Your secret number is", str(result))