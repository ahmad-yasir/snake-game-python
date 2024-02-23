from turtle import *
import random
import time


#Screen
win = Screen()
win.bgcolor("gold")
win.title("Snake Game")
win.setup(600,600)
win.tracer(0)

#Snake Head
head = Turtle()
head.shape("square")
head.color("navy")
head.penup()
head.speed(0)
head.direction = "stop"

#Snake Food
food = Turtle()
food.shape("circle")
food.color("red")
food.shapesize(0.6,0.6)
food.penup()
food.speed(0)
food.direction="stop"
food.goto(0,50)

#pen
pen = Turtle()
pen.color("black")
pen.hideturtle()
pen.penup()
pen.speed(0)
pen.direction="stop"
pen.goto(0,270)
pen.write("Score: 0    High Score: 0",align="center",font=("Calibri",20,"bold"))

#Move function
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"

win.listen()
win.onkey(go_up,"w")
win.onkey(go_down,"s")
win.onkey(go_right,"d")
win.onkey(go_left,"a")

segment = []
score=0
high_score=0

target = 5 #You can set any target to be a snake master

#MainLoop
while True:
    win.update()

    #Check border hitting
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.5)
        pen.clear()
        pen.goto(0,0)
        pen.write("Game Over!",align="center",font=("Calibri",20,"bold"))
        time.sleep(1)
        pen.clear()
        pen.write("Restarting...",align="center",font=("Calibri",20,"bold"))
        time.sleep(0.5)
        pen.clear()
        pen.goto(0,270)
        score=0
        pen.write("Score: {}    High Score: {}".format(score,high_score),align="center",font=("Calibri",20,"bold"))
        head.goto(0,0)
        head.direction = "stop"

        for i in segment:
            i.goto(1000,1000)

        segment.clear()


    #Food Eating
    if head.distance(food) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        food.goto(x,y)

        score+=1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score,high_score),align="center",font=("Calibri",20,"bold"))



        ns = Turtle()
        ns.shape("square")
        ns.color("grey")
        ns.penup()
        ns.speed(0)
        ns.direction="stop"
        segment.append(ns)

    for i in range(len(segment)-1, 0,-1):
        x = segment[i-1].xcor()
        y = segment[i-1].ycor()
        segment[i].goto(x,y)

    if len(segment)>0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)

    move()

    for i in segment:
        if i.distance(head)<20:
            time.sleep(0.5)
            pen.clear()
            pen.goto(0,0)
            pen.write("Game Over!",align="center",font=("Calibri",20,"bold"))
            time.sleep(1)
            pen.clear()
            pen.write("Restarting...",align="center",font=("Calibri",20,"bold"))
            time.sleep(0.5)
            pen.clear()
            pen.goto(0,270)
            score=0
            pen.write("Score: {}    High Score: {}".format(score,high_score),align="center",font=("Calibri",20,"bold"))
            head.goto(0,0)
            head.direction = "stop"

            for i in segment:
                i.goto(1000,1000)

            segment.clear()
    if score==target:
        pen.clear()
        pen.goto(0,0)
        pen.write("Congrats! You are the snake master!",align="center",font=("Calibri",26,"bold"))
        break
    time.sleep(0.1)


