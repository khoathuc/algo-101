"""Problems links"""
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

"""Import required"""
import sys
sys.path.append('../../binary_tree')
from tree_node import TreeNode
from typing import List, Optional


"""Define global variables"""
pre_order: List[int] = []
in_order: int = 0

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global pre_order
        global in_order

        with open('input.txt', 'r') as f:
            pre_data = f.readline()

            """Set variables"""
            pre_order = [int(data) for data in pre_data.split(',')]

            in_data = f.readline()

            """Set variables"""
            in_order = [int(data) for data in in_data.split(',')]


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, pre_order: List[int], in_order: List[int]):
        #solve here
        def build_tree(pre_o, in_o):
            if(len(pre_o) != len(in_o)):
                return None
            
            if(len(pre_o) == 0):
                return None
            
            node = TreeNode(pre_o[0])
            for i in range (len(in_o)):
                if(in_o[i] == node.val):
                    in_left = in_o[:i]
                    in_right = in_o[i+1:]
                    break
            
            pre_left = pre_o[1:len(in_left)+1]
            pre_right = pre_o[len(in_left)+1:]

            node.left = build_tree(pre_left, in_left)
            node.right = build_tree(pre_right, in_right)

            return node
        
        return build_tree(pre_order, in_order)
        
        # res = []

        # def inorder(node):
        #     if node is None:
        #         return
            
        #     inorder(node.left)
        #     res.append(node.val)
        #     inorder(node.right)
        
        # inorder(tree)
        # print(res)
        pass


def app():
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(pre_order, in_order)

app()