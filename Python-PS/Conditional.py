#1330번 두 수 비교하기
'''
A,B = map(int,input().split())
if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
'''
#2753번 윤년
'''
y = int(input())
if y %4==0 and y%100 !=0 or y % 400 == 0:
    print(1)
else:
    print(0)
'''
#14681번 사분면
'''
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
'''
#2884번 알람시계
'''
H, M = map(int, input().split())
if M < 45:
    M = 60 - (45-M)
    H -= 1
    if(H<0):
        H = 23
    print(H,M)
else:
    print(H,M-45)
'''
#2525번 오븐시계
'''
A,B = map(int,input().split())
C = int(input())
B += C
while B>59:
    A+=1
    B-=60
if A>23:
    A-=24
print(A,B)
'''
#2480번 주사위 세개 
A,B,C = map(int,input().split())

if A==B==C:
    print(10000+A*1000)
elif A==B or A==C:
    print(1000+A*100)
elif B==A or B==C:
    print(1000+B*100)
elif C==A or C==B:
    print(1000+C*100)
else:
    print(max(A,max(B,C))*100)
