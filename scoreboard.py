from turtle import Turtle



class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.write(f'Score: {self.score}      Highscore: {self.highscore}', move= False,align="center", font=("Courier", 15, "normal"))
        self.hideturtle()
    
    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}      Highscore: {self.highscore}', move= False,align="center", font=("Courier", 15, "normal"))
    
    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        
        self.score = 0
        
        self.update_score()