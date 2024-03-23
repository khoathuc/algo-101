class Node:
    """Node class"""
    leftmost_child = None
    right_sibling = None

    def __init__(self, label) -> None:
        self.label = label