"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/palindrome-partitioning

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
        res: List[List[str]] = []
        tmp: List[str] = []

        def check_palindrome(tmp_str):
            return tmp_str == tmp_str[::-1]

        def backtrack(index):
            if(index == len(s)):
                res.append(tmp.copy())
                return 
            
            for i in range(index, len(s)):
                substr = s[index:i+1]
                if(check_palindrome(substr)):
                    tmp.append(substr)
                    backtrack(i+1)
                    tmp.pop()

        backtrack(0)
        print(res)
        pass


def app():
    global s
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(s)

app()