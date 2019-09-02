import turtle
import time
import random
Delay= 0.1

#Score
score =0
high_score=0

#set up screen
wn = turtle.Screen()
wn.setup (height= 600, width = 600)
wn.bgcolor("black")
wn.title ("Snake Game by @ Jannatul (Evana)")
wn.tracer(0)


#Snake head

H = turtle.Turtle()
H.shape("square")
H.color ("#15CB45")
H.speed(0)
H.penup()
H.goto(0,0)
H.direction= "stop"  #question about Direction stop

#Snake food
F = turtle.Turtle()
F.shape("circle")
F.color ("red")
F.speed(0)
F.penup()
F.goto(0,100)

Segment= []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align="center",
          font= ("Courier", 24, "normal"))

#Function

def go_up():
    if H.direction != "down":
        H.direction = "up"
def go_down():
    if H.direction != "up":
        H.direction = "down"
def go_left():
    if H.direction != "right":
        H.direction ="left"
def go_right():
    if H.direction != "left":
        H.direction= "right"


def move_Snake():
    if H.direction == "up":
        y= H.ycor()
        H.sety(y +20)

    if H.direction =="down":
        y= H.ycor()
        H.sety (y -20)

    if H.direction== "left":
        x= H.xcor()
        H.setx (x-20)

    if H.direction =="right":
        x = H.xcor()
        H.setx (x +20)

#Keyboard pressing

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_down, "Down")

# Main game loop
while True:
    wn.update()

    #check for collision

    if H.xcor() >290 or H.xcor()<-290 or H.ycor()>290 or H.ycor()<-290:
        time.sleep(1)
        H.goto(0,0)
        H.direction= "stop"

        #hide the sagments--- review
        for s in Segment:
            s.goto(1000,1000)
        Segment.clear()

        #reset score
        score=0

        #reset delay
        Delay -= 0.001
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))
    if H.distance(F) <20:  #need review
        x= random.randint(-290,290)
        y= random.randint(-290,290)
        F.goto(x,y)

        N_segment= turtle.Turtle()
        N_segment.color ("yellow")
        N_segment.shape("square")
        N_segment.goto (0,0)
        N_segment.penup()
        Segment.append(N_segment)

        #Speed up sagment
        Delay -= 0.001

        #increare score
        score +=10
        if score>high_score:
            high_score= score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),
                  align="center", font=("Courier", 24, "normal"))
   #moving the segment ----- Need review
    for index in range (len(Segment) -1,0,-1):
        x= Segment[index-1].xcor()
        y= Segment[index-1].ycor()
        Segment[index].goto(x,y)
    #move the 0 segemnt to the head

    if len(Segment)>0:
        x= H.xcor()
        y= H.ycor()
        Segment[0].goto(x,y)

    move_Snake()

    #check for the body collusion with the head

    for s in Segment:
        if s.distance(H)<20:
            time.sleep(1)
            H.goto(0,0)
            H.direction = "stop"

            #hide the sagment
            for s in Segment:
                s.goto(1000,1000)
            Segment.clear()
            score = 0

            #reset the delay
            Delay -= 0.001
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score),
                      align="center", font=("Courier", 24, "normal"))


    time.sleep(Delay)


wn.mainloop()