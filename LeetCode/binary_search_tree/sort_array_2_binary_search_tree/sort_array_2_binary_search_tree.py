"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

"""Import required"""
import sys
sys.path.append('../../binary_tree/adt')

from typing import List
from typing import Optional

sys.path.append('../../binary_tree')
from tree_node import TreeNode

"""Define global variables"""
sorted_array: List[int] = []

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global sorted_array
        with open('input.txt', 'r') as f:
            nums_data = f.readline()

            """Set variables"""
            sorted_array = [int(num_str) for num_str in nums_data.split(',')]


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, arr: List[int]) -> Optional[TreeNode]:
        def buildNode(start, end):
            nonlocal arr
            if(start > end):
                return None
            mid = start + (end-start)//2
            
            node = TreeNode()
            node.val = arr[mid]
            node.left = buildNode(start, mid - 1)
            node.right = buildNode(mid + 1, end)    
            return node        
        
        root = buildNode(0, len(arr) - 1)

        res: List[int] = []
        def inOrder(node: Optional[TreeNode]):
            if(node is None):
                return 
            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)

        inOrder(root)
        print(res)


def app():
    global sorted_array
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(sorted_array)

app()