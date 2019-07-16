num_idcs = [[0, 1, 2, 4, 5, 6],
						[1, 4],
						[0, 1, 3, 5, 6],
						[0, 1, 3, 4, 6],
						[1, 2, 3, 4],
						[0, 2, 3, 4, 6],
						[0, 2, 3, 4, 5, 6],
						[0, 1, 4],
						[0, 1, 2, 3, 4, 5, 6],
						[0, 1, 2, 3, 4, 6]]

s, n = map(int, input().split())
n = list(str(n))

lines = [[(0, i) for i in range(1, s+1)],
				 [(i, s+1) for i in range(1, s+1)],
				 [(i, 0) for i in range(1, s+1)],
				 [(s+1, i) for i in range(1, s+1)],
				 [(s+1+i, s+1) for i in range(1, s+1)],
				 [(s+1+i ,0) for i in range(1, s+1)],
				 [(2*s+2, i) for i in range(1, s+1)]]

def create_num(num):
	print_num = [[' '] * (s+3) for _ in range(2*s+3)]

	for idx in num_idcs[int(num)]:
		for (x, y) in lines[idx]:
			if 0 < y < s+1:
				print_num[x][y] = '-'
			else:
				print_num[x][y] = '|'	
	return print_num

nums = [[''] for _ in range(2*s+3)]
for number in n:
	p_n = create_num(number)
	for i in range(2*s+3):
		nums[i] += ''.join(p_n[i])

for i in range(2*s+3):
	print(''.join(nums[i]))
