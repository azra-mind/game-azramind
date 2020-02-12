
To Play the game:

This is a command-line game written in Python with a backend and API written in Python/Flask

I taught myself how to build a backend in Python/Flask in 3 days to write this program in an Object Oriented Language. 

* Clone this repo onto your machine
* From the terminal, cd into the root directory of the repo
* The game is written in Python version 3.7.4 so you need to have Python 3 installed on your machine.
* You will also need to utilize the PIP package manager to install the requests library, which is included in Python 3.4 and up. 
* If you need to install PIP, you can do so here: https://pypi.org/project/pip/
* Once you have PIP, please run this command from the root folder of the project: pip3 install requests
* After you've installed the requests library. You are ready to play the game!
* Enter the following prompt to start playing the game: python3 game-logic.py


Known issues:
- App errors out if you put a non-integer. App also does not check if the code input is >4 digits
- App accepts non-alpha numeric characters as username


Known usability feedback:
- Difficulty level is confusing
- clean up the scores view a bit
- add date-time to past scores
- add the digits and locations guessed correctly with each turn so user doesn't have to scroll up as much
