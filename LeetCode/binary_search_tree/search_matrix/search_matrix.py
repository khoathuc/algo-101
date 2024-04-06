# https://leetcode.com/problems/search-in-rotated-sorted-array

from typing import List

import sys
sys.path.append('..')
#pylint: disable=wrong-import-position
from binary_search_tree import BinarySearch
#pylint: enable=wrong-import-position
# pylint: disable=E1101

matrix: List[int] = []
target: int = 0

class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global matrix
        global target

        with open('input.txt', 'r') as f:
            m = int(f.readline())

            for i in range (m):
                row_data = f.readline()
                row = [int(num_str) for num_str in row_data.split()]

                matrix.append(row)
                
            target = f.readline()

class Solution():
    def search(self, matrix, target: int) -> bool:
        print(BinarySearch.matrixSearch2(matrix,  target))
        return True if BinarySearch.matrixSearch(matrix,  target) else False


def app():
    Reader().read()
    print(matrix)
    solution = Solution()
    res = solution.search(matrix,int(target))
    print(res)

app()