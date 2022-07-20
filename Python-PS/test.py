#self_number
u_set = set(range(1,10001))
b_set = set()

#1~10000
for i in range(1,10001):
    #숫자 i를 str형태로 바꿔서 850인 경우 8 5 0 으로 나눈다.
    for j in str(i):
        #기존의 i에 str(j)를 더해준다. 850 += 8, 5, 0 -> 863
        #i = 863이 되고 b_set에 add해준다.
        i+=int(j)
    b_set.add(i)

self_number = sorted(u_set - b_set)
for i in self_number:
    print(i)