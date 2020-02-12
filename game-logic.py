import requests
from requests.exceptions import HTTPError
import sys

from azramind_func import azramind
from util import game_rules, get_code_list


# url for the api for the backend that I built for this project
BASE_API_URL = "https://azramind.herokuapp.com"
# BASE_API_URL = "http://localhost:5000"


print("\nWelcome to Azramind! A game where you must guess the code to win. Do you have what it takes?\n\n")
q = False
while q is False:

    # number of tries a player gets to guess the code.
    limit = 11
    command = input(
        '''Please enter a command:
    1 Play the game
    2 rules of the game
    3 view scores
    q quit game
            ''')

    # lowercase + remove white spaces
    command = command.lower().strip()

    if command == "1":
        print("""\n\nSo, you want to try your luck? First, you must tell me who you are \n\n""")

        # while I don't have a valid username
        user_obj = None
        # this loop saves the username object so we can save scores
        while user_obj is None:
            # initializing the response object
            response = None
            command = input(
                '''Enter a command:
            a create a new username
            b enter an existing username
                ''')

            command = command.lower().strip()

            if command not in {'a', 'b'}:
                print('\nInvalid input, please enter a or b\n')

            else:
                username_input = input("Enter username: ").lower().strip()
                username_obj = {"username": f"{username_input}"}
                username_url = f"{BASE_API_URL}/user"

                if command == "a":

                    # put the conditions for username creation here:
                    if len(username_input) < 4:
                        print('\nyour username must be at least 4 characters long\n')
                    else:
                        response = requests.post(
                            username_url, data=username_obj).json()

                if command == "b":

                    response = requests.get(
                        username_url, data=username_obj).json()

            if response:
                if 'username' in response:
                    user_obj = response
                if 'message' in response:
                    print(response['message'])

        # URL to access the random number generator API
        INT_URL = "https://www.random.org/integers/"

        # INT_URL parameters
        INT_URL_PARAMS = {
            'num': 4,  # num digits requested
            'min': 0,  # min int
            'max': 4,  # max int
            'col': 1,
            'base': 10,
            'format': 'plain',
            'rnd': 'new'
        }

        # function inside util.py accesses API to generate the 4 digit code list
        try:
            code_list = get_code_list(INT_URL, INT_URL_PARAMS)
        except:
            print("the code couldn't be generated, we can't play the game!")

        score_obj = azramind(code_list, limit=11)
        print(f"{score_obj} \n")
        print(f"{user_obj}\n")
        score_obj["user_id"] = user_obj["id"]
        score_url = f"{BASE_API_URL}/score"

        # posting the score to the scores table
        response = requests.post(score_url, data=score_obj).json()

    elif command == "2":
        game_rules(limit)

    elif command == "3":
        username = input("Please enter your username to view past scores: ")
        GET_SCORES_URL = f"{BASE_API_URL}/{username}/scores"
        response = requests.get(url=GET_SCORES_URL).json()

        if response:
            if 'message' in response:
                print(response)
            elif 'score' in response:
                for score in response['scores']:
                    print(score)
            else:
                print('something went wrong, we had trouble retrieving your scores')

    elif command in {"q", "quit"}:
        print("thank you for playing, good bye")
        q = True

    elif command not in {"1", "2", "3", "q"}:
        print("\nInvalid input. Possible command values are 1, 2, 3, or q. Please try again.\n")
