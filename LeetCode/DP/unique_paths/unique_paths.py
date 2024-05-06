"""Pascal triangle"""

"""Problems links"""
# https://leetcode.com/problems/unique-paths

"""Import required"""
from typing import List


"""Define global variables"""
m:int
n:int

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global m,n
        
        with open('input.txt', 'r') as f:
            """Set variables"""
            m = int(f.readline())
            n = int(f.readline())


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, m:int, n: int):
        """arr is number of unique path from topleft to (m,n)"""
        arr:List[List[int]] = [[0]*n for i in range(m)]
        for i in range (m):
            arr[i][0] = 1
        for j in range (n):
            arr[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
        
        return arr[m - 1][n - 1]
def app():
    global m,n
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    print(solution.solve(m,n))

app()