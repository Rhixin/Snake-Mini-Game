import turtle
from turtle import Turtle,Screen
import time
import winsound
from turtle import addshape

addshape(shape=None,name="snake_skin.gif")
addshape(shape=None,name="snake_head.gif")



class Snake:
    def __init__(self,bodies):
        self.bodies = []
        
        x_axis = 0
        for i in range(bodies):
            t = Turtle()
            t.speed("fastest")
            t.penup()
            t.shape("snake_skin.gif")
            t.color("white")
            t.setposition(x_axis,0)
            x_axis-=20
            
            self.bodies.append(t)
            
        self.head = self.bodies[0]
        self.head.shape("snake_head.gif")

        
    def move(self):    
        for i in range(len(self.bodies) - 1, 0 ,-1):
            self.bodies[i].showturtle()
            self.bodies[i].goto(self.bodies[i-1].pos())
                    
        self.head.forward(20) 
    
    def move_up(self):
        if self.head.heading() != 270:    
            self.head.setheading(90)
            winsound.PlaySound("eat.wav", winsound.SND_ASYNC) 
    
    def move_right(self):
        if self.head.heading() != 180:    
            self.head.setheading(0)
            winsound.PlaySound("eat.wav", winsound.SND_ASYNC) 
        
    def move_left(self):
        if self.head.heading() != 0: 
            self.head.setheading(180)
            winsound.PlaySound("eat.wav", winsound.SND_ASYNC) 
        
    def move_down(self):
        if self.head.heading() != 90: 
            self.head.setheading(270)
            winsound.PlaySound("eat.wav", winsound.SND_ASYNC) 
    
    def add_body(self):
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.shape("snake_skin.gif")
        t.color("white")
        self.bodies.append(t)
        
    def check_gameover(self):
        if self.head.xcor() < -290 or self.head.xcor() > 290 or self.head.ycor() < -290 or self.head.ycor() > 290:
            return True
        
        return False
    
    def reset(self,bodies):
        for i in self.bodies:
            i.hideturtle()
            
        self.bodies.clear()

        x_axis = 0
        for i in range(bodies):
            t = Turtle()
            t.speed("fastest")
            t.penup()
            t.shape("snake_skin.gif")
            t.color("white")
            t.setposition(x_axis,0)
            x_axis-=20
            
            self.bodies.append(t)
            
        self.head = self.bodies[0]
        self.head.shape("snake_head.gif")
        