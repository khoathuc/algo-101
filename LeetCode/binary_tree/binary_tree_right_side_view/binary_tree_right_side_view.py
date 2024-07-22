"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/binary-tree-right-side-view

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
    def solve(self, root: Optional[TreeNode]) -> List[List[int]]:
        dump = TreeNode()
        dump.right = root
        tmp = dump.right
        while(tmp is not None):
            tmp.left = None
            tmp = tmp.right
        
        def printNode(node: Optional[TreeNode]):
            if(node is None):
                return
            print(node.val)
            printNode(node.right)
            
        printNode(dump.right)
        return dump.right


def app():
    """Function read input, solve and output"""
    tree = Reader().read()
    
    solution = Solution()
    solution.solve(tree)

app()