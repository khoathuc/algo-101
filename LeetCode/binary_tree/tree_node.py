from typing import Optional


class TreeNode:
    """Tree node class"""
    def __init__(self, val=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

    def find_node(self,val):
        if(self.val == val):
            return self
        
        if(self.left):
            res = self.left.find_node(val)
            if res:
                return res
        
        if(self.right):
            return self.right.find_node(val)