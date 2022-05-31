#for문
#시퀀스 가능
'''
#샘플1
for i in [0,1,2]:
    print(i)

#샘플2 - 리스트(List)
a = [0,1,2]
for i in a:
    print(i)

#샘플3 - 문자열(String)
for i in "Hello":
    print(i)

#샘플4 - 튜플(tuple)
fruits = ('apple','orange','grape')

for i in fruits:
    print(i)

#실습 - 구구단
for i in range(1,10):
    print("5 *",i,"=",5*i)

#실습 - score
score = [90,35,75,69,80]
num = 0
for i in score:
    num+=1
    if( i >=70):
        print(num,"번 학생 점수는",i,"이고 합격")

    else:
        print(num,"번 학생 점수는",i,"이고 불합격")

#실습 - range()
for i in range(2):
    print("hello")

for i in range(3):
    print(i)

for i in range(5,10):
    print(i,end=" ")

print()

for i in range(0,10,2):
    print(i,end=" ")

print()

for i in range(10,0,-2):
    print(i, end=" ")

print()
#실습 - revered()
for i in reversed(range(3)):
    print(i,end=" ")

#1~10까지 모든 수의 합 구하기
sum = 0
for i in range (0,11,3):
        sum+=i
print(sum)

#입력 횟수대로 반복하는 프로그램
cnt = int(input("횟수 입력: "))
for i in range (cnt):
   print("hello",i)

#정수 입력 받아 1~숫자까지 합 계산
val = int(input("어디까지 계산: "))
sum = 0
for i in range (val+1):
    sum += i

print("1부터%d까지의 정수의 합:%d"%(i,sum))

#구구단 
dan = int(input("단:"))
for i in range (1,10):
    print("%d * %d = %d" %(dan,i,dan*i))

#양의 정수 입력 받고 짝수 오름차순
val = int(input("양의 정수 입력: "))
for i in range (2,val+1,2):
    print(i,end=" ")    

#양의 정수 입력 받고 3의 배수
val = int(input("양의 정수 입력: "))
for i in range(1,val+1):
    print(3*i)

#정수 두개 입력 받고 둘 중 큰 수에서 작은 수 사이 카운트 다운
val1 = int(input("정수 입력: "))
val2 = int(input("정수 입력: "))

if(val1<val2):
    val1,val2 = val2,val1

for i in range (val1,val2-1,-1):
    print(i)

#ver2
val1 = int(input("정수 입력: "))
val2 = int(input("정수 입력: "))

if(val1<val2):
    val1,val2 = val2,val1

for i in reversed(range(val2,val1+1,1)):
    print(i)

#정수 두개 입력 받아 작은수->큰수의 합
val1 = int(input("정수 입력: "))
val2 = int(input("정수 입력: "))

if val1>val2:
    val1,val2 = val2,val1

sum = 0
for i in range(val1,val2+1):
    sum += i
print("%d에서 %d까지 더하면 %d"%(val1,val2,sum))

#반복문의 변수에 값을 변경
for i in range(10):
    print(i,end=" ")
    i = 10  #영향 x

#break = 제어흐름 중단 , continue = 제어흐름 유지

#실습 - break 
i = 0
while True:
    print(i,end=" ")
    i+=1
    if i ==3:
        break
print()
print("무한루프탈출")

#실습 - break 2
for i in range(10000):
    print(i,end=" ")
    if i == 10:
        break
print()
print("반복문 탈출")

#실습 - continue
i = 0
while i<10:
    i+=1
    if i%2 == 0:
        continue
    print(i,end=" ")

#실습 - continue 2
i = 0
for i in range (10):
    i+=1
    if i%2 ==0:
        continue
    print(i,end=" ")

#pass문
for i in range(10):
    pass
while True:
    pass

#중첩 반복문
for i in range(3):
    for j in range(2):
        print(j,end=" ")
    print()

#사각형 출력
for i in range(3):
    for j in range(5):
        print("*",end="")
    print()

#가로 세로 입력 받아 직사각형 그리기
width = int(input("가로:"))
height = int(input("세로:"))
for i in range(height):
    for j in range(width):
        print("*",end="")
    print()

#층수 입력받아 직각 삼각형 그리기
floor = int(input("층수:"))
for i in range(floor):
    for j in range(i+1):
        print("*",end="")
    print()

#층수 입력받아 직각 삼각형 뒤집어 그리기
floor = int(input("층수:"))
for i in range(floor):
    for k in range(floor+1,i,-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()

#층수 입력받아 역 직각 삼각형 그리기
floor = int(input("층수:"))
for i in reversed(range(floor)):
    for j in range(i+1):
        print("*",end="")
    print()

#2~9단 모두 출력
for i in range(2,10):
    for j in range(1,10):
        print("%d * %d = %d" %(i,j,i*j))
    print()
'''