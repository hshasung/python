#제어문-조건문(선택문)
'''
#홀짝 판별 프로그램

num=int(input("자연수 입력: "))

#1. 단일 선택문(단일 조건문) :짝수면 * 출력
if num % 2 == 0: #짝수라면
    print("*")
print(num)


#2. 이중 선택문(이중 조건문) :짝수면 짝수입니다 홀수면 홀수입니다
if num % 2 == 0:
    print("짝수입니다")
else:
    print("홀수입니다")

#예제 2 나이판별

# 나이가 17살 이상이면 "타 컸네" 그렇지 않으면 "넌 아직 어려"출력
age=int(input("나이 입력: "))

if age >= 17:
    print("다 컸네")
else:
    print("넌 아직 어려")


#예제 3 점수 입력 받아 80점 이상이면 합격 그렇지 않으면 불합격 출력

score=int(input("점수 입력: "))

if score >= 80:
    print("합격")
else:
    print("불합격")


#다중 선택문 if~elif~else
#나이 8미만 유아  8이상 19이하 학생 그 외에는 성인
age=int(input("나이 입력: "))

if age<8:
    print("유아")
elif age>=8 and age<=19:
    print("학생")
else:
    print("성인")



# 요일별 게임 조건

today=input("요일 입력:")

if today == "일요일":
    print("게임 열판하기")
elif today == "토요일":
    print("밤새서 게임하기")
else:
    print("물한잔 하기")
print("공부 시작")


total=int(input("손님 수 입력:"))

if total <=4:
    print("추가비용이 없습니다")
elif 5<=total<=8:
    print(f"추가비용은 {total-4}만원 입니다")
else:
    print("입장인원은 최대 8명입니다")
''' 


temp=int(input("체온 입력:"))
if temp>=40:
    print("고열립니다. 병원으로 뛰어가세요")
elif temp>=38:
    print("병원에 가세요")
elif temp>=37:
    print("학교에 가서 보건선생님을 만나요")
else:
    print("정상입니다 당장 학교로 가세요")











































  














