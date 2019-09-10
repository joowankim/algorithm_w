'''
date: 2019-09-10
'''

N = int(input())

def hanoi(n, from_pos, to_pos, aux_pos):
    if n == 1:
        print(from_pos, to_pos)
        return
    hanoi(n-1, from_pos, aux_pos, to_pos)
    hanoi(1, from_pos, to_pos, aux_pos)
    hanoi(n-1, aux_pos, to_pos, from_pos)

print(2**N - 1)
if N <= 20:
    hanoi(N, 1, 3, 2)