from turtle import *

speed(0)
delay(0)

up()
pencolor('blue')

def drawstar(size = 100):
	down()
	for i in range(5):
		forward(size)
		right(144)
	up()


for x in range(-300, 301, 50):
	for y in range(-300, 301, 50):
		if not((x==y) or (x==-y)):
			goto(x,y)
			if (y==0) or (x==0):
				pencolor('red')
			drawstar(40)
			pencolor('blue')
