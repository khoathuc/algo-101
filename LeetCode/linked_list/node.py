from typing import Any
class Node: 
    """Node class"""
    def __init__(self, x: Any):
        self.val = x
        self.next = None
    
class ListNode:
    """Definition for singly-linked list
    """
    def __init__(self) -> None:
        self.head = None

    