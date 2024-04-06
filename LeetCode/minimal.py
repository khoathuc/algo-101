"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/[problems]

"""Import required"""
from typing import List


"""Define global variables"""
var_1: List[int] = []
var_2: int = 0

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global var_1
        global var_2

        with open('input.txt', 'r') as f:
            nums_data = f.readline()

            """Set variables"""
            var_1 = [int(num_str) for num_str in nums_data.split()]

            var_2 = f.readline()


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self):
        #solve here
        pass


def app():
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve()

app()