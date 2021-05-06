from turtle import Turtle
# Create the Scoreboard class, inherit turtle graphics
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        # read high score or create it on first run. Save as a text file.
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.shape()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
# eat function, add 1 to score and update the scoreboard
    def eat(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

# update scoreboard function with current score and high score
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Scoreboard = {self.score} High Score: {self.high_score}", True, align="center")

# when game ends reset, update high score if needed, reset user score to 0
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

