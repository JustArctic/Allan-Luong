import pygame
import math
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 1480, 720
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("images/hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = ["IPAD", "REPLIT", "PYTHON", "PYGAME", "AUDIBLE", "FIRE", "WORDLE", "PAYTOWIN", "TAXEVASION", "ITSATRAP""APPLE", "BRIDGE", "CANDLE", "DRAGON", "ECHO", "FEATHER", "GALAXY", "HORIZON", "IVORY", "JUPITER", "KITE", "LABYRINTH", "MEADOW", "NEBULA", "ORBIT", "PRISM", "QUARTZ", "RAVEN", "SAPPHIRE", "TWILIGHT", "UMBRELLA", "VOYAGER", "WONDER", "XENON", "YONDER", "ZENITH","WINNER"]
word = random.choice(words)
guessed = []

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# statistics
wins = 0
losses = 0

def draw():
    win.fill(WHITE)
    
    # draw title
    text = TITLE_FONT.render("DON'T LET BRO DIE!", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 18))
    
    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (350, 200))
    
    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
    
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def show_menu():
    global wins, losses
    win.fill(WHITE)
    
    title_text = TITLE_FONT.render("HANGMAN GAME", 1, BLACK)
    win.blit(title_text, (WIDTH/2 - title_text.get_width()/2, 100))
    
    stats_text = WORD_FONT.render(f"Wins: {wins}  Losses: {losses}", 1, BLACK)
    win.blit(stats_text, (WIDTH/2 - stats_text.get_width()/2, 200))
    
    play_text = WORD_FONT.render("Press ENTER to Play", 1, BLACK)
    quit_text = WORD_FONT.render("Press ESC to Quit", 1, BLACK)
    
    win.blit(play_text, (WIDTH/2 - play_text.get_width()/2, 300))
    win.blit(quit_text, (WIDTH/2 - quit_text.get_width()/2, 400))
    
    pygame.display.update()

def main():
    global hangman_status, word, guessed, wins, losses

    # Reset game variables
    hangman_status = 0
    word = random.choice(words)
    guessed = []

    # Reset letters visibility
    for letter in letters:
        letter[3] = True  # Make all letters visible again

    FPS = 60
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
            
            # Key press handling
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key).upper()  # Get the key and convert to uppercase
                if key.isalpha() and key not in guessed:  # Ensure it's a valid letter and not already guessed
                    guessed.append(key)
                    for letter in letters:
                        if letter[2] == key:
                            letter[3] = False  # Make the letter button disappear when guessed
                    if key not in word:
                        hangman_status += 1
        
        draw()
        
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            display_message("You WON!")
            wins += 1
            break
        
        if hangman_status == 6:
            display_message("You LOST!")
            losses += 1
            break

def game_loop():
    running = True
    while running:
        show_menu()  # Show menu screen first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Start the game
                    main()
                if event.key == pygame.K_ESCAPE:  # Quit the game
                    running = False
    pygame.quit()

game_loop()
    
win.blit(images[hangman_status], (150, 100))
pygame.display.update()

win.blit(images[hangman_status], (150, 100))
pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def show_menu():
    global wins, losses
    win.fill(WHITE)
    
    title_text = TITLE_FONT.render("HANGMAN GAME", 1, BLACK)
    win.blit(title_text, (WIDTH/2 - title_text.get_width()/2, 100))
    
    stats_text = WORD_FONT.render(f"Wins: {wins}  Losses: {losses}", 1, BLACK)
    win.blit(stats_text, (WIDTH/2 - stats_text.get_width()/2, 200))
    
    play_text = WORD_FONT.render("Press ENTER to Play", 1, BLACK)
    quit_text = WORD_FONT.render("Press ESC to Quit", 1, BLACK)
    
    win.blit(play_text, (WIDTH/2 - play_text.get_width()/2, 300))
    win.blit(quit_text, (WIDTH/2 - quit_text.get_width()/2, 400))
    
    pygame.display.update()

def main():
    global hangman_status, word, guessed, wins, losses

    # Reset game variables
    hangman_status = 0
    word = random.choice(words)
    guessed = []

    # Reset letters visibility
    for letter in letters:
        letter[3] = True  # Make all letters visible again

    FPS = 60
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
            
            # Key press handling
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key).upper()  # Get the key and convert to uppercase
                if key.isalpha() and key not in guessed:  # Ensure it's a valid letter and not already guessed
                    guessed.append(key)
                    for letter in letters:
                        if letter[2] == key:
                            letter[3] = False  # Make the letter button disappear when guessed
                    if key not in word:
                        hangman_status += 1
        
        draw()
        
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            display_message("You WON!")
            wins += 1
            break
        
        if hangman_status == 6:
            display_message("You LOST!")
            losses += 1
            break

def game_loop():
    running = True
    while running:
        show_menu()  # Show menu screen first
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Start the game
                    main()
                if event.key == pygame.K_ESCAPE:  # Quit the game
                    running = False
    pygame.quit()

game_loop()

