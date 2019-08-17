'''
date: 2019-08-15
'''

N = int(input())

fib = [0] * (N+1)

fib[0] = 0
fib[1] = 1


for i in range(2, N+1):
    fib[i] = fib[i-1] + fib[i-2]

print("{}".format(fib[N]))


