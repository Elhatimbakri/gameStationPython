import random
from tkinter import *
import tkinter as tk
import pygame


# Game 1 : RockPaperScissors
def game1():
    root = Tk()

    # geometry
    root.geometry("300x300")

    # title
    root.title("Rock Paper Scissor")

    # Computer Value
    computer_value = {
        "0": "Rock",
        "1": "Paper",
        "2": "Scissor"
    }

    # Reset The Game
    def reset_game():
        b1["state"] = "active"
        b2["state"] = "active"
        b3["state"] = "active"
        l1.config(text="Player              ")
        l3.config(text="Computer")
        l4.config(text="")

    # Disable the Button
    def button_disable():
        b1["state"] = "disable"
        b2["state"] = "disable"
        b3["state"] = "disable"

    # Match Rules
    # Rock < Paper
    # Rock > Scissors
    # Scissors > Paper

    # If player selected rock
    def isrock():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Match Draw"
        elif c_v == "Scissor":
            match_result = "Player Win"
        else:
            match_result = "Computer Win"
        l4.config(text=match_result)
        l1.config(text="Rock            ")
        l3.config(text=c_v)
        button_disable()

    # If player selected paper
    def ispaper():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Paper":
            match_result = "Match Draw"
        elif c_v == "Scissor":
            match_result = "Computer Win"
        else:
            match_result = "Player Win"
        l4.config(text=match_result)
        l1.config(text="Paper           ")
        l3.config(text=c_v)
        button_disable()

    # If player selected scissor
    def isscissor():
        c_v = computer_value[str(random.randint(0, 2))]
        if c_v == "Rock":
            match_result = "Computer Win"
        elif c_v == "Scissor":
            match_result = "Match Draw"
        else:
            match_result = "Player Win"
        l4.config(text=match_result)
        l1.config(text="Scissor         ")
        l3.config(text=c_v)
        button_disable()

    # Add Labels, Frames and Button
    Label(root,
          text="Rock Paper Scissor",
          font="normal 20 bold",
          fg="blue").pack(pady=20)

    frame = Frame(root)
    frame.pack()

    l1 = Label(frame,
               text="Player              ",
               font=10)

    l2 = Label(frame,
               text="VS             ",
               font="normal 10 bold")

    l3 = Label(frame, text="Computer", font=10)

    l1.pack(side=LEFT)
    l2.pack(side=LEFT)
    l3.pack()

    l4 = Label(root,
               text="",
               font="normal 20 bold",
               bg="white",
               width=15,
               borderwidth=2,
               relief="solid")
    l4.pack(pady=20)

    frame1 = Frame(root)
    frame1.pack()

    b1 = Button(frame1, text="Rock",
                font=10, width=7,
                command=isrock)

    b2 = Button(frame1, text="Paper ",
                font=10, width=7,
                command=ispaper)

    b3 = Button(frame1, text="Scissor",
                font=10, width=7,
                command=isscissor)

    b1.pack(side=LEFT, padx=10)
    b2.pack(side=LEFT, padx=10)
    b3.pack(padx=10)

    Button(root, text="Reset Game",
           font=10, fg="green",
           bg="black", command=reset_game).pack(pady=20)

    # Execute Tkinter
    root.mainloop()


# Game 2 : Snake
def game2():
    pygame.init()

    # couleurs

    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    # Les proportions de la fenetre
    dis_width = 720
    dis_height = 480

    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game')

    clock = pygame.time.Clock()

    # La vitesse du jeu
    snake_block = 10
    snake_speed = 15

    # Style du texte
    font_style = pygame.font.SysFont("Times New Roman", 25)
    score_font = pygame.font.SysFont("Times New Roman", 35)

    # Calcul du score
    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, black)
        dis.blit(value, [0, 0])

    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])

    def gameLoop():
        game_over = False
        game_close = False

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_List = []
        Length_of_snake = 1

        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close == True:
                dis.fill(white)
                message("You Lost! Press P-Play Again or Q-Quit", black)
                Your_score(Length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_p:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(white)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()
        quit()

    gameLoop()


# Game 3 : Guess the price
def game3():
    # Create a new window
    window = tk.Tk()

    # Set the dimensions of the created window
    window.geometry("600x400")

    window.resizable(width=False, height=False)

    # Set Window Title
    window.title('Number Guessing Game')


    TARGET = random.randint(0, 1000)
    RETRIES = 0

    def update_result(text):
        result.configure(text=text)

    # Create a new game
    def new_game():
        guess_button.config(state='normal')
        global TARGET, RETRIES
        TARGET = random.randint(0, 1000)
        RETRIES = 0
        update_result(text="Guess a number between\n 1 and 1000")

    # Continue the ongoing game or end it
    def play_game():
        global RETRIES

        choice = int(number_form.get())

        if choice != TARGET:
            RETRIES += 1

            result = "Wrong Guess!! Try Again"
            if TARGET < choice:
                hint = "Low"
            else:
                hint = "High"
            result += "\n\nHINT :\n" + hint

        else:
            result = "You guessed the correct number after {} retries".format(RETRIES)
            guess_button.configure(state='disabled')
            result += "\n" + "Click on Play to start a new game"

        update_result(result)

    # Heading of our game
    title = tk.Label(window, text="Guessing Game", font=("Arial", 24), fg="red")

    # Result and hints of our game
    result = tk.Label(window, text="Click on Play to start a new game", font=("Arial", 12, "normal", "italic"),
                      fg="Black", justify=tk.LEFT)

    # Play Button
    play_button = tk.Button(window, text="Play Game", font=("Arial", 14, "bold"), fg="Black", bg="#29c70a",
                            command=new_game)

    # Guess Button
    guess_button = tk.Button(window, text="Guess", font=("Arial", 13), state='disabled', fg="#13d675", bg="Black",
                             command=play_game)

    # Exit Button
    exit_button = tk.Button(window, text="Exit Game", font=("Arial", 14), fg="White", bg="#b82741", command=exit)

    # Entry Fields
    guessed_number = tk.StringVar()
    number_form = tk.Entry(window, font=("Arial", 11), textvariable=guessed_number)

    # Place the labels

    title.place(x=170, y=50)
    result.place(x=180, y=210)

    # Place the buttons
    exit_button.place(x=300, y=320)
    guess_button.place(x=350, y=147)
    play_button.place(x=170, y=320)

    # Place the entry field
    number_form.place(x=180, y=150)

    # Start the window
    window.mainloop()
