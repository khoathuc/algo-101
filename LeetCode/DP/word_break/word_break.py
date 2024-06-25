"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/[problems]

"""Import required"""
from typing import List


"""Define global variables"""
s: str
wordDict: List[str]

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global s, wordDict

        with open('input.txt', 'r') as f:
            """Set variables"""
            s = f.readline().strip()
            wordDict = f.readline().strip().split()


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, s:str, wordDict:List[str]):
        #solve here
        s = " "+s
        res: List[int]=[False] * (len(s))
        # " " is always True
        res[0] = True
        
        # iterate through s
        for i in range(len(s)):
            if(res[i] == False):
                continue

            if(i == len(s)):
                break
            
            for word in wordDict:
                tmp = s[1:i + 1] + word
                if(i + len(word) > len(s)):
                    continue
                if(tmp ==  s[1 : (i + len(word) + 1)]):
                    res[i + len(word)] = True
        
        return res[-1]
        pass


def app():
    global s, wordDict
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(s, wordDict)

app()