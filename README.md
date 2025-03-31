Hangman Game
A fun implementation of the classic Hangman game using Python's pygame library. In this game, you try to guess the word by selecting letters one at a time. If you make too many incorrect guesses, "Bro" dies!

Features
A simple and intuitive user interface with clickable letter buttons.

Displays an image of a hangman that progressively updates as incorrect guesses are made.

Keeps track of wins and losses, showing the final results after each game.

Fun and engaging game mechanics where you can save "Bro" from dying or let him perish based on your guesses!

Requirements
Python 3.x

Visual Code Studios

pygame library

You can install pygame by running:

pip install pygame in terminal 

How to Play
Start the game from the menu by pressing Enter.

Guess the letters of the word by clicking them with the mouse or pressing the corresponding key on your keyboard.

If you guess a letter correctly, it will appear in the word.

If you make 6 incorrect guesses, "Bro" will die, and you lose the game.

If you guess all the letters correctly, you save "Bro" and win the game!

Instructions
Play: Press Enter from the menu to start the game.

Quit: Press Esc from the menu to quit the game.

Guess: Click on the letters or type them using your keyboard.

Files
images/hangman0.png to images/hangman6.png: Images of the hangman, displayed progressively as incorrect guesses are made.

Code Walkthrough
Initialization:

The game window is initialized with a resolution of 1480x720 pixels.

The letter buttons are placed on the screen, and their positions are calculated dynamically.

Word choices are stored in a predefined list, and one word is selected at random at the start of each game.

Main Gameplay Loop:

The game runs in a loop, checking for events such as mouse clicks or key presses.

When a letter is clicked or typed, the game checks if it's part of the word and updates the hangman image and guessed letters.

The game ends when either the word is guessed correctly or the hangman reaches 6 wrong guesses.

Display Functions:

The draw() function updates the game window with the current word, the hangman status, and the available letters.

The display_message() function shows a message after a game ends (win or loss).

The show_menu() function displays the menu with stats and options to play or quit.

Game States:

Wins and Losses are tracked and displayed on the menu screen.

The game is reset after each round, with new words chosen randomly from the word list.

pygame library

Hangman image assets

Enjoy the game, and don't let Bro die!
