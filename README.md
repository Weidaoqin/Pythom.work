# Pythom.work
python.work
#e2.1DrawPython.py
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("green")
turtle.pensize(25)
turtle.seth(-40)
for i in range(2):
	turtle.circle(40,80)
	turtle.circle(-40,80)

	
turtle.pensize(25)
turtle.pencolor("black")
turtle.seth(-40)
for i in range(2):
	turtle.circle(40,80)
	turtle.circle(-40,80)

turtle.pencolor("green")
turtle.pensize(25)
turtle.seth(-40)
turtle.pencolor("red")
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.pensize(25)
turtle.seth(-40)
turtle.pensize(25)
turtle.pencolor("black")
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.seth(-20)
for i in range(2):
	turtle.circle(40,-80)
	turtle.circle(-40,-80)
