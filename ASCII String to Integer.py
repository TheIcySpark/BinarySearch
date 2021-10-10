import re
class Solution:
    def solve(self, s):
        return sum( [int(i) if i != '' else 0 for i in re.split(r'[a-z]', s) ])
        