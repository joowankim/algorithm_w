'''
date: 2019-06-20
'''

def combi(depth, pre, lotto):
    if depth == 6:
        print(lotto)
    else:
        for i in range(pre+1, k):
            combi(depth+1, i, lotto + S[i] + ' ')
while True:
    inputs = input().split()
    if inputs == ['0']:
        break
    k, S = int(inputs[0]), inputs[1:]

    combi(0, -1, '')
    print()