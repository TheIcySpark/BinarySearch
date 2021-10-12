class Solution:
    def solve(self, nums):
        nums_sorted = sorted(nums)
        substract = lambda x, y: abs(x - y)
        ascending_diference = sum([substract(x, y) for (x, y) in zip(nums_sorted, nums)])
        nums_sorted.reverse()
        descending_diference = sum([substract(x, y) for (x, y) in zip(nums_sorted, nums)])
        return min(ascending_diference, descending_diference)