import sys
sys.path.append('../../binary_tree')
from tree_node import TreeNode
from typing import List, Optional

class TreeReader:
    """Tree reader class"""
    values:Optional[List]
    tree: Optional[TreeNode]

    @classmethod
    def read_input(cls):
        with open('input.txt', 'r') as file:
            input_data = file.read().strip()

        values = input_data.split(', ')
        for i, val in enumerate(values):
            if val.lower() == 'null':
                values[i] = None
            else:
                values[i] = int(val)
        
        cls.values = values
    
    @classmethod
    def build_tree(cls):
        cls.read_input()
        
        if(cls.values is None):
            cls.tree = None

        values = cls.values
        def build_tree(index):
            nonlocal values

            if index < len(values):
                if values[index] is None:
                    return None
                else:
                    node = TreeNode(values[index])
                    node.left = build_tree(2 * index + 1)
                    node.right = build_tree(2 * index + 2)
                    return node
            return None

        cls.tree = build_tree(0)
        