"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/[problems]

"""Import required"""
from typing import List


"""Define global variables"""
var_1: List[int] = []
var_2: int = 0

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global var_1
        global var_2

        with open('input.txt', 'r') as f:
            nums_data = f.readline()

            """Set variables"""
            var_1 = [int(num_str) for num_str in nums_data.split()]

            var_2 = f.readline()


    """
    Based on binary search

    Args:
        arr (List[int]): sorted array
        l (int): left position
        r (int): right position
        x (int): value need to be search

    Returns:
        int: index of value in given array
    """

    if l > r:
        return l

    mid = l + (r-l) // 2

    if arr[mid] == x:
        return mid
    
    elif arr[mid] > x:
        """if mid value > x, find the left side"""
        return insert_index(arr, l, mid - 1, x)
    
    else:
        """if mid value > x, find the right side"""
        return insert_index(arr, mid + 1, r, x)


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self):
        pass


def app():
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve()

app()