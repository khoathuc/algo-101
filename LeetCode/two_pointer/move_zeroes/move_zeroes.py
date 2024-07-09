"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/move-zeroes

"""Import required"""
from typing import List


"""Define global variables"""
nums: List[str]

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global nums

        with open('input.txt', 'r') as f:
            """Set variables"""
            nums = [int(num) for num in f.readline().split()]


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, nums: List[str]):
        #solve here
        print(nums)

        #try push all non-zeros at the beginning
        #sort the nonzero to the beginning. When sorting done, all non zeroes will be at the beginning
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
        
        print(nums)
        pass


def app():
    global nums
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(nums)

app()