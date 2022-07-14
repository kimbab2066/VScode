import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    data = input().strip().split(' ')
    scores = list(map(float, data[1:]))
    average = sum(scores) / len(scores)

    above = 0
    for score in scores:
        if score > average:
            above += 1

    print(f'{(above/len(scores))*100:.3f}%')