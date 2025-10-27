import turtle as t
import random

#1.다각형 그리기
'''
n = int(input("몇 각형을 그릴까요? "))

for i in range(n):
    t.forward(100)
    t.left(360/n)

#2.다각형 그리기 입력한 각형->삼각형까지 그리기

n = int(input("몇 각형부터 그릴까요? "))
t.shape("turtle")
t.speed(5)
for i in range(n,2,-1):
    for j in range(i):
        t.forward(100)
        t.left(360/i)

#3.다각형 그리고 색칠하기
color=["red","green","purple","blue","brown","yellow",
       "navy","gray","pink","orange"]

n = int(input("몇 각형부터 그릴까요? ")) #최대 9각형 까지
t.shape("turtle")
t.speed(5)

for i in range(n,2,-1):
    t.color(color[i])
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()

#4.다각형 그리고 랜덤 색칠하기

color=["red","green","purple","blue","brown","yellow",
       "navy","gray","pink","orange"]

n = int(input("몇 각형부터 그릴까요? ")) #최대 9각형 까지
t.shape("turtle")
t.speed(5)

for i in range(n,2,-1):
    random.shuffle(color)
    t.color(color[i])
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()
'''
#5.색 중복 없애기
color=["red","yellow","orange"]
count=0
n = int(input("몇 각형부터 그릴까요? ")) #최대 색깔 리스트 변수 갯수
for i in range(n,2,-1):
    t.color(color[count])
    count=count+1
    if count==3:
        count=0
    t.begin_fill()
    for j in range(i):
        t.forward(100)
        t.left(360/i)
    t.end_fill()



















