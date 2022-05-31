'''
name = input("what is your name?")
print("hello "+name)
age = input("how old are you?")
print(age+" years")

x = int(input("첫번째정수: "))
y = int(input("두번째정수: "))
sum = x+y
print(sum)

x = int(input("정수1: "))
y = int(input("정수2: "))

print("곱은",x*y,"입니다.")

a = 11
if (a==10):
    print("10입니다.")
else :
    print("다른값")

def func():
    num = int(input("정수입력: "))
    if(num>50):
        print("50보다큼")
    else:
        print("50보다 큰 숫자를 입력하세요.")
        func()
func()

s = ("Hello"     +" world")
print(s)

weight = 25.5
print(weight)
weight = 32.4
print(weight)

x=y=z=10
print(x)
print(y)
print(z)
print(x,y,z,sep=",")

x,y=10,20
print(x,y)
x,y=y,x
print(x,y)

y = 'hello'
print(y)

x = 'hello'
y = 'world'
print(x+y)
x = '100'
y =  '200'
print(x+y)
x= 100
y=200
print(x+y)

v = 10
print(type(v),v)
v = '10'
print(type(v),v)
v = 10.1
print(type(v),v)
v = 'world'
print(type(v),v)
del v
print(v)

x = None
print(x)

import keyword
print(keyword.kwlist)
'''


'''
x = str(3)
y = 'hi'
print(x+y)
'''

#def
#type()
#keyword