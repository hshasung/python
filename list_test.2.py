
#리스트변수 - 여러개의 값을 저장,값을 변경,[]
'''
score=[]
print(score)
print(type(score))

score=[90.2, 78.6, 89.5, 67.8, 60.2, 99.5, 52.8]
#sort() 오름차순 정렬
score.sort()
print(score)
fruit=["사과","포도","파인애플","샤인머스켓","복숭아"]

fruit.sort()
print(fruit)

h=[5,4,9,2,7,3]

#역순 정렬

h.sort()
h.reverse()
print(h)
#h.sort(reverse=True)


fruit=["사과","포도","파인애플","샤인머스켓","복숭아"]

fruit.remove("파인애플")
fruit.append("망고")
fruit.pop(0)
fruit.insert(2,"딸기")
print(fruit)

#리스트 변수 함수 append(), remove(), insert(), pop(), sort(), reverse()

name_list=["김건영","김의준","김진성","남명진","박한올"]
print(name_list)
name_list[2]="김하성"
print(name_list)
name_list[4]="백지율"
print(name_list)
#['김건영', '김의준', '김하성', '남명진', '백지율']
#인덱싱
print(name_list[0:2])
print(name_list[1:4])
print(name_list[0:5:2])
print(name_list[1:4:2])
'''
import random

#random() 난수발생
'''
x=random.random() #0-1 사이의 난수 발생
print(x)

x=[1,2,3,4,5,6,7,8,9]
print(x)
y=random.choice(x)
print(y)
random.shuffle(x)
print(x)
z=random.sample(x,2)
print(z)
'''

x=random.randint(1.100)
print(x)
x=random.randint(1,18)
print(x)
















