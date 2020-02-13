import requests
from requests.exceptions import HTTPError
import sys


# takes a url and parameters to make a GET request to the integers API and return the response
def get_code_list(URL, PARAMS):
    # getting the response with the 4 random numbers from then API:
    try:
        response = requests.get(
            url=URL, params=PARAMS)
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        # Python 3.6
        sys.exit(
            f'HTTP error, unable to generate code from random Integer API: {http_err}')
    except Exception as err:
        # Python 3.6
        sys.exit(
            f'Other error occurred, unable to generate code from random Integer API: {err}')

    # a list of number strings from the response
    num_str_list = response.text.splitlines()

    return num_str_list


def game_rules(limit=10, difficulty=4):

    print(f'''
    THESE ARE THE RULES:
    *I will select {difficulty} random integers from 0 to 7. 
    *You have {difficulty} tries to guess which {difficulty} integers I've selected.
    *After each try, I will disclose the number of digits and their placement you guessed correctly.
    *I will also disclose the number of digits you guessed correctly without guessing their correct placement.
    *If you are able to guess the code correctly in {difficulty} tries, you become a Mastermind!
    ''')


def quit_function(string):
    if string.lower() in {"q", "quit"}:

        sys.exit("\nthank you for playing Azramind, good bye\n")


# this function validates guesses and
def validate_guess(string, difficulty=4):

    message = f"Invalid input, your input must be a {difficulty} digit integer"

    if len(string) != difficulty:
        print(message)
        return False
    try:
        int(string)
    except ValueError:
        print(message)
        return False

    return True
