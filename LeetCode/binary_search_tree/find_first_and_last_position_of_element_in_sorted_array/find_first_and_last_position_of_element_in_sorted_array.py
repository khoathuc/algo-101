# https://leetcode.com/problems/search-in-rotated-sorted-array

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
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        first_index =  BinarySearch.findFirst(nums, start, end,  target)
        last_index =  BinarySearch.findLast(nums, start, end, target)

        return [first_index, last_index]


def app():
    Reader().read()
    
    solution = Solution()
    res = solution.search(nums, int(target))
    print(res)

app()