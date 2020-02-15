import requests
from requests.exceptions import HTTPError
import sys


# takes a url and parameters to make a GET request to the integers API and return the response
def get_code_list(URL, PARAMS):
    # getting the response with the 4 random numbers from then API:
    try:
        response = requests.get(
            url=URL, params=PARAMS)
        # If the response was successful, no exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:

        sys.exit(
            f'HTTP error, unable to generate code from random Integer API: {http_err}')
    except Exception as err:

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


# this function validates guesses
def validate_guess(string, difficulty=4):

    message = f"Invalid input, your input must be a {difficulty} digit integer between 0 and 7"

    if len(string) != difficulty:
        print(message)
        return False
    if "8" in string or "9" in string:
        print(message)
        return False
    try:
        int(string)
    except ValueError:
        print(message)
        return False

    return True


# this function posts the username to the db and returns it in an object
# args are: quit_function to enable user exit, API url to ping the DB, requests
def post_and_return_username(quit_function, BASE_API_URL, requests):

    # initializing the response object
    response = None
    command = input(
        '''Enter a command:
                a create a new username
                b enter an existing username
                    ''')

    command = command.lower().strip()

    # quit if user enters q or quit
    quit_function(command)

    if command not in {'a', 'b'}:
        print('\nInvalid input, please enter a or b\n')

    else:
        username_input = input("Enter username: ").lower().strip()

        # quit if user enters q or quit
        quit_function(username_input)

        username_obj = {"username": f"{username_input}"}
        username_url = f"{BASE_API_URL}/user"

        if command == "a":

            # put the conditions for username creation here:
            if len(username_input) < 3:
                print(
                    '\nyour username must be at least 3 characters long\n')
            else:
                response = requests.post(
                    username_url, data=username_obj).json()

        if command == "b":

            response = requests.get(username_url, data=username_obj).json()

    if response:
        # return response if username is there
        if 'username' in response:

            print(f"Hello, {response['username']}")
            return response

        # print error message if no username
        if 'message' in response:
            print(response['message'])
