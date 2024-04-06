"""Pascal triangle"""

"""Problems links"""
# https://leetcode.com/problems/pascals-triangle

"""Import required"""
from typing import List


"""Define global variables"""
MAX = 32
target: int = 0

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global target
        
        with open('input.txt', 'r') as f:
            """Set variables"""
            input = f.readline()
            target = int(input)


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self):
        global target

        res: List = [[1]]
        for i in range (1, target):
            sub: List = []
            for j in range (i + 1):
                if(j == 0) or (j == i):
                    sub.append(1)
                else:
                    print(res, i, j)
                    tmp = res[i - 1][j - 1] + res[i - 1][j]
                    sub.append(tmp)
            res.append(sub)
        
        print(res)


def app():
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve()

app()