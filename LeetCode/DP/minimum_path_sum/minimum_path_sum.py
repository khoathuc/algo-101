"""Pascal triangle"""

"""Problems links"""
# https://leetcode.com/problems/minimum-path-sum

"""Import required"""
from typing import List


"""Define global variables"""
grid: List[List[int]] = []

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global grid
        with open('input.txt', 'r') as f:
            """Set variables"""
            while True:
                row_data = f.readline()
                """Set variables"""
                row = [int(row_data) for row_data in row_data.split()]

                if(len(row) == 0):
                    break

                grid.append(row)


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, grid: List[List[int]]):
        row_length, col_length = len(grid), len(grid[0])
        res: List[List[int]] = [[0] * col_length for i in range(row_length)]

        for i in range(0, row_length):
            for j in range(0, col_length):
                if(i == 0 and j == 0):
                    res[i][j] = grid[i][j]
                elif(i == 0):
                    res[i][j] = res[i][j - 1] + grid[i][j]
                elif(j == 0):
                    res[i][j] = res[i - 1][j] + grid[i][j]
                else:
                    res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]
        
        return res[row_length - 1][col_length - 1]        
def app():
    global grid
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    print(solution.solve(grid))

app()