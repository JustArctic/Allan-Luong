START

    INITIALIZE Pygame library
    SET up game display (WIDTH, HEIGHT)
    CREATE variables for game settings (letters, word list, images, etc.)
    LOAD fonts and images (for hangman status)
    SET initial game variables (hangman_status, wins, losses, etc.)
    SET up the starting word randomly from the word list
    
    FUNCTION draw():
        CLEAR the screen
        DISPLAY the title ("DON'T LET BRO DIE!")
        DISPLAY the word, replacing unguessed letters with underscores ("_")
        DISPLAY available letters as buttons
        DISPLAY hangman image based on current hangman status
        UPDATE the screen
        
    FUNCTION display_message(message):
        DISPLAY a message (win/lose condition)
        WAIT for a few seconds
        CLEAR the screen
        
    FUNCTION show_menu():
        DISPLAY the game menu (title, wins, losses, play option, quit option)
        WAIT for user input (press ENTER to play, ESC to quit)
        
    FUNCTION main_game():
        RESET game variables (hangman_status, guessed letters, new word)
        RESET letter visibility for the alphabet buttons
        
        WHILE the game is running:
            HANDLE user events (mouse click or keyboard press)
            
            IF the user clicks on a letter or presses a key:
                MARK that letter as guessed
                IF the letter is in the word:
                    CONTINUE to check for win condition
                ELSE:
                    UPDATE hangman status (increment failure count)
            
            CHECK if all letters are guessed (win condition):
                CALL display_message("You Saved Bro!")
                INCREMENT win count
                BREAK out of the game loop
            
            CHECK if hangman_status reaches 6 (lose condition):
                CALL display_message("You Let Bro Die! The word was: " + word)
                INCREMENT loss count
                BREAK out of the game loop

    FUNCTION game_loop():
        WHILE the game is running:
            CALL show_menu() to display the game menu
            HANDLE user input (ENTER to start game, ESC to quit)
            
            IF the user presses ENTER:
                CALL main_game() to start a new game
            IF the user presses ESC:
                EXIT the game
        
    START the game loop

END
