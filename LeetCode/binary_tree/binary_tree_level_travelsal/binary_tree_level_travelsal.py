"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/binary-tree-level-order-traversal

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
        #solve here
        res: List[List[int]] = []
        node_queue: Queue[List[TreeNode]] = []

        if(root is None):
            return res

        node_queue.append([root])

        while len(node_queue) > 0:
            level: List[int] = []
            queue: List[TreeNode] = []
            tmp_nodes = node_queue.pop(0)

            for i, node in enumerate(tmp_nodes):
                if(node is None):
                    continue
                level.append(node.val)
                queue.extend([node.left, node.right])
            
            if(len(level) > 0):
                res.append(level)
            if(len(queue) > 0):
                node_queue.append(queue)

        print(res)
        pass


def app():
    """Function read input, solve and output"""
    tree = Reader().read()
    
    solution = Solution()
    solution.solve(tree)

app()