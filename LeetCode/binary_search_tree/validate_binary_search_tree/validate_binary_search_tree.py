"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/validate-binary-search-tree

"""Import required"""
import sys
sys.path.append('../../binary_tree/adt')

from adt import TreeReader
from typing import List
from typing import Optional
from tree_node import TreeNode


"""Define global variables"""

"""Reader class"""
class Reader(TreeReader):
    @classmethod
    def read(cls):
        super().build_tree()
        return cls.tree

class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, tree:Optional[TreeNode]):
        curr_value: int = float('-inf')
        res: bool = True

        def inOrder(node):
            nonlocal res, curr_value

            if node is None:
                return 
            
            inOrder(node.left)
            if(node.val <= curr_value):
                res = False
                return 
            else:
                curr_value = node.val
            
            inOrder(node.right)
        
        inOrder(tree)
        print(res)



def app():
    """Function read input, solve and output"""
    tree = Reader.read()
    
    solution = Solution()
    solution.solve(tree)

app()