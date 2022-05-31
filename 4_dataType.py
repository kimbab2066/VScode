'''
#16진수
a= 0xFA
print("16진수",a)

#8진수
b = 0o123
print("8진수",b)

#2진수 
c  = 0b01010011
print("2진수",c)

#숫자 입력_
n = 100_000
print(n)

#소수
f_a = 1.2
print(f_a)
print(type(f_a))

#지수 표현방식
val = 3.1415E8
val2 = 2312e-6
print(val)
print(val2)

#문자열
str = "김밥"
print(str)
print(type(str))

#boolean
a = True
b = False
print(a,b,sep="\n")
print(type(a))
print(type(b))

#boolean2
a =  (100<100)
print(a)
b = (300==300)
print(b)

#None
n  = None
print(n)
print(type(n))

#String,int different
x = 10
y = 20
print(x+y)

x = 'Hello'
y = 'World'
print(x+y)

#Circle Area
r = 5.0
c_area = 3.141592 *r*r
print("첫번째",c_area)

c_area = 3.141592 *r**2
print("두번째",c_area)

#BMI
def bmi_check():
    if(bmi>25):
        print("비만")
    elif(bmi>23):
        print("과체중")
    elif(bmi>18.5):
        print("정상")
    else:
        print("저체중")
#
h  = float(input())
w  = float(input())
bmi = w/h**2

bmi_check()

#boolean3
b1 = True
b2 = False
print(b1)
print(b2)
print(3<4)
print(3>4)

#quotes
s = "그가 좋아? '응' 왜?"
print(s)
#백슬래시\
k = "그가 좋아요 \"왜요?\" \'그냥요\'"
print(k)

#escape char
print("Hello \nWorld")
print("Hello \tWorld")
print("Hello \\World")
print("Hello \bWorld")
print("Hello \vWorld")
print("\u0061")

#formating
name = "홍길동"
age = 22
height =176.5
print("제 이름은 %s입니다"%name)
print("나이는 %d"%age)
print("키는%fcm"%height)
print("키는%.1fcm"%height)

#formating2
msg = "현재시각 %s."
time = "12:00pm"
print(msg %time)

#formating3
print("전공은 %s, %d학년."%("컴공",1))

#String Add
first="컴"
print(first+"공")

#String Multi
star = "*"
print(star*50)
s1 = "컴"
s2 = "공"
s3 = (s1+s2+"!!")*3
print(s3)

#indexing and slicing
s = "Hello"
print(s[0])
print(s[3])
print(s[-1])
print(s[0:4])

s = "Hello World"
print(s[2:5])
print(s[6:9])

s = "kkkkk difdsfasdf"
print(s[:5])
print(s[10:])

#slicing test
s = '20210514Friday'
print(s[0:4]+"년 "+s[4:6]+"월 "+s[6:8]+"일 "+s[8:])

#count() 
s = "Hello World"
print(s.count('l'))
print(s.count('w'))

#find()
s = "Hello World"
print(s.find("H"))
print(s.find("l"))
print(s.find("w"))
print(s.find("World"))
print(s.find("WORLD"))

#index()
s = "Hello World"
print(s.index("H"))
print(s.index("World"))
print(s.index("K"))

#strip()
s = '   hello   '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

#upper() lower()
s = "Hello World"
print(s.upper())
print(s.lower())

#join()
s = "Hello"
print(' . '.join(s))
sep = " == "
print(sep.join(s))

#replace()
s = "Hello World"
s = s.replace('Wo','ab')
print(s)

#split()
s = "Hello.World"
print(s.split())
s = "www.naver.com"
print(s.split("."))

#format()
s = "hi man {}"
#s = s.format("kim")
s = s.format("park")
print(s)

s = "hi Mr. {0} {1}"
s = s.format("kim","park")
print(s)

s = "hi Ms. {1} {0}"
s = s.format("lee","young")
print(s)

s = "hi Mr,Mrs. {str1} {str2}"
s = s.format(str1 ="김밥",str2="만두")
print(s)

#len()
s = "pypypypy"
print(len(s))
arr = [1,2,3,4,5,6]
print(len(arr))

#chr() ord()
print(chr(65))
print(ord("ㄱ"))

#hex() oct()
print(hex(45))
print(oct(78))

#casting1
print(str(10)+"10")
print(10+int("10"))
print(int("a"))

#casting2
print(float(3))
print(type(float(3)))
print(float(6/2))
print(float("2000"))
print(float("3.1415926"))

#casting3
score = int(input("정수입력: "))
print(str(score) + "점 입니다.")
'''