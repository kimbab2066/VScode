'''
#while문
i = 0
while(i < 10):
    print("hello")
    i+=1

#에러테스트
i = 0
while(i<3):
    print("hello")
    i-=1
    #break 없으면 loop

#실습 0~9까지 출력
i = 0
while(i<10):
    print(i,end=" ")
    i+=1

#실습 1~7 print반복
i = 1
while(i<=7):
    print(i,"번째 hello!")
    i += 1

#구구단
val = int(input("출력하고 싶은 단:"))
i = 1
while(i<10):
    print(val,"*",i,"=",val*i)
    i+=1

#양의 정수 받아 출력
val = int(input("양의 정수 입력:"))
i = 1
while(i<=val):
    if(i % 3 == 0 or i %5 == 0): # or  둘 중 하나의 조건이 참
    #if(i % 3 == 0 and i % 5 == 0): and 두 조건이 모두 참
        print(i,end=" ")
    i+=1

#양의정수 입력, 0까지 감소
val = int(input("양의 정수 입력:"))
while(val>=0):
    print(val,end=" ")
    val-=1

#양의 정수 입력, 짝수 오름차순
val = int(input("양의 정수 입력:"))
i = 2
while(i<=val):
    print(i,end=" ")
    i+=2

#양의 정수 입력, 2의 제곱수 오름차순
val = int(input("양의 정수 입력:"))
i = 2
while(i<=val):
    print(i,end=" ")
    i*=2

#양의 정수 입력, 그 수 만큼 3의 배수 출력
val = int(input("양의 정수 입력:"))
i = 1
while(i<=val):
    print(3*i)
    i+=1

#샘플
val = int(input("양의 정수 입력:"))
i = 0
cnt = 0
while(cnt < val):
    cnt += 1
    i += 3
    print(i)

#양의 정수 입력, 그 수만큼 세로로 *
val = int(input("양의 정수 입력:"))
i = 0
while(i<val*val):
    print("*",end="")
    i+=1
    if(i%val==0):
        print()

#샘플
val = int(input("양의 정수 입력:"))
i = 0
while(i<val):
    print("*"*val)
    i+=1

#두 개의 정수 입력, 큰 수에서 작은 수 사이 카운트
val1 = int(input("정수 입력:"))
val2 = int(input("정수 입력:"))
if(val1<val2):
    num1 = val2
    num2 = val1
else:
    num1 = val1
    num2 = val2
    
while(num1>=num2):
    print(num1)
    num1 -= 1

#샘플 python swap 예시
val1 = int(input("정수 입력:"))
val2 = int(input("정수 입력:"))
if(val1<val2):
    val1,val2 = val2,val1
while(val1>=val2):
    print(val1)
    val1-=1

#누적합 구하기
#1~n까지의 합
n = int(input("정수 입력:"))
i = 1
sum = 0
while(i<=n):
    sum+=i
    i+=1
print(sum)

#정수 3개의 합계
i = 0
sum = 0
while(i<3):
    val = int(input("정수 입력:"))
    sum += val
    i+=1
print("합계는",sum,"입니다.")

#정수입력, 자리수의 합
val = int(input("정수 입력:"))
sum = 0
while(val>0):
    sum += val%10
    val //= 10
print(sum)

#정수 입력, 자릿수 출력
val = int(input("정수 입력:"))
cnt = 0
while(val>0):
    val //= 10
    cnt+=1
print(cnt)

#보초값(sentinel) 사용
#성적들의 평균 구하기
sum = 0
cnt = 0
while(True):
    score = int(input("성적 입력:"))
    if(score<0):
        break
    sum += score
    cnt += 1

print("성적의 평균은 %f 입니다." % (sum/cnt))

#샘플
n = 0
sum = 0
score = 0
print("음수 입력 시 종료")
while(score>=0):
    score = int(input("성적 입력:"))
    if(score>0):
        sum+=score
        n+=1
if(n>0):
    avg = sum/n
print("성적의 평균은 %f입니다"%avg)

#최대값 구하기 알고리즘
max = -1

val = int(input("정수 입력:"))

while(val>=0):
    if val>max:
        max = val
    val = int(input("정수 입력:"))

if max != -1:
    print("최대값:",max,"입니다.")
#샘플
max = -1
n = int(input("양의 정수 입력:"))

while(n>=0):
    if n > max:
        max = n
    n = int(input("양의 정수 입력:"))

if max != -1:
    print("최대값:",max,"입니다.")

#난수(Random Number)
import random
val = random.randint(1,10)
print(val)

#주사위 굴려 3 나오면 종료
import random

val = random.randint(1,6)
while(val!=3):
    print("주사위를 굴렸다. %d나옴"%val)
    val = random.randint(1,6)
print("드디어 3 나옴.")

#랜덤하게 구구단 문제 3개 출력
import random
print("구구단 게임입니다.")
i = 0
cnt = 0

while i<3:
    f_n = random.randint(1,9)
    s_n = random.randint(1,9)
    print(f_n,"*",s_n,"= ",end="")

    val = int(input())
    
    if val == f_n*s_n:
        print("맞습니다")
        cnt+=1
    else:
        print("틀렸습니다")

    i+=1
print("총 3문제 중 %d문제 맞추셨습니다"%cnt)

#샘플
import random
print("구구단 게임입니다.")
i = 0
cnt = 0

while i<3:
    f_n = random.randint(1,9)
    s_n = random.randint(1,9)
    result = f_n*s_n

    print(f_n,'*',s_n,"= ",end="")
    ans = int(input())

    if ans == result:
        print("맞습니다.")
        cnt+=1
    else:
        print("틀렸습니다.")

    i+=1
print("총 3문제 중 %d문제 맞추셨습니다."%cnt)

#가위 바위 보 게임
import random
print("이길 때 까지 계속 합니다.")
win = False

while(not win):
    val = input("가위,바위,보 중 선택:")
    com = random.randint(1,3) #1 = 가위, 2 = 바위, 3 = 보
    print("컴퓨터: ",end="")

    if com ==1:
        print("가위")
        if val =="가위":
            print("비겼다")
        elif val == "바위":
            print("이겼다")
            win = True
        else :
            print("졌다")

    if com ==2:
        print("바위")
        if val =="가위":
            print("졌다")
        elif val == "바위":
            print("비겼다")
        else :
            print("이겼다")
            win = True

    if com ==3:
        print("보")
        if val =="가위":
            print("이겼다")
            win = True
        elif val == "바위":
            print("졌다")
        else :
            print("비겼다")
'''