'''
date: 2019-07-13
'''

n, T = map(int, input().split())
Q = list(map(int, input().split()))

t = 0
for i in range(n):
    t += Q[i]
    if t > T:
        print(i)
        break
if t <= T:
    print(n)
