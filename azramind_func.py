import requests
from requests.exceptions import HTTPError
import sys


# API parameters


# turn it into a string to make it easier to compare with inputs
def azramind(code_list, limit):

    # uncomment below to see the code list:
    # print(code_list)

    code_str = "".join(code_list)
    guesses = []

    n = input(" Pick 4 numbers between 0 and 7 to guess the 4 digit code:\n")

    guesses.append(int(n))

    tries = 1
    while (n != code_str and tries < limit):

        # guesses that were made.
        tries += 1

    # like the boardgame, black = count of correct number + location, white = correct # only
        black = 0
        white = 0

        # making copies of code_str_list to manipulate as needed
        black_temp_code = code_list.copy()
        white_temp_code = code_list.copy()

        for i in range(0, len(code_list)):

            # checking for equality of digit + location
            if (n[i] == black_temp_code[i]):
                # number of digits + locations guessed correctly increments
                black += 1

            # checking for equality of digit only
            if(n[i] in white_temp_code):
                # number of digit guessed correctly increments
                white += 1

                # remove the digit to avoid double counting
                white_temp_code.remove(n[i])

        # number of times digits guessed correctly but location guessed incorrectly
        white = white-black

        # if not all the digits are guessed correctly:
        if (black != 4):
            if (black > 0):
                print(
                    f"\nYou guessed {black} digits including their placement correctly")
            if (white > 0):
                print(
                    f"\nYou guessed {white} digits correctly but got their placement wrong")

            if (black == 0 and white == 0):
                print("None of the numbers in your input match.")

            print(f"\nyou have {limit-tries} tries remaining")
            print("\nthese are your previous tries:")
            for g in guesses:
                print(g)

            n = (input("\nEnter your next choice of numbers: "))
            guesses.append(int(n))

        # when none of the digits are guessed correctly.

    # condition for equality.
    if n == code_str:
        print("You've become a Mastermind!")
        if tries == 1:
            print(f"WHOA!! You guessed it right on the first try that's impressive!!")
        else:
            print(f"It took you {tries} tries.")
    else:
        print(
            f"I'm sorry, you've exceeded {limit} tries. The code is {code_str}. You'll get it next time!")

    score_json_obj = {
        "difficulty": limit,
        'num_tries': tries,
    }

    return score_json_obj
