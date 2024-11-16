def linear_search(nums, target):
	for i in range(0, len(nums)):
		if nums[i] == target:
			return i
	return None

def binary_search(nums, target):
	l = 0
	h = len(nums) - 1
	while l <= h:
		m = (l+h) // 2
		if nums[m] == target:
			return m
		elif nums[m] > target:
			h = m - 1
		elif nums[m] < target:
			l = m + 1
	return None

def kadane(nums):
	m_sum = float("-inf")
	c_sum = 0
	for i in nums:
		c_sum = max(i, c_sum+i)
		m_sum = max(m_sum, c_sum)
	return m_sum

def selection_sort(nums):
	l = []
	while len(nums) != 0:
		m = float("-inf")
		for i in nums:
			if i > m:
				m = i
		l.append(m)
		nums.remove(m)
	return l
