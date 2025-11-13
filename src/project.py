import os
import random

import turtle
turtle.speed(0) #speed of animation
turtle.bgcolor("black")
turtle.ht() #hides default turtle
turtle.setundobuffer(1) # limits the amount of memory the turtle module uses
turtle.tracer(1) #changes speed of animation

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0) #speed of animation 
        self.penup()
        self.color(color)
        self.goto(startx, starty)
        self.speed = 1

    #default movement func
    def move(self):
        self.fd(self.speed)

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3


#Create sprites
player = Player("triangle", "white", 0, 0)


#Main game loop
while True:
    player.move()










delay = input("Press enter to finish. >")
