from turtle import Turtle
import random


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.color("blue")
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.refresh()
        
    def refresh(self):
        random_x = random.randint(-280, 250)
        random_y = random.randint(-280, 250)
        self.penup()
        self.goto(random_x, random_y)
        