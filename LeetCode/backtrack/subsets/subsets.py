"""Subsets"""

"""Problems links"""
# https://leetcode.com/problems/subsets

"""Import required"""
from typing import List


"""Define global variables"""
nums: str

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global nums

        with open('input.txt', 'r') as f:
            """Set variables"""
            row_data = f.readline()
            """Set variables"""
            nums = [int(row_data) for row_data in row_data.split()]


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, nums:List[int]):
        #solve here
        res = []
        def backtrack(subsets: List[int]):
            if(len(subsets) > len(nums)):
                return 

            res.append(subsets)

            for i in nums:
                if subsets and (i in subsets or i <= subsets[-1]):
                    continue

                subsets.append(i)
                backtrack(subsets.copy())
                subsets.pop()

        backtrack([])
        return res


def app():
    global nums
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(nums)

app()