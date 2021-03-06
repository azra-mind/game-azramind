import requests
from requests.exceptions import HTTPError
import sys

from azramind_func import azramind
from util import game_rules, get_code_list, quit_function, post_and_return_username, validate_guess


# url for the api for the backend that I built for this project
BASE_API_URL = "https://azramind.herokuapp.com"
# BASE_API_URL = "http://localhost:5000"


print("\nWelcome to Azramind! A game where you must guess the code to win. Do you have what it takes?\n\n")
q = False
while q is False:

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

        # this loop runs until we have a user_obj for saving scores after game over
        while user_obj is None:

            # function inside util.py. Post the username to the db an return a user json object
            user_obj = post_and_return_username(BASE_API_URL)

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

        # this is the main function for the game logic. It returns a game score
        score_obj = azramind(code_list, limit=10, difficulty=4)

        # creating the score json object and urls
        score_obj["user_id"] = user_obj["id"]
        score_url = f"{BASE_API_URL}/score"

        # posting the score to the scores table

        try:
            response = requests.post(score_url, data=score_obj)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(
                f"something went wrong trying to save your game score", err, "\n")

    elif command == "2":
        game_rules(limit, difficulty)

    elif command == "3":
        username = input("Please enter your username to view past scores: ")

        # quit if user enters q or quit
        quit_function(username)

        get_scores_url = f"{BASE_API_URL}/{username}/scores"

        try:
            response = requests.get(url=get_scores_url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            if response.status_code == 404:
                print(response.json(), response.status_code)
            else:
                print(
                    f"something went wrong trying to retrieve your game score", err, "\n")

        if response:
            scores = response.json()
            for score in scores['scores']:
                print({
                    "date and time": score["date_time"],
                    "guesses": score["num_tries"],
                    "digits in code": score["difficulty"]
                })

    elif command in {"q", "quit"}:
        print("thank you for playing, good bye")
        q = True

    elif command not in {"1", "2", "3", "q"}:
        print("\nInvalid input. Possible command values are 1, 2, 3, or q. Please try again.\n")
