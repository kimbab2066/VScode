'''
#대입연산자
x = y = 100
print(x,y)

n1 , n2 = 100,200
print(n1,n2)


#산술연산자
print(1+2)
print(2-3)
print(3*4)
print(8/4)
print(7//4)
print(6%4)
print(2**8)

#실습
x = int(input("정수 입력: "))
print("10을 더하면",x+10)
print("10을 빼면",x-10)
print("10을 곱하면",x*10)
print("10을 나누면",x/10)

#실습
x = int(input("정수 입력: "))
print(x,"나누기 5의 몫은",x//5)
print(x,"나누기 5의 나머지는",x%5)

#실습
x = int(input("정수1 입력: "))
y = int(input("정수2 입력: "))
print("이들의 합은",x+y,"이고 곱은",x*y,"입니다.")

#실습
x  = float(input("실수 입력: "))
print("입력한 실수는",x)

#실습
x = float(input("cm 입력: "))
print("인치로 변환하면",x/2.54,"inch 입니다.")

#실습
x = int(input("num1 입력: "))
y = int(input("num2 입력: "))
z = int(input("num3 입력: "))
print("합계는",x+y+z,"이고 평균은",(x+y+z)/3,"입니다.")

#실습
str = input("생년원일: ")
print("출생일자: ",str[0:4],"년 ",str[4:6],"월 ",str[6:],"일",sep="")

#실습_2
x = int(input("생년월일: "))
year =  x//10000
month = (x%10000)//100
day = x%100
print("출생일자: ",year,"년 ",month,"월 ",day,"일",sep="")

#복합대입 연산자
a = 10
b = 20

#논리 연산자
y = int(input("연도 입력: "))
#print("윤년 여부 :", (y%4 == 0) and (y %100 != 0) or (y%400 == 0) )

def leap_year(y): 
    if(y%4==0):
        return  y%4==0
        if(y%100 !=0):
            return y%100 !=0
        elif(y%400==0):
            return y%400==0
        else:
            return False
    else:
        return False
    return False
print("윤년 여부:",leap_year(y))
'''
#비트 연산자 (2진수로 계산 -> 10진수로 반환)
