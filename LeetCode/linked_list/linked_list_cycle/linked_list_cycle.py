"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/linked-list-cycle

"""Import required"""
from typing import List


"""Define global variables"""

"""Reader class"""
class Reader(LinkedListReader):
    @classmethod
    def read(cls):
        super().build_linked_list()
        return cls.linked_list


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