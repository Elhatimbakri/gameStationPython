from tkinter import *
import games

def main():

    root0 = Tk()

    # Les proportion de la fenetre
    root0.geometry("400x400")

    # Le titre de la fenetre
    root0.title("Game Station")

    # Les textes
    Label(root0,
          text="Welcome to Game Station",
          font="normal 20 bold",
          fg="black").pack(pady=20)

    Label(root0,
          text="Select a game",
          font="normal 20 bold",
          fg="black").pack(pady=20)

    # Les Bouttons
    Button(root0, text="Rock Paper Scissors",
           font=10, fg="black",
           bg="white", command=games.game1).pack(pady=20)

    Button(root0, text="Snake",
           font=10, fg="black",
           bg="white", command=games.game2).pack(pady=20)

    Button(root0, text="Guess The Price",
           font=10, fg="black",
           bg="white", command=games.game3).pack(pady=20)



    # Execution
    root0.mainloop()


main()