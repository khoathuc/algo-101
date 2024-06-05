"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/linked-list-cycle

"""Import required"""
import sys

sys.path.append("..")
from reader import LinkedListReader
from typing import Dict, Optional
from ll import ListNode, Node

"""Define global variables"""
global head, n
"""Reader class"""


class Reader(LinkedListReader):
    def read(self):
        global head, n
        with open("input.txt", "r") as f:

            """Set variables"""
            #read list
            input_data = f.readline()
            head_data = [int(data) for data in input_data.split(" ")]
            head = LinkedListReader().build_linked_list_w_values(head_data)

            #read n
            n = int(f.readline())


class Solution:
    """
    Class Solution
    We'll solve problems here
    """

    def solve(self, head: Optional[Node], n:int):
        # solve here
        if head is None:
            return head
        
        # add new node to head of the list to prevent None case of pre_pointer
        node = Node(0, head)
        # maintain 2 pointers that delay n steps
        pre_ptr = node
        after_ptr = node

        # make pre_ptr is delayed n+1 steps
        pos = 0
        while(pos < n + 1):
            if(after_ptr is None):
                return head
            after_ptr = after_ptr.next
            pos += 1
        
        # move 2 ptr toward tail of list
        while(after_ptr):
            pre_ptr = pre_ptr.next
            after_ptr = after_ptr.next

        pre_ptr.next = pre_ptr.next.next

        return node.next


def app():
    """Function read input, solve and output"""
    global head, n
    Reader().read()

    solution = Solution()
    solution.solve(head.head, n)

app()
