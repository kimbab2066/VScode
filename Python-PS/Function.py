#15596 정수 N개의 합
'''

def solve(a):
    ans = sum(a)
    return ans
'''
#4673 Self Numbers
'''
n_num = set(range(1,10001))
g_num = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    g_num.add(i)

#차집합 A - B
self_num = sorted(n_num - g_num)
for i in self_num:
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