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


#데이터 정렬 후 1번 이상 중복되는 데이터를 뽑아서
#새로운 리스트에 집어 넣고 count를 이용해서 출력한다