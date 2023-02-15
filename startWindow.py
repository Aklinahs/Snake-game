from turtle import Turtle


class StartWindow(Turtle):
    def __init__(self):
        self.play = "n"

    def ask_start(self):
        play = self.textinput("Start the game", "Press 'Y' to start the game")
        if play.lower() == "y":
            print("Play")

