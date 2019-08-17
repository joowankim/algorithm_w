'''
date: 2019-08-15
'''

for test_case in range(1, int(input())+1):
    N = int(input())

    fib = [[0, 0] for _ in range(N+1)]

    if N > 0:
        fib[0] = [1, 0]
        fib[1] = [0, 1]
    else:
        fib[0] = [1, 0]


    for i in range(2, N+1):
        fib[i] = [fib[i-1][0] + fib[i-2][0], fib[i-1][1] + fib[i-2][1]]

    print("{} {}".format(fib[N][0], fib[N][1]))


