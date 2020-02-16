import requests
from requests.exceptions import HTTPError
import sys
from util import quit_function, validate_guess

# this file contains the main game play function

# args:
# quit_function lets user quit anytime.
# validate_guess function checks if the guess the user entered is a valid input
# limit is the number of tries, difficulty is the number of digits in the secret code


def azramind(code_list, limit=10, difficulty=4):

    # uncomment below to see the code list for debugging etc:
    # print(code_list)

    code_str = "".join(code_list)

    # this is where we'll keep track of guesses and results
    guess_results = []

    print(
        f"Enter {difficulty} integers between 0 and 7 to guess the {difficulty} digit code.\n")

    # the variable where we store user guesses
    guess = None

    tries = 0
    while (guess != code_str and tries < limit):

        guess = (input("\nEnter your guess here: "))

        # if user inputs q or quit, this function exits the program
        quit_function(guess)

        # function that validates the guess is a {difficulty} digit integer
        valid_guess = validate_guess(guess, difficulty)

        # if the guess is valid ()
        if valid_guess:
            tries += 1

            # like the boardgame, black = # of correct number + location, white = correct # only
            black = 0
            white = 0

            # making copies of the code list to check for equality of digits and manipulate as needed to avoid pass by reference errors
            black_temp_code = code_list.copy()
            white_temp_code = code_list.copy()

            for i in range(0, len(code_list)):

                # checking for equality of digit + location
                if (guess[i] == black_temp_code[i]):

                    # number of digits + locations guessed correctly increments
                    black += 1

                # checking for equality of digit only
                if(guess[i] in white_temp_code):

                    # number of digits guessed correctly increments
                    white += 1

                    # remove digit to avoid double counting
                    white_temp_code.remove(guess[i])

            # number of times digits guessed correctly but location guessed incorrectly
            white = white-black

            # if not all the digits guessed correctly:
            if (black != difficulty):
                if (black > 0):
                    print(
                        f"\nYou guessed {black} digits including their placement correctly")
                if (white > 0):
                    print(
                        f"\nYou guessed {white} digits correctly but got their placement wrong")

                if (black == 0 and white == 0):
                    print("None of the numbers in your input match.")

                guess_results.append({
                    'guess': guess,
                    'correct digit & placement': black,
                    'correct digit only': white,
                    'guesses remaining': (limit-tries)
                })

                print(f"\nyou have {limit-tries} guesses remaining")
                print("\nthese are your previous guesses:")
                for g in guess_results:
                    print(g)

    # out of the while loop conditions for equality or reaching the guess limit
    if guess == code_str:
        print("\nYou've conquered Azramind!")
        if tries == 1:
            print(f"\nWHOA!! You guessed it right on the first try that's impressive!!\n")
        else:
            print(f"It took you {tries} tries.\n")
    else:
        print(
            f"I'm sorry, you've exceeded {limit} tries. The code is {code_str}. You'll get it next time!\n")
        # to indicate in the scores table that the user exceeded 10 tries, didn't win
        tries = limit+1

    score_obj = {
        "difficulty": difficulty,
        'num_tries': tries,
    }

    return score_obj
