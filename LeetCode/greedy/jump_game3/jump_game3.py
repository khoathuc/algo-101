"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/jump-game

"""Import required"""
from typing import List


"""Define global variables"""
arr: List[int] = []
start: int
"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global arr
        global start

        with open('input.txt', 'r') as f:
            nums_data = f.readline()

            """Set variables"""
            arr = [int(num_str) for num_str in nums_data.split()]
            start = f.readline()


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self):
        global arr
        global start
        
        print(arr, start)
        pass

def app():
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    print(solution.solve())

app()