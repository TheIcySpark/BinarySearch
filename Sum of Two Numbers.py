class Solution:
    def solve(self, nums, k):
        nums.sort()
        i = 0
        while i < len(nums) - 1 and k - nums[i] >= nums[i + 1]:
            search_value = k - nums[i]
            if binary_search(i + 1, len(nums) - 1, search_value, nums):
                return True
            i += 1
        return False

def binary_search(start, end, search_value, nums):
    while start <= end:
        m = int((start + end) / 2)
        if nums[m] == search_value:
            return True
        elif nums[m] < search_value:
            start = m + 1
        else:
            end = m - 1
    return False