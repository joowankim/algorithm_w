'''
date: 2019-08-01
'''

L, C = map(int, input().split())
word = sorted(input().split())

def permu(depth, pw, last):
    if depth == L:
        con, vow = 0, 0
        for i in range(L):
            if pw[i] in ['a', 'e', 'i', 'o', 'u']:
                vow += 1
        con = L - vow
        if con >= 2 and vow >= 1:
            print(pw)
    else:
        for i in range(last+1, C):
            permu(depth+1, pw + word[i], i)

permu(0, "", -1)

