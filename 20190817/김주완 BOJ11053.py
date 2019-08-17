'''
date: 2019-08-15
'''

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
max_ = 1
for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
    max_ = max(max_, dp[i])

print(max_)

