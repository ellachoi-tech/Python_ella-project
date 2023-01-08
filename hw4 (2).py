from turtle import *
up()
clear()
x=-400
angle = 20
goto(x,0)
for i in range(5):
	down()
	for j in range(6):
		forward(40)
		right(angle)
		forward(40)
		right(180 - angle)
		forward(40)
		right(angle)
		forward(40)
		right(180 - angle)
		right(60)
	up()
	x = x + 200
	angle = angle+10
	goto(x,0)
