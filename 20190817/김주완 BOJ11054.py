'''
date: 2019-08-15
'''

N = int(input())
A = list(map(int, input().split()))

dp = [[1, 1] for _ in range(N)]

for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j] and dp[i][0] < dp[j][0] + 1:
            dp[i][0] = dp[j][0] + 1

for i in range(N-1, 0, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j] and dp[i][1] < dp[j][1] + 1:
            dp[i][1] = dp[j][1] + 1
max_ = 1
for i in range(N):
    cur = sum(dp[i])-1
    if cur > max_:
        max_ = cur

print(max_)