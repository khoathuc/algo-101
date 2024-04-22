"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/jump-game

"""Import required"""
from typing import List


"""Define global variables"""
arr: List[int] = []

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global arr

        with open('input.txt', 'r') as f:
            nums_data = f.readline()

            """Set variables"""
            arr = [int(num_str) for num_str in nums_data.split()]


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self):
        global arr
        
        furthest = 0
        # list to store minimum step to reach to each index
        res: List[int] = [0] * len(arr)
        for i in range(len(arr) - 1):
            # we suppose that can reach last index
            tmp = i + arr[i]
            if(tmp > furthest):
                res[furthest + 1:tmp + 1] = [res[i] + 1] * (tmp + 1 - furthest)
                furthest = tmp
        
        # if iterate through all of index but still not return false, 
        # it show that we have visited the last index
        return res

def app():
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    print(solution.solve())

app()