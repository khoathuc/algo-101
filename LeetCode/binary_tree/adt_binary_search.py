"""Binary search tree"""
class Node:
    """Node class"""

    def __init__(self, key:int):
        """_summary_

        Args:
            key (int): value of node
        """
        self.left = None
        self.right = None
        self.val = key


    def insert(self, data: int):
        """
        Insert a node to a tree
        Args:
            data (int): _description_

        Returns:
            self
        """
        if not data:
            return 
        
        if data < self.val:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)

        if data > self.val:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

        return self


    def inorderTraversal(self, node):
        pass
