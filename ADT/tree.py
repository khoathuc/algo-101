from node import Node

class Tree():
    """Tree class"""

    def __init__(self) -> None:
        self.root = None #Type: Node
        self.nodes = [] #Type: List[Node]

    def addNode(self, node_data) -> Node:
        node_val = node_data[0]
        node = Node(node_val)
        self.nodes.append(node)

        if(self.root is None):
            self.root = node

        return self
    
    def getNode(self, val) -> Node:
        for node in self.nodes:
            if(node.getLabel() == val):
                return node

    
    def updateNode(self, node, parent, right_sibling):
        

