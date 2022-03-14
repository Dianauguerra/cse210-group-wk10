# Cycle
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

# Rules
There are 2 players. Players can move up, down, left and right: Player one moves using the W, S, A and D keys. Player two moves using the I, K, J and L keys. Each player's trail grows as they move. Players try to maneuver so the opponent collides with their trail. If a player collides with their opponent's trail the GAME IS OVER.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 cycle
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    ( project root folder )
+-- cycle               ( source code for game )
  +-- game              ( game specific classes )
  +-- __main__.py       ( program entry point )
+-- README.md           ( general info )
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Miguel López ( lop18028@byui.edu ) : Coded __main__.py, casting classes( Actor, Cast, Player_one_score, Player_one, Player_two and Player_two_scores classes ) and updated Control_actors_action, Draw_actors_action and Handle_collisions_action from scripting classes. Oversaw the review of the project as a whole.
* Ryan Weinheimer ( ryanweinheimer@gmail.com ) : Coded Action, Script, Move_actors_action classes and Video_service class from services classes. Participated by giving ideas to solve problems encountered.
* Diana Guerra ( diana.1609@hotmail.com ) : Created the team repository, created README file. Coded constants.py file, directing classes( Director class ), Keyboard_service class from services classes and participated by giving ideas to solve problems encountered.
* Eduardo Mosquera Galarza ( mos21008@byui.edu ) : Coded Color class.
* Chioneso Chatayika( cchatayika@outlook.com ) : Coded Point class.

