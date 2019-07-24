'''
date: 2019-07-20
'''

for test_case in range(1, int(input())+1):
    seq = [input() for _ in range(5)]
    leng = [len(s) for s in seq]

    res = ""
    for j in range(max(leng)):
        for i in range(5):
            if leng[i] > j:
                res += seq[i][j]

    print("#{} {}".format(test_case, res))
