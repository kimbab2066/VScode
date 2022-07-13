#10818 최소, 최대
'''
N = int(input())
arr = list(map(int,input().split()))
print(min(arr),max(arr))
'''
#2562 최댓값
'''
import sys
arr = list()
for i in range(9):
    arr.append(int(sys.stdin.readline()))
print(max(arr))
print(arr.index(max(arr))+1)
'''
#x = [int(input()) for i in range(9)]
#print(max(x), x.index(max(x))+1 ,sep="\n")
#2577 숫자의 개수
'''

A = int(input())
B = int(input())
C = int(input())

d = list(map(int,str(A*B*C)))

for i in range(10):
    print(d.count(i))
'''
#3052 MODULO
'''

N = [int(input())%42 for i in range(10)]
print(len(set(N)))
'''
#1546 평균
'''
N = int(input())
arr = list(map(int,input().split()))
max = max(arr)
avg = [arr[i]/max*100 for i in range(N)]
print(sum(avg)/N)
print(sum(arr)/max*100/N)
'''
#8958 Score
'''
T = int(input())
list = []
for i in range(T):
    list.append(input())
sb = []
for i in range(T):
    cnt = 0
    sum = 0
    for j in list[i]:
        if(j == "O"):
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    sb.append(sum)
print(' '.join(map(str, sb)))
'''
#4344 Above Average
'''
'''
