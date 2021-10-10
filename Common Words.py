class Solution:
    def solve(self, s0, s1):
        s0 = s0.lower()
        s1 = s1.lower()
        d1 = {k:1 for k in s0.split()}
        c = 0
        for w in s1.split():
            if d1.get(w, 0) == 0: 
                continue
            else:
                c += 1
                d1[w] = 0
        return c