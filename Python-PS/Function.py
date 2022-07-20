#15596 정수 N개의 합
'''

def solve(a):
    ans = sum(a)
    return ans
'''
#4673 Self Numbers
#self_number
'''
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
'''
# 1 <= x <= 10000
# 생성자가 없는 숫자를 셀프 넘버라고 한다.

#1065 한수
'''
print(sum((i//100 + i % 10 == i //10 % 10 * 2) | (i<100) for i in range(1,int(input())+1)))
#True = 1 이니 True인 경우 1씩 합치니 += 1과 같음
#백의 자리 + 일의 자리 == 십의자리 * 2
#753의경우
#7 + 3 == 5 * 2
'''