"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list

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
    def solve(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_queue:Queue[TreeNode] = []
        
        # // pre-order travel tree and add node to queue
        def add_node(node):
            if node is None:
                return 

            node_queue.append(node)
            add_node(node.left)
            add_node(node.right)

        add_node(root)
  

        # init linked list
        dump = TreeNode()
        tmp=dump
        while(len(node_queue) > 0):
            curr = node_queue.pop(0)
            tmp.left = None
            tmp.right = curr
            tmp=tmp.right
    
        return dump.right
        pass


def app():
    """Function read input, solve and output"""
    tree = Reader().read()
    
    solution = Solution()
    solution.solve(tree)

app()