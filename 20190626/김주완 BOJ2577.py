'''
date : 2019-06-20
'''

A = int(input())
B = int(input())
C = int(input())

pd = list(map(int, list(str(A*B*C))))
counts = [0] * 10
for c in pd:
    counts[c] += 1
for num in counts:
    print(num)