"""Generate Parenthesess"""

"""Problems links"""
# https://leetcode.com/problems/generate-parentheses

"""Import required"""
from typing import List


"""Define global variables"""
n: int

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global n

        with open('input.txt', 'r') as f:
            """Set variables"""
            n = int(f.readline())


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, n:int)->List[str]:
        #solve here
        res = []

        def generateOutput(parenthenes_list: List[int]):
            #push in to result
            tmp = ""
            for i in parenthenes_list:
                if i:
                    tmp+="("
                else:
                    tmp+=")"
            return tmp
        
        def backtrack(index: int, op: int, cl: int, parenthenes_list: List[int]):
            """
            Back track function.
            We use op, cl to cache number of parenthenes at index i - 1

            Args:
                index (int): current index
                op (int): number of open parenthenes at index i-1
                cl (int): number of close parenthenes at index i-1
                parenthenes_list (List[int]): list of parenthenes at index i - 1
            """


            #check condition
            if(op < cl) or op > n or cl > n:
                return 
            
            #limit reach
            if(index == 2*n):
                tmp = generateOutput(parenthenes_list)
                res.append(tmp)
                return 

            # try adding open parenthenes
            parenthenes_list.append(1)
            backtrack(index + 1, op + 1, cl, parenthenes_list)
            
            # remove the last index
            parenthenes_list.pop()
            
            #try adding close parenthenes
            parenthenes_list.append(0)
            backtrack(index + 1, op, cl + 1, parenthenes_list)
            parenthenes_list.pop()
        
        backtrack(0, 0, 0, [])
        return res
        pass


def app():
    global n
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(n)

app()