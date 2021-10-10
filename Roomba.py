class Solution:
    def solve(self, moves, x, y):
        x1 = sum([1 if m == 'EAST' else -1 if m == 'WEST' else 0 for m in moves])
        y1 = sum([1 if m == 'NORTH' else -1 if m == 'SOUTH' else 0 for m in moves])
        if(x1 == x and y1 == y):
            return True
        else:
            return False