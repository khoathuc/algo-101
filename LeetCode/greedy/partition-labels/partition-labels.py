"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

"""Import required"""
from typing import List


"""Define global variables"""
s: str


"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global s

        with open('input.txt', 'r') as f:
            s = f.readline()


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, s: str):
        print(s)
        

def app():
    """Function read input, solve and output"""
    Reader().read()
    global s

    solution = Solution()
    print(solution.solve(s))

app()