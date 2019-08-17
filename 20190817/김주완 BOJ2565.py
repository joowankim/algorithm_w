'''
date: 2019-08-15
'''

N = int(input())
p = sorted([tuple(map(int, input().split())) for _ in range(N)])

line = [0] * N
for i in range(N):
    line[i] = p[i][1]

max_ = 1
dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if line[i] > line[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
    max_ = max(max_, dp[i])

print(N - max_)
