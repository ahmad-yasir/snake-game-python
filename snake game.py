import turtle
import time
import random

score = 0
high_score = 0

#set up the screen
win = turtle.Screen()
win.title("Yasir's Snake Game")
win.bgcolor("gold")
win.setup(600,600)
win.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.direction = "stop"


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

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

#Buttons to move
win.listen()
win.onkey(go_up,"w")
win.onkey(go_down, "s")
win.onkey(go_left,"a")
win.onkey(go_right, "d")


#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.7,0.7)
food.goto(0,50)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("purple")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0    High Score: 0", align="center", font=("Courier", 18, "bold"))

#Pen2
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.shape("square")
pen2.color("red")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,50)


segment = []

#Main game loop
while True:
    win.update()

    #Check for border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(.7)
        head.goto(0,0)
        head.direction = "stop"

        for i in segment:
            i.goto(1000,1000)

        segment.clear()
        
        pen2.write("Game Over", align='center', font=("Comic Sans MS", 24, "bold"))
        time.sleep(0.75)
        pen2.clear()
        pen2.write("Start Again", align='center', font=("Comic Sans MS", 24, "bold"))
        time.sleep(0.5)
        pen2.clear()
        
        score = 0
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "bold"))    

            

    if head.distance(food) < 15:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        food.goto(x,y)

        #add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white smoke")
        new_segment.penup()
        segment.append(new_segment)

        #Update the score
        score+=10

        if score>high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "bold"))    
    
    #move the end segment in reverse order
    for i in range(len(segment)-1, 0, -1):
        x = segment[i-1].xcor()
        y = segment[i-1].ycor()
        segment[i].goto(x,y)

    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x,y)

    move()
    
    #Check for body collision
    for i in segment:
        if i.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction = "stop"

            for i in segment:
                i.goto(1000,1000)

            segment.clear()

            pen2.write("Game Over", align='center', font=("Comic Sans MS", 24, "bold"))
            time.sleep(0.5)
            pen2.clear()
            pen2.write("Start Again", align='center', font=("Comic Sans MS", 24, "bold"))
            time.sleep(0.3)
            pen2.clear()

            score = 0
            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 16, "bold"))    


  
    time.sleep(0.10)


















    
