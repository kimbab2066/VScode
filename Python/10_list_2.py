'''
#7p
a = [1,2,3,4,5]
for i in a:
    print(i)

# enumerate()함수
# 리스트 요소에 순서 값을 부여해주는 함수

num = ['one','two','three','four']
for i in enumerate(num):
    print(i)

num = ['one','two','three','four']
for idx,val in enumerate(num):
    print(idx,val)

#while로 요소 출력 11p
a = [1,2,3,4,5]
i = 0
while i < len(a):
    print(a[i])
    i+=1

#for를 이용한 성적 출력
score = [100,80,95,90,70]

sum = 0
for i in score:
    sum+=i

print(sum)
print(sum/len(score))


#while를 이용한 성적 출력
score = [100,80,95,90,70]

sum,i=0,0

while i<len(score):
    sum+=score[i]
    i+=1
print(sum)
print(sum/len(score))

#실습14p
#5명의 성적 입력 받고 성적 모두 출력
score = list()
for i in range(0,5):
    score.append(int(input("성적 입력: ")))

for i in range(0,len(score)):
    print("%d번째 성적:%d" %(i+1,score[i]))

#최소값 구하기
score = [100,80,95,90,70]

min = score[0]
for i in score:
    if min > i:
        min = i
print("최소값: %d" %min)

#최대값 구하기
score = [100,80,95,90,70]

max = score[0]
for i in score:
    if max < i:
        max = i
print("최대값:%d"%max)



score = [100,20,40,50,60]
min,max = 101,0
for i in score:
    if min > i:
        min = i
    if max < i:
        max = i
print("최소값: %d, 최대값: %d" %(min,max))

#정렬 이용
score = [100,80,95,90,70]
score.sort()
min = score[0]
score.sort(reverse=True)
max = score[0]
print("최소값: %d, 최대값: %d" %(min,max))

#min, max함수
score = [100,80,95,90,70]
min = min(score)
max = max(score)
print("최소값: %d, 최대값: %d" %(min,max))

#sum함수
score = [100,80,95,90,70]
sum = sum(score)
print("합계: ",sum)
print("평균: ",sum/len(score))

#실습22p
#성적 개수 제한 없이 입력받아 최고,최저,평균 구하기 음수가 입력되면 종료

score = 0
arr = []
while score >=0:
    score = int(input("성적 입력:"))
    if score >=0:
        arr.append(score)
if len(arr) > 0:
    print("최고:%d, 최저:%d. 평균:%.1f"%(max(arr),min(arr),sum(arr)/len(arr)))
else :
    print("입력 값이 없음")


#리스트 함축(list comprehension)
#[출력식 for 변수 in 리스트 if 조건식]
#if 조건식은 생략 가능
s = [i*2 for i in range(10)]
print(s)

list = [0,1,2,3,4,5]
s = [i for i in list]
print(s)

#조건식 붙이기 27p
s = [i for i in range(10) if i%2 == 0]
print(s)

s = [i**2 for i in range(10) if i%2 == 0]
print(s)

#함축식을 이용해서 
s = [round(i*0.1,1) for i in range(10)]
print(s) # 실수처리 에러

#2차원 리스트29,30p
#가로 x 세로 = 행(row), 열(column)
#리스트 = [[요소,요소],[요소,요소],[요소,요소]]
a = [[1,2], [3,4], [5,6]]
print(a)
 
#예제 31p
a = [[1,2], [3,4], [5,6]]
print(a[0][0])
print(a[2][1])
print(a[1][0])
a[1][0] = 100
print(a[1][0])

#반복문 사용요소 출력
a = [[1,2], [3,4], [5,6]]
for x,y in a:
    print(x,y)

#중첩for문 사용
a = [[1,2], [3,4], [5,6]]
for i in a:
    for j in i:
        print(j,end=" ")
    print()

#while문 사용하여 요소 출력
a = [[1,2], [3,4], [5,6]]
i = 0
while i<len(a):
    x,y = a[i]
    print(x,y)
    i+=1

#***
#중첩 while문 사용 35p
a = [[1,2], [3,4], [5,6]]
i = 0
while i<len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j],end=" ")
        j+=1
    print()
    i+=1

#pprint모듈 사용 요소 출력
from pprint import pprint
a = [[1,2], [3,4], [5,6]]
pprint(a,indent=1,width=20)

#반복문으로 2차원 리스트 만들기
from pprint import pprint
a  = []
for i in range(5):
    list = []
    for j in range(3):
        list.append(i*2 + (j+1))
    a.append(list)
pprint(a,indent=1,width=20)

from pprint import pprint
#리스트 함축 사용
a = [[i *2 + (j+1) for j in range(2)] for i in range(3)]
pprint(a,indent=1,width=20)

#2차원 리스트 사용하여 이름 성적 저장후 평균과 최고 성적 학생 이름,점수 출력
list = [['john',80],['lan',95],['alice',70]]
sum = 0
top_std = ""
top_score = 0

for name,score in list:
    sum+=score
    if(score>top_score):
        top_score = score
        top_std = name
    
    
print("평균: ",sum/len(list))
print("최고 성적 학생: ",top_std)
print("최고 성적 점수: ",top_score)
'''
'''
#튜플
#가변성(mutable)객체 자료형
#리스트, 집합, 딕셔너리

#불가변성(immutable)객체 자료형
#튜플, 수치자료형(int, float), 문자열(str)

#id()함수 : 객체의 고유한 reference id 값을 반환, id가 같으면 내부적으로 같음
a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))

#튜플
#요소 저장 가능 그러나 변경,추가,삭제 불가(읽기 전용 리ㅡ트)
#함수 리턴값처럼 값이 변경되면 안될 때 사용
#형식 : 튜플 = (요소1,요소2,요소3...요소n) ()괄호 없이 그냥 , 구분 가능
a = (1,2,3,4,5)
print(a)
b = 10,20,30,40,50
print(b)


#요소 하나인 튜플 = 끝에 ,
a = (10,)
print(a)
'''
#tuple()함수 사용해보기
a = tuple(range(5))
print(a)

b = tuple(range(5,10))
print(b)


