import os
import random

import turtle
#turtle.fd(0)
turtle.speed(0) #speed of animation
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1) # limits the amount of memory the turtle module uses
turtle.tracer(1) #changes speed of animation

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0) #speed of animation 
        self.penup()
        self.color(color)
        #self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

#Create sprites
player = Sprite("triangle", "white", 0, 0)










delay = input("Press enter to finish. >")
