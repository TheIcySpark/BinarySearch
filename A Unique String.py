class Solution:
    def solve(self, s):
        h = {}
        for i in s:
            h[i] = h.get(i, 0) + 1
            if h[i] != 1:
                 return False
        return True