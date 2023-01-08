# 데이터컴퓨팅수업과제
# 이화여자대학교
# 휴먼기계바이오공학부
# 학번: 2270090
# 이름: 최희나
# 파일명: hw10.py
# 설명: Regular Expression

import re

state_names=['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut',
             'Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa',
             'Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan',
             'Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada',
             'New Hampshire','New Jersey','New Mexico','New York','North Carolina',
             'North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island',
             'South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia',
             'Washington','West Virginia','Wisconsin','Wyoming']

# 다음 문제를 해결하기 위해 빈칸에 들어갈 regular expressions를 작성하고 코드를 제출하시오.
# 1. N 으로 시작하면서, 한 단어로 이루어진 주를 찾아서 출력하기(5점)
for a in state_names :
	n=re.search('^N\w+$', a)
	if n :
		print(n.group())


# 2. N 으로 시작하면서, 두 단어로 이루어져 있고, 두 번째 단어에 y(또는 Y)가 포함된 주를 찾아서 출력하기 (5점)
for a in state_names :
	n=re.search('^N\w+\s\w*[yY]\w*$', a)
	if n :
		print(n.group())
