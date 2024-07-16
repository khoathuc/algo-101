"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

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
            nums = [int(num) for num in f.readline().split()]


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, nums: List[int]):
        #solve here
        l,r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            mid = l + (r-l)//2
            
            if(nums[mid] > nums[r]):
                l = mid + 1
    
            else:
                res = min(res, nums[mid])
                r = mid - 1

        min(res, nums[l])
        pass

def app():
    global nums
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(nums)

app()