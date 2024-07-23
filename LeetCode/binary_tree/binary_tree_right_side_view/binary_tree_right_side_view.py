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
        tree_level: List[List[TreeNode]] = []
        
        # append root
        if(root is None):
            return []

        tree_level.append([root])

        # travel each level and push to queue        
        curr_level = tree_level[-1]
        while(len(curr_level) > 0):
            new_level: List[TreeNode] = []
            #loop through each node in level and push their children in queue.
            #because we visit node from left=> right => order is considered to be right.
            for i, node in enumerate(curr_level):
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)

            #break if new level is null
            if(len(new_level) == 0):
                break
            
            #else append to tree level and update current level
            tree_level.append(new_level)
            curr_level = tree_level[-1]
        
        #return res
        def generateRes():
            res = []
            for node_level in tree_level:
                node_most_right = node_level[-1]
                if(node_most_right):
                    res.append(node_most_right.val)
                
            return res
        
        return generateRes()
def app():
    """Function read input, solve and output"""
    tree = Reader().read()
    
    solution = Solution()
    print(solution.solve(tree))

app()