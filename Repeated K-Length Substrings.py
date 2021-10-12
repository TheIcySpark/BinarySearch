from collections import defaultdict

class Solution:
    def solve(self, s, k):
        cont: int = 0
        i: int = 0
        found = defaultdict(int)
        while i <= len(s) - k :
            found[s[i:i + k]] += 1
            if found[s[i: i + k]] == 2:
                cont += 1
            i += 1
        return cont