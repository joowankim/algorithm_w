'''
date: 2019-08-30
'''

R, C = map(int, input().split())
MAP = [input() for _ in range(R)]

counts = [0] * 5

def count(x, y):
    cnt = 0
    for i in range(2):
        for j in range(2):
            cur = MAP[x+i][y+j]
            if cur == 'X':
                cnt += 1
            if cur == '#':
                return
    counts[cnt] += 1

for i in range(R-1):
    for j in range(C-1):
        count(i, j)

for i in range(5):
    print(counts[i])