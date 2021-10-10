import copy
class Solution:
    def solve(self, matrix):
        dp_matrix = copy.deepcopy(matrix)
        row: int = 1
        number_columns: int = len(matrix[0]) - 1
        while row < len(matrix):
            dp_matrix[row - 1] = zip(range(number_columns + 1), dp_matrix[row -1])
            dp_matrix[row - 1] = sorted(dp_matrix[row -1], key = lambda x: x[1])
            for i in range(number_columns + 1):
                last_row_min = \
                    dp_matrix[row - 1][0][1] if dp_matrix[row - 1][0][0] != i else dp_matrix[row -1 ][1][1]
                dp_matrix[row][i] = last_row_min  + matrix[row][i]
            row += 1
        return min(dp_matrix[-1])
