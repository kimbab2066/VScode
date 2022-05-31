'''
#if condition
x=10
if (x>1):
    print("x는 1보다 크다")
    print("이것도 실행")

#test
x = int(input("정수입력: "))

if (x % 10):
    print("10의 배수가 아님")

#입력값<100
x = int(input("정수 입력: "))
if(x<100):
    print("입력한 정수",x,"는 100보다 작음")

print("프로그램 종료")

#절대값
x = int(input("정수입력: "))

if (x < 0):
    x = -x

print("절대값은",x,"입니다.")

#if-else

x = int(input("정수입력: "))
if(x<0):
    print("음수 입니다")
else:
    print("양수 입니다")

#if-else 2
x = int(input("정수 입력: "))
if (x % 2 == 0):
    print("짝수 입니다.")
else:
    print("홀수 입니다.")
print("\n프로그램 종료")

#if-else3
print("두 개의 정수 입력")
x = int(input("정수1입력: "))
y = int(input("정수2입력: "))
if(x>y):
    result = x
else:
    result = y

print("둘 중 큰 수는",result,"입니다.")

#if-else4
print("두 개의 정수 입력")
x = int(input("정수1 입력: "))
y = int(input("정수2 입력: "))

if(x>y):
    result = x-y
else:
    result = y-x
print("두 수의 차는",result,"입니다.")
'''
#NESTION IF-ELSE 
'''
#Nestion if-else test
a=  9
if(a>0):
    if(a == 10):
        print("10입니다")
    else:
        print("10이 아닙니다.")
else:
    print("0보다작습니다")        

#Nesting if-else
x = int(input("정수 입력: "))
if(x>=0):
    print("양수입니다.")
    if(x%2==0):
        print("짝수입니다.")
    else:
        print("홀수입니다")
else:
    print("음수입니다.")        
'''
##
'''
#Nesting if-else2
age = int(input("나이 입력: "))
if(age>=20):
    print("응시가능")
    score = int(input("점수 입력: "))
    if(score>=80):
        print("합격")
    else:
        print("불합격")
else:
    print("응시불가능")

#Nesting if-else3
print("*"*44)
print("프로그램")
gender = input("성별 입력[남자/여자]: ")
if(gender=="남자"):
    weight = float(input("몸무게 입력(kg): "))
    if(weight>=70):
        result = "농구"
    else:
        result = "축구"
else:
    height = float(input("키 입력(cm): "))
    if(height>=160):
        result = "배구"
    else:
        result = "피구"
print("[",result,"] 경기를 추천합니다")
'''
#IF-ELIF-ELSE


'''
#if-elif-else 1
score = int(input("점수 입력: "))
if(score>=70):
    print("합격")
elif(score>=50):
    print("재시")
else:
    print("불합격")

#if-elif-else 2
score = int(input("점수 입력: "))
if(score>=90):
    result = "A"
elif(score>=80):
    result = "B"
elif(score>=70):
    result = "C"
elif(score>=60):
    result = "D"
else:
    result = "F"
print(result,"학점")

#if-elif-else 3
val = int(input("정수 입력: "))
if(val>0):
    result = "양수"
elif(val==0):
    result = val
else:
    result = "음수"
print(result,"입니다.")

#if-elif-else 4
print("두 개의 정수 입력")
val1 = int(input("정수1 입력:"))
val2 = int(input("정수2 입력:"))
if(val1>val2):
    print("정수1이 정수2보다 크다.")
elif(val1==val2):
    print("두 수는 같다.")
else:
    print("정수1이 정수2보다 작다.")
'''

#Complex Conditional Expression(복합조건식)
'''
year = int(input("연도 입력: "))
if((year % 4 == 0 and year % 100 != 0 )or year % 400 == 0):
    print(year,"년은 윤년.")
else:
    print(year,"년은 평년.")

#CCE test1
month = int(input("몇 월입니까: "))
if(3 <= month and month <= 5):
    print("봄.")
elif(6 <= month and month <= 8):
    print("여름.")
elif(9 <= month and month <= 11):
    print("가을.")
elif(month == 1 or month == 2 or month == 12):
    print("겨울.")
else:
    print("그런 월 없음.")
'''  
#PASS
score = int(input("점수 입력: "))
if(score>=70):
    pass
elif(score >= 50):
    pass
else:
    pass
