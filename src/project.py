import os
import random
import time

import turtle
turtle.speed(0) #speed of animation
turtle.bgcolor("black")
#Change window title
turtle.title("Dog-Fight")
#Change the background image
turtle.bgpic("Space bk.gif")
turtle.ht() #hides default turtle
turtle.setundobuffer(1) # limits the amount of memory the turtle module uses
turtle.tracer(0) #changes speed of animation


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

        #Boundary detection (collision)
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)


    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)
    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0,360))

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 8
        self.setheading(random.randint(0,360))

    def move(self):
        self.fd(self.speed)

        #Boundary detection (collision)
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000) 

    def fire(self):
        if self.status == "ready":
            #Player missile sound (UPDATE LATER)
            #os.system("afplay laser.mp3&")
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        
        if self.status == "ready":
            self.goto(-1000, 1000) 

        if self.status == "firing":
            self.fd(self.speed)

        #Border check
        if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"

class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000, -1000)
        self.frame = 0

    def explode(self,starx, starty):
        self.goto(starx, starty)
        self.setheading(random.randint(0,360))
        self.frame = 1
    
    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1

        if self.frame > 10:
            self.frame = 0
            self.goto(-1000, -1000)
        
#keeps game information
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.Bpen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        #Draw border
        self.pen.speed(0) #anim speed
        self.pen.color("white")
        self.pen.pensize(3)

        self.Bpen.speed(0) #anim speed
        self.Bpen.color("white")
        self.Bpen.pensize(3)
        self.Bpen.penup()
        self.Bpen.goto(-300, 300)
        self.Bpen.pendown()
        for side in range(4):
            self.Bpen.fd(600)
            self.Bpen.rt(90)
        self.Bpen.penup()
        self.Bpen.ht()
        self.Bpen.pendown()
    
    def show_status(self):
        self.pen.clear()
        msg = "Score: %s" %(self.score)
        liv = "Lives: %s" %(self.lives)
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font =("Courier New", 16, "normal"))
        self.pen.penup()
        self.pen.goto(-150, 310)
        self.pen.write(liv, font = ("Courier New", 16, "normal"))

    def __str__(self):
        return f"Score: {self.score}"
    
    

#Create Game Object
game = Game()
print(game)

#Draw the boarder
game.draw_border()

#show the game status
game.show_status()


#Create sprites
player = Player("triangle", "white", 0, 0)
#enemy = Enemy("circle", "red", -100, 0)
missile = Missile("triangle", "yellow", 0, 0)
#ally = Ally("square", "blue", 100,0)

enemies = []
for i in range(6):
    enemies.append(Enemy("circle", "red", -100, 0))

allies = []
for i in range(6):
    allies.append(Ally("square", "blue", 100,0))

particles = []
for i in range(20):
    particles.append(Particle("circle", "orange", 0,0))

#Keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen() #asks turtle to watch for key pressed events

def main():
    #Main game loop
    while True:
        turtle.update()
        time.sleep(0.03)

        player.move()
        missile.move()

        for enemy in enemies:
            enemy.move()
        
            #Check for collision with the player
            if player.is_collision(enemy):
                # Play explosion sound(UPDATE LATER)
                #os.system("afplay explosion.mp3&")
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                enemy.goto(x, y)
                game.lives -= 1
                game.score += 50
                game.show_status()


            #Check for collision between missile and the enemy
            if missile.is_collision(enemy):
                # Play explosion sound(UPDATE LATER)
                #os.system("afplay explosion.mp3&")
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                enemy.goto(x, y)
                missile.status = "ready"
                #Increase the score
                game.score += 100
                game.show_status()
                #Do the explosion
                for particle in particles:
                    particle.explode(missile.xcor(), missile.ycor())

        for ally in allies:
            ally.move()

            #Check for collision between missile and the ally
            if missile.is_collision(ally):
                # Play explosion sound(UPDATE LATER)
                #os.system("afplay explosion.mp3&")
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                ally.goto(x, y)
                missile.status = "ready"
                #Decrease the score
                game.score -= 50
                game.show_status()

        for particle in particles:
            particle.move()
            
if __name__ == "__main__":
    main()



delay = input("Press enter to finish. >")
