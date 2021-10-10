class Solution:
    def solve(self, nums):
        return sum(map(lambda x: (len(str(x)) % 2) == 1, nums))