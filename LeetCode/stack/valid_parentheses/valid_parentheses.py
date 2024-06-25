"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/[problems]

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
            """Set variables"""
            s = f.readline().strip()

class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, s:str):
        #solve here
        tmp = []
        def is_pair(last, curr):
            if last == "(" and curr == ")" or last == "{" and curr == "}" or last == "[" and curr == "]":
                return True
            return False
        
        for i , char in enumerate(s):
            if tmp:
                last = tmp[-1]
                if is_pair(last, char):
                    tmp.pop()
                    continue
            tmp.append(char)
        
        return not tmp


def app():
    global s
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(s)

app()