import requests
from requests.exceptions import HTTPError
import sys


username = "anita"
BASE_URL = "http://localhost:5000"
# BASE_URL = "https://azramind.herokuapp.com"


print("\nWelcome to Azramind! A game where you must guess the code to win. Do you have what it takes?\n\n")
q = False
while q is False:
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

        print("""\n\nSo, you'd like to try your luck? First, you must tell me who you are \n\n""")

        command = input(
            '''Enter a command:
        a enter an existing username
        b create a new username
            ''')

        username = input("Enter username: ")
        username_url = f"{BASE_URL}/register"

        command = command.lower().strip()
        if command == "a":
            '

            print("you selected a")

        if command == "b":
            print("you selected b")

        x = requests.post(url, data=myobj)

    elif command == "2":
        print("\nrules are the rules!!\n\n")

    elif command == "3":

        username = input("Please enter your username to view past scores: ")
        GET_SCORES_URL = f"{BASE_URL}/{username}/scores"
        response = requests.get(url=GET_SCORES_URL).json()

        if response['message']:
            print(response)
        else:
            print(response['scores'])

    elif command not in {"1", "2", "3", "q"}:
        print("\nInvalid input. Possible command values are 1, 2, 3, or q. Please try again.\n")

    elif command.lower() == "q":
        print("thank you for playing, good bye")
        q = True
