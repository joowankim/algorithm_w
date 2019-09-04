'''
date: 2019-09-02
'''

def swap(s, start, last):
    interval = int((last - start + 1) / 2)
    for i in range(interval):
        tmp = s[start+i]
        s[start+i] = s[start+interval+i]
        s[start+interval+i] = tmp

for test_case in range(1, int(input())+1):
    n = int(input())
    seq = list(map(int, input().split()))
    answer = [i for i in range(1, n+1)]

    search = []
    for k in range(int(n/2), -1, -1):
        for i in range(n-2*k-1):
            search += [(i, i+2*k+1)]

    order = []
    sorted_ = False
    while not sorted_:
        print(seq)
        for (s, e) in search:
            not_sort = 0
            interval = int((e - s + 1) / 2)
            for i in range(interval):
                if seq[s+i] - seq[s+interval+i] == interval:
                    not_sort += 1
            if not_sort == interval:
                swap(seq, s, e)
                order += [(s+1, e+1)]
                break

        if answer == seq:
            sorted_ = True


    print(len(order))
    for (s, e) in order:
        print(s, e)
