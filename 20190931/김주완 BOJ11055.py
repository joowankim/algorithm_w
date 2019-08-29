'''
date: 2019-08-29
'''

N = int(input())
A = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    dp[i] = A[i]
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j] + A[i]:
            dp[i] = dp[j] + A[i]

print(max(dp))