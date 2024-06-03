"""Permutations"""

"""Problems links"""
# https://leetcode.com/problems/permutations

"""Import required"""
from typing import List


"""Define global variables"""
nums: List[int]

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
    def solve(self, nums: List[int]) -> List[List[int]]:
        #solve here
        res = []
        n = len(nums)

        def backtrack(index:int, permute:List[int]):
            if index == n:
                res.append(permute)
                return
            
            for i in nums:
                if(i in permute):
                    continue

                permute.append(i)
                backtrack(index + 1, permute.copy())
                permute.pop()

        backtrack(0, [])
        return(res)
        pass


def app():
    global nums
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(nums)

app()