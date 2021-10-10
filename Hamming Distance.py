class Solution:
    def solve(self, x, y):
        x = bin(x).split('0b')[1][::-1]
        y = bin(y).split('0b')[1][::-1]
        while len(x) < len(y):
            x += '0'
        while len(y) < len(x):
            y += '0'
        return sum([v1!=v2 for (v1, v2) in zip(x, y)])