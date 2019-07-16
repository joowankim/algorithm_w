N, K = map(int, input().split())

nums = [i for i in range(2, N+1)]

while True:
	n = nums[0]
	for num in nums:
		if num%n == 0:
			nums.remove(num)
			K -= 1
			if K == 0:
				print(num)
				quit()
