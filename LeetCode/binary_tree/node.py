"""Binary tree"""
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
        self.pos = None


    def insert(self, data: int, pos):
        """
        Insert a node to a tree
        Args:
            data (int): _description_
            pos (str): left or right
        Returns:
            self
        """
        if not data:
            return 

        child = Node(data)   
        child.pos = pos

        if pos == 'l':
            self.left = child
        
        elif pos == 'r':
            self.right = child

        return self

    
    def isLeft(self):
        return self.pos == 'l'
    

    def isRight(self):
        return self.pos == 'r'

    def inorderTraversal(self, node):
        pass
