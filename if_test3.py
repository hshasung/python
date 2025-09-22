#제어문-선택문 if if~else if~elif~else

import random

#홀짝 구하기 %2
'''
num = 150
if num % 2 ==0:#짝수일때
    print("짝수입니다")
else:
    print("홀수입니다")

#학점구하기
score=int(input("점수 입력:"))

if score>=90:
    print("A학점입니다")
elif score>=80:
    print("B학점입니다")
elif score>=70:
    print("C학점입니다")
elif score>=60:
    print("D학점입니다")
else:
    print("F학점입니다")
'''
#1부터 6까지 적힌 주사위 두개를 던져 나오는 값을 a,b라고 할때
a=random.randint(1,6)
b=random.randint(1,6)
print(f'첫번째 주사위의 값은:{a}')
print(f'첫번째 주사위의 값은:{b}')

#a, b 모두 홀수이면 (a의 제곱 +b) 출력하시오
#a,b 모두 짝수이면 절대값(a-b)를 출력하시오# abs()

if a%2==1 and b%2==1:
    print(a**2 + b)
elif a%2==0 and b%2==0:
    print(abs(a-b))
else:
    print(2*(a+b))


































































































































































































































































































