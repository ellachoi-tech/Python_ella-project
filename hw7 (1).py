# 데이터컴퓨팅수업과제
# 이화여자대학교
# 휴먼기계바이오공학부
# 학번: 2270090
# 이름: 최희나
# 파일명: hw7.py

from turtle import *

def diamond_flower(size=50, n=7, angle=30):
	down()
	for i in range(n):
		for j in range(2):
			forward(size)
			right(angle)
			forward(size)
			right(180-angle)
		right(360/n)
	up()
	
flower_dict = {
	'trigems':(3,70),
	'five':(5,50),
	'richnine':(9,50),
	'thinnine':(9,30),
	'needle':(30,10)
	}

def draw(name):
	clear()
	(n, angle) = flower_dict[name]
	diamond_flower(100, n, angle)

speed(0)
delay(0)
up()

while True :
	name = input('Enter flower name(q to exit): ')

	if(name == 'q'):
		break

	if name in flower_dict:
		draw(name)
	else:
		print('No flower named', name)
