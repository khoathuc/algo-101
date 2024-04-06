# https://leetcode.com/problems/search-insert-position

from typing import List

import sys
sys.path.append('..')
#pylint: disable=wrong-import-position
from binary_search_tree import BinarySearch
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
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = BinarySearch.binarySearch(nums, 0, len(nums) - 1, target)

        print(index)


def app():
    Reader().read()
    
    solution = Solution()
    solution.searchInsert(nums, int(target))

app()