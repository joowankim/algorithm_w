'''
date: 2019-08-15
'''

N = int(input())

dp = [0] * (N+1)

if N == 2:
    dp[2] = 1
elif N > 2:
    dp[2] = 1
    dp[3] = 1

for i in range(4, N+1):
    if i%2 != 0 and i%3 != 0:
        dp[i] = dp[i-1] + 1
    elif i%2 == 0 and i%3 != 0:
        dp[i] = min(dp[i-1], dp[int(i/2)]) + 1
    elif i%2 != 0 and i%3 == 0:
        dp[i] = min(dp[i-1], dp[int(i/3)]) + 1
    else:
        dp[i] = min(dp[i-1], dp[int(i/2)], dp[int(i/3)]) + 1

print(dp[N])