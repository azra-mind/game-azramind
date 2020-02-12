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
            f'HTTP error, unable to generate 4 digit code from random Integer API: {http_err}')
    except Exception as err:
        # Python 3.6
        sys.exit(
            f'Other error occurred, unable to generate 4 digit code from random Integer API: {err}')

    # a list of number strings from the response
    num_str_list = response.text.splitlines()

    return num_str_list


def game_rules(limit=10):

    print(f'''
    THESE ARE THE RULES:
    *I will select 4 random integers from 0 to 7. 
    *You have {limit} tries to guess which 4 integers I've selected.
    *After each try, I will disclose the number of digits and their placement you guessed correctly.
    *I will also disclose the number of digits you guessed correctly without guessing their correct placement.
    *If you are able to guess the code correctly in {limit} tries, you become a Mastermind!
    ''')


def quit_function(string):
    if string.lower() in {"q", "quit"}:

        sys.exit("\nthank you for playing Azramind, good bye\n")


# this function validates guesses and
def validate_guess(string, n=4):

    message = "Invalid input, your input must be a 4 digit integer"

    if len(string) != n:
        print(message)
        return False
    try:
        int(string)
    except ValueError:
        print(message)
        return False

    return True
