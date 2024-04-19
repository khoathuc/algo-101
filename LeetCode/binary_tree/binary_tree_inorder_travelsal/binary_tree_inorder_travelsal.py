"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/binary-tree-inorder-traversal/

"""Import required"""
import sys
sys.path.append('../../binary_tree/adt')

from adt import TreeReader
from typing import List
from typing import Optional
from tree_node import TreeNode
from queue import Queue


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
    def solve(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res


def app():
    """Function read input, solve and output"""
    tree = Reader().read()
    
    solution = Solution()
    solution.solve(tree)

app()