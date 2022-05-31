'''
#List

score = [100,90,60,50,20]
print(score)
print(score[0])
print(score[4])
print(score[0]+score[4])
print(score[-1])

#시퀀스(sequence) 자료형
#리스트, 튜플, range, 문자열, 바이트, 바이트배열

#List Indexing 13p
a = []
b = [1,2,3]
c = ['abc','def','가나다']
d = [3.14,55,'hello']
print(a)
print(b)
print(c)
print(d)
print(d[0]+d[2])

#예제 15p
score = [100,80,95,90,70]

sum = score[0] + score[1] + score[2] + score[3] + score[4]
print(sum)
print(sum/len(score))

#에제 16p
score = [100,80,95,90,70]
sum = 0
for i in range(len(score)):
    sum += score[i]

print("합계:",sum)
print("평균",sum/len(score))

#덧셈 연산자 21p
a = [101,102,103]
b = [201,202,203]
print(a+b)

#곱셈 연산자 22p
a = [101,102,103]
print(a*2)

#비교연산자 23p
c = [10,20,30]
d = [10,20,30,40]
print(c == d) #false
print(c >d) #false
print(c < d) #true
print(c != d) #true

#내장함수 24,25p
#len()
score = [100,20,30,40,50]
#sum()
print(sum(score))
#max()
print(max(score))
#min()
print(min(score))

#list() 26p
a = range(1,5)
print(a)

b = list(range(1,5))
print(b)

c = list("test")
print(c)

#빈리스트 27p
#[], list() 둘 다 같음
a = []
print(a)
b = list()
print(b)

#method : 객체에 속한 함수 28~31p
a = [1,2,3]
print(a)
a.append(4)
print(a)

b = []
print(b)
b.append(10)
print(b)

#append(리스트) 32p
#list 안 list 가능
a = [1,2,3]
a.append([40,50])
print(a)
print(len(a)) # 4가 나옴

#extend(리스트) 33p
a = [1,2,3]
a.extend([40,50])
print(a)
print(len(a))

# append vs extend
# append는 요소 x를 리스트 끝에 추가
# extend는 리스트를 기존 리스트 뒤에 추가

#insert(index,item) 34p
a = [1,2,3]
a.insert(2,100)
print(a)
print(len(a))

#35p
a = [1,2,3]
a.insert(0,100)
print(a)

a = [1,2,3]
a.insert(len(a),100) # a.append(100)과 동일
print(a)
a.append(200)
print(a)

#리스트 요소 삭제 36p
#remove(x) 요소 x를 찾아서 리스트에서 삭제
#pop(index) index 위치의 요소를 찾아서 반환 후, 해당 요소를 삭제. 인덱스 사용 안할 시 마지막 요소 반환 후 삭제
#del 명령어

#remove(값) 37p
a = [1,2,3]
print(a)
a.remove(2)
print(a)
a.remove(4) #없어서 에러
print(a)

#remove(값) 38p
a = [1,2,3,1]
a.remove(1)
print(a)

#pop(index) 39p
a = [1,2,3]
print(a)
a.pop(1)
print(a)
a.pop()
print(a)

#del 40p
a = [1,2,3]
print(a)
del a[1]
print(a)

#index(값) 41p
#index(값) 
#리스트 특정 값의 인덱스를 구함
#같은 값이 두 개 이상이면 첫번째 인덱스 반환
#없는 값을 넣으면 에러
a = [1,2,3,1]
print(a.index(1))
print(a.index(3))

#count(값) 42p
#특정 값의 개수, 없으면 0
a = [1,2,3,1]
print(a.count(1))
print(a.count(2))

#reverse() 43p
#리스트에서 요소의 순서를 역순으로 만들어 줌
a = [1,2,3,4,5]
a.reverse()
print(a)

#sort() 44p
#리스트의 요소를 오름차순으로 정렬
#내림차순은 sort(reverse=True)
a = [3,2,6,4,1]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

#clear() 45p
#리스트의 모든 요소를 삭제하고 빈 리스트 []가 됨
a = [1,2,3]
print(a)
a.clear()
print(a)

#copy() 46p
#리스트를 복사해서 또 다른 리스트 만듬
#또 다른 리스트->값은 같지만 다른 리스트(깊은 복사)
a = [1,2,3]
print(a)
b = a.copy()
print(b)

#얕은 복사 47p
a = [1,2,3]
print(a)
b = a
print(a)

#48~52p
#참조(Reference)
#참조 : 객체 주소값

#얕은 복사 예시
a = [1,2,3]
b = a
print(b)
b[0] = 100
print(b)
print(a)

#깊은 복사 예시
a = [1,2,3]
b = a.copy()
print(b)
b[0]=200
print(a)
print(b)

#실습 53p
a = list()
for i in range(0,5):
    a.append(i)
    print(a[i])

#ver.2
list = []
for i in range(0,5):
    list.append(i)
    print("list[%d] = %d" %(i,list[i]))


#실습 55p
list = []
for i in reversed(range(0,5)):
    #list.append(i)
    list.append(i+1)
for i in range(0,5):
    print("list[%d] = %d" %(i,list[i]))

#실습 57p
list = []
num = 0.0
for i in range(0,11):
    list.append(num)
    print("list[%d] = %.1f" %(i,num))
    num+=0.1

#ver.2
list = []
for i in range(11):
    list.append(i/10)
    print("list[%d] = %.1f" %(i,list[i]))
'''
#실습 마무리
#입력받은 10개의 점수를 sort() 해서 작은수부터 출력
list = []
for i in range(10):
    val = int(input("정수 입력:"))
    list.append(val)

#list = val.split(" ")
list.sort()
for i in range(10):
    print(list[i],end=" ")
print()

for i in range(len(list)):
    print("%d은 %d번 나왔습니다." %(list[i],list.count(list[i])))
    i+=list.count(list[i])
    break
#동일 점수 count