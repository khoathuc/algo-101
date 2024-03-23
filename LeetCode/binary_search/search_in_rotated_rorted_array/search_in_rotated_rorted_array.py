# https://leetcode.com/problems/search-in-rotated-sorted-array

from typing import List

import sys
sys.path.append('..')
#pylint: disable=wrong-import-position
from binary_search import BinarySearch
#pylint: enable=wrong-import-position
# pylint: disable=E1101

nums: List[int] = []
target: int = 0

class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global nums
        global target

        with open('input.txt', 'r') as f:
            nums_data = f.readline()
            nums = [int(num_str) for num_str in nums_data.split()]

            target = f.readline()

class Solution():
    def search(self, nums: List[int], target: int) -> int:
        
        # find pivot
        pivot = BinarySearch.pivotSearch(nums)

        print(pivot)
        
        if(target >= nums[pivot]) and (target <= nums[len(nums) - 1]):
            return BinarySearch.binarySearch(nums, pivot, len(nums) - 1, target)
        elif (target >= nums[0]) and (target <= nums[pivot - 1]):
            return BinarySearch.binarySearch(nums, 0, pivot - 1, target)
        else:
            return -1


def app():
    Reader().read()
    
    solution = Solution()
    res = solution.search(nums, int(target))
    print(res)

app()