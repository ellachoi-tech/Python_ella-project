# 데이터컴퓨팅수업과제
# 이화여자대학교
# 휴먼기계바이오공학부
# 학번: 2270090
# 이름: 최희나
# 파일명: hw9.py
# 설명: String manipulation

# 문제1 : string에 문자열 "Central Nervous System Neoplasms" 저장
string = "Central Nervous System Neoplasms"

# 문제2 : Central Nervous 출력
print(string[0:15])

# 문제3 : Nervous System 출력
print(string[8:22])

# 문제4 : System Neoplasms 출력
print(string[16:])

# 문제5 : 대문자로 바꾸고 다시 저장
string = string.upper();
print(string)

# 문제6 : 공백단위로 분리후 str_split에 저장
str_split = string.split();
print(str_split)

# 문제7 : str_split을 _로 붙여서 출력
print('_'.join(str_split))
