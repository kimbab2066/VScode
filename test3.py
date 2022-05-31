list = []
for i in range(5):
    val = int(input("정수 입력:"))
    list.append(val)

#list = val.split(" ")

#데이터 정렬
list.sort()
print(list)

cnt = []
for i in list:
    #1번 이상 중복되는 데이터를 뽑아서
    if i not in cnt:
        #새로운 리스트에 집어 넣고
        cnt.append(i)
#count를 이용해서 출력한다
for i in range(len(cnt)):
    print("%d는 %d번 나왔습니다." %(cnt[i], list.count(cnt[i])))

