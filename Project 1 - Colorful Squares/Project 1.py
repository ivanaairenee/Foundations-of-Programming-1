import turtle
import random

#prompt user to input the side length of the first square
slength= turtle.numinput("Rotating Colorful Squares", "Please enter the side length of the first square: ", default=40, minval=20, maxval=60)

#move turtle 100 to the left
turtle.up()
turtle.goto(-180,0)

#change turtle's colormode to 255
turtle.colormode(255)


#determine variables for turtle's degrees' and length
sudut=90
leftlength=slength

#repeat the process of drawing squares using for function
for a in range(36):
#determine the fastest speed for turtle
    turtle.speed(0)
#set the squares' color to random
    turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#set squares' border to black
    turtle.pencolor('black')
#draw squares
    turtle.setheading(sudut)
    leftlength=leftlength+3
    sudut=sudut-10
    turtle.begin_fill()
    turtle.down()
    turtle.forward(leftlength)
    turtle.left(90)
    turtle.forward(leftlength)
    turtle.left(90)
    turtle.forward(leftlength)
    turtle.left(90)
    turtle.forward(leftlength)
    turtle.end_fill()
  
    
    
#move turtle to the right
turtle.up()
turtle.goto(180,0)

#repeat the process of drawing squares using for function
sudut=0
for a in range(36):
#determine the fastest speed for turtle
    turtle.speed(0)
#set the squares' color to random
    turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#set squares' border to black
    turtle.pencolor('black')
#draw squares
    turtle.setheading(sudut)
    slength=slength+3
    sudut=sudut+10
    turtle.begin_fill()
    turtle.down()
    turtle.forward(slength)
    turtle.left(90)
    turtle.forward(slength)
    turtle.left(90)
    turtle.forward(slength)
    turtle.left(90)
    turtle.forward(slength)
    turtle.end_fill()
    

#move the turtle to the bottom
turtle.up()
turtle.goto(-180,-230)
#hide the turtle to make it invisible
turtle.hideturtle()
#give a text that says how many squares there are
turtle.pencolor("blue")
turtle.write("There are 72 Colorful Rotating Squares", font=8)
#prompt user to exit on click
print ("Click anywhere on the screen to exit")
#wait for user to exit
turtle.exitonclick()


    

