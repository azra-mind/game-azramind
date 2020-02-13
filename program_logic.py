import requests
from requests.exceptions import HTTPError
import sys

from azramind_func import azramind
from util import game_rules, get_code_list, quit_function


# url for the api for the backend that I built for this project
BASE_API_URL = "https://azramind.herokuapp.com"
# BASE_API_URL = "http://localhost:5000"


print("\nWelcome to Azramind! A game where you must guess the code to win. Do you have what it takes?\n\n")
q = False
while q is False:

    # number of tries a player gets to guess the code.

    command = input(
        '''Please enter a command:
    1 play the game
    2 rules of the game
    3 view past scores
    q to quit game at any time
            ''')

    # lowercase + remove white spaces
    command = command.lower().strip()

    # number of attempts the user gets
    limit = 10

    # number of digits to guess
    difficulty = 4

    if command == "1":
        print(
            """\nSo, you want to try your luck? First, you must tell me who you are. \n""")

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
                        print('\nyour username must be at least 3 characters long\n')
                    else:
                        response = requests.post(
                            username_url, data=username_obj).json()

                if command == "b":

                    response = requests.get(
                        username_url, data=username_obj).json()

            if response:
                if 'username' in response:
                    user_obj = response
                    print(f"Hello, {response['username']}")
                if 'message' in response:
                    print(response['message'])

        # URL to access the random number generator API
        INT_URL = "https://www.random.org/integers/"

        # INT_URL parameters
        INT_URL_PARAMS = {
            'num': difficulty,  # num digits requested
            'min': 0,  # min int
            'max': 7,  # max int
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

        # this is
        score_obj = azramind(code_list, limit, difficulty)

        score_obj["user_id"] = user_obj["id"]
        score_url = f"{BASE_API_URL}/score"

        # posting the score to the scores table
        response = requests.post(score_url, data=score_obj).json()

    elif command == "2":
        game_rules(limit, difficulty)

    elif command == "3":
        username = input(
            "Please enter your username to view past scores: ")

        # quit if user enters q or quit
        quit_function(username)

        GET_SCORES_URL = f"{BASE_API_URL}/{username}/scores"

        response = requests.get(url=GET_SCORES_URL).json()

        if response:
            if 'message' in response:
                print(response)
            elif 'scores' in response:
                for score in response['scores']:
                    print({
                        "date and time": score["date_time"],
                        "guesses": score["num_tries"],
                        "digits guessed": score["difficulty"]
                    })
            else:
                print('something went wrong, we had trouble retrieving your scores')

    elif command in {"q", "quit"}:
        print("thank you for playing, good bye")
        q = True

    elif command not in {"1", "2", "3", "q"}:
        print("\nInvalid input. Possible command values are 1, 2, 3, or q. Please try again.\n")
