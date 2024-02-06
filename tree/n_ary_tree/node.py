class Node:
    """Node class"""

    def __init__(self, val, nodes=None) -> None:
        """_summary_

        Args:
            val (string): value or name of node
            nodes (Node): child nodes
        """

        self.__val = val
        self.__nodes = []
        
        if(nodes is not None):
            self.__nodes = nodes

    def addNode(self, node)->None:
        """Add child node in node

        Args:
            node (Node): child node
        """
        if(isinstance(node, Node)):
            self.__nodes.append(node)
    
    def getNodes(self):
        """get nodes

        Returns:
            Nodes[]: list of node
        """
        return self.__nodes
    
    def getVal(self):
        return self.__val

    def __repr__(self) -> str:
        repr_str = 'Root-{} '.format(self.getVal())
        for node in self.getNodes():
            repr_str += node.getVal() + ' '

        return repr_str