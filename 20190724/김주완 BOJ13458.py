'''
date: 2019-07-19
'''

N = int(input())
people = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for num in people:
    if num > 0:
        cnt += 1
    num -= B
    if num > 0:
        o, r = num//C, num%C
        if r == 0:
            cnt += o
        else:
            cnt += o + 1
print(cnt)