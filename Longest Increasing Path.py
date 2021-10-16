class Solution:
    def solve(self, matrix):
        max_increasing_path = 0
        posible_movements = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        columns, rows = len(matrix) - 1, len(matrix[0]) - 1
        dp = [[0 for j in range(rows + 1)] for i in range(columns + 1)]
        i = 0
        while i <= columns:
            j = 0
            while j <= rows:
                if dp[i][j] == 0:
                    stack = [(i, j)]
                    while stack:
                        current_position = stack[-1]
                        stack.pop()
                        dp_next_movements = [0]
                        all_next_movements_dp_computed = True
                        for posible_movement in posible_movements:
                            next_position = (current_position[0] + posible_movement[0], current_position[1] + posible_movement[1])
                            if valid_position(next_position, rows, columns):
                                if dp[next_position[0]][next_position[1]] == 0 and \
                                        matrix[current_position[0]][current_position[1]] < matrix[next_position[0]][next_position[1]]:
                                    stack.append(current_position)
                                    stack.append(next_position)
                                    not_all_next_movements_dp_compute = False
                                    break
                                else:
                                    if(matrix[current_position[0]][current_position[1]] < matrix[next_position[0]][next_position[1]]):
                                        dp_next_movements.append(dp[next_position[0]][next_position[1]])
                        if all_next_movements_dp_computed:
                            dp[current_position[0]][current_position[1]] = max(dp_next_movements) + 1
                            max_increasing_path = max(dp[current_position[0]][current_position[1]], max_increasing_path)
                j += 1
            i += 1
        return max_increasing_path            

                    


def valid_position(position, rows, columns):
    return True if position[0] >= 0 and position[0] <= columns and position[1] >= 0 and position[1] <= rows else False
