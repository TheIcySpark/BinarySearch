import functools
class Solution:
    def solve(self, n):
        n2 = [int(i) for i in str(n)]
        return n == sum(map(lambda x: pow(x, len(n2)), n2))
        