Azramind is a command-line game modeled after the popular board game Mastermind. It is written in Python with a backend and RESTful API written in Python/Flask, which can be found here in a separate repository. [Link to Azramind Backend](https://github.com/azra-mind/be-azramind)

I had a lot of fun building this game! I hope you enjoy playing it.

### SOFTWARE REQUIREMENTS:

- [Python 3.7.4+](https://www.python.org/download/)
- [PIP package manager](https://pip.pypa.io/en/stable/installing/) (automatically included in Python 3 >=3.4)
- requests library
- an internet connection

### INSTRUCTIONS TO RUN THE GAME PROGRAM:

- Open your terminal.
- **git clone https://github.com/azra-mind/game-azramind.git** to clone the master branch of the repo.
- **cd game-azramind** to cd into the root directory of the repo.
- **pip3 install -r requirements.txt** to Install the requirements.
- Now you're ready to play the game!
- **python3 program_logic.py** to start the game program.
- Game play instructions are included in the program.

### CODE STRUCTURE:

- This repo provides the user interface for playing the game.
- To view the api written in python/flask that saves the scores, please visit the backend repository [here](https://github.com/azra-mind/be-azramind)
- There are 3 main files that form the codebase for this program.

#### program_logic.py

- contains the main logic for the game program. This is the file you run in your terminal to start the game.
- When you run the file, you will see a main menu of 3 choice:
  1 play the game
  2 rules of the game
  3 view past scores
  q to quit game at any time
- Upon selecting 1 play the game, you will be prompted to enter a new or existing username.
- Then you will automatically drop into the game.
- After finishing the game, your score will be saved to the database and you will return to the main menu.
- Upon selecting 3 view past scores You can observe your past scores whuch are saved in a Postgres DB.

#### azramind_func.py

- contains the the function `azramind` which has the logic for the game itself.

#### util.py

- contains helper functions utilized in `program_logic.py` and `azramind_func.py`.

### GAME EXTENSIONS:

- I built a backend in Python/Flask to include the ability to save and retrieve past scores.
- I added the ability to view the rules of the game.
- I also made the number of guesses allowed and the number of digits to guess configurable in the code, but not by the player (yet). I hope to continue building on this project to - enable the game player to configure those options as well.
- Lastly, I added a little commentary to make the game a bit more lively.

### HOW I APPROACHED BUILDING THIS GAME:

I built this game in Python because it is my favorite language to code in out of the ones I've tried thus far (Ruby, Javascript, Python). In addition, I really enjoy building APIs and thought this would be a great way for me to learn how to do so using Python.

While I knew how to bulid APIs in Node.js, and knew enough Python to solve CS coding challenge style problems in Algorithms, Datastructures, I had never built a backend utilizing Object Oriented Programming, nor had I ever built a REST API from scratch using a Python framework such as Flask or Django prior to building this project. I decided to use this challenge as a forcing function to teach myself something that I'd been meaning to learn anyway: How to build a backend and RESTful API in Flask. I chose Flask over Django because it is a more light-weight framework that I could learn and deploy quickly, yet it scales well since companies like Netflix, Reddit, and Lyft use it.


### WHAT'S NEXT:

I plan to continue working on this project to build upon my knowledge.

#### Game Play Interface

- Add the ability for the player to configure difficult levels
- better error handling for no internet connection
- Build out a frontend in React.js
- ability to play in offline mode

#### Backend

- Add unit tests to the backend repo
- Add user authorization (login/password)
- Add a lookup table for difficulty levels (easy/medium/hard)
