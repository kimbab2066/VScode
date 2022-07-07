#2739   구구단
'''
N = int(input())
for i in range (1,10):
    print("%d * %d = %d" %(N,i,N*i))
'''
#10950  A+B-3
'''
T = int(input())
while T > 0:
    A,B = map(int,input().split())
    print(A+B)
    T-=1
'''
#이 문제 풀면서 JAVA StringBuilder같은게 있나 확인해봤는데 없었음
#8393   Sum
'''
N = int(input())
total = 0
for i in range(1, N+1):
    total += i
print(total)
#print(sum(range(int(input())+1)))
#list = range(1,10)
'''
#15552  빠른 A+B
'''
import sys
T = int(sys.stdin.readline())
for i in range(T):
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)
'''
#2741   N 찍기
'''
import sys
N = int(sys.stdin.readline())
for i in range(1,N+1):
    print(i)
'''
#2742   기찍 N
'''
import sys
N = int(sys.stdin.readline())
for i in reversed(range(1,N+1)):
    print(i)
'''
#11021  A+B-7
'''
import sys
T = int(sys.stdin.readline())
for i in range(1,T+1):
    A,B = map(int,sys.stdin.readline().split())
    print("Case #%d: %d"%(i,A+B))
'''
#11022  A+B-8
'''
import sys
T = int(sys.stdin.readline())
for i in range(1,T+1):
    A,B = map(int,sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d"%(i,A,B,A+B))
'''
#2438   별찍기-1
''''''
#2439   별찍기-2
''''''
#10871  X보다 작은 수
''''''
#10952  A+B-5
''''''
#10951  A+B-4
''''''
#1110   더하기 사이클
''''''