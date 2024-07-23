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
global k

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
    def solve(self, root: Optional[TreeNode], k: int) -> List[List[int]]:
        # in-order traversal
        in_order = []
        def inOrder(node):
            if node is None:
                return 
            
            
            inOrder(node.left)
            in_order.append(node)
            inOrder(node.right)            
        
        inOrder(root)
        
        k_node = in_order[k-1]
        return k_node.val

def app():
    global k
    """Function read input, solve and output"""
    tree = Reader().read()
    
    solution = Solution()
    print(solution.solve(tree, 1))

app()