"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/[problems]

"""Import required"""
from typing import List


"""Define global variables"""
word1: str
word2: str

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global word1, word2

        with open('input.txt', 'r') as f:
            """Set variables"""
            word1 = f.readline()
            word2 = f.readline()


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, word1:str, word2:str):
        #solve here
        print(word1, word2)
        pass


def app():
    global word1, word2
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(word1, word2)

app()