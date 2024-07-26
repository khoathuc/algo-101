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
    def solve(self, root: Optional[TreeNode],p: TreeNode, q: TreeNode) -> TreeNode:
        # solve here
        height: dict[TreeNode, TreeNode] = {}
        parent: dict[TreeNode, TreeNode] = {}
        
        # travel all nodes to get parent of each node
        height[root] = 0
        parent[root] = None
        def in_order(node):
            if node is None:
                return
            
            if(node.left):
                parent[node.left] = node
                height[node.left] = height[node] + 1
                in_order(node.left)
                
            if(node.right):
                parent[node.right] = node
                height[node.right] = height[node] + 1
                in_order(node.right)
        
        in_order(root)
        
        # find LCA of p and q
        def lca(u: TreeNode, v: TreeNode):
            if(u == v):
                return u
            
            if(height[u] < height[v]):
                v = parent[v]
                return lca(u, v)
            
            if(height[u] > height[v]):
                u = parent[u]
                return lca(u, v)
            
            return lca(parent[u], parent[v])     
            
        return  lca(p,q)
        
        pass

def app():
    global k
    """Function read input, solve and output"""
    tree = Reader().read()
    q = tree.find_node(1)
    p  = tree.find_node(5)
    
    solution = Solution()
    solution.solve(tree, p, q)
    # print(solution.val)

app()