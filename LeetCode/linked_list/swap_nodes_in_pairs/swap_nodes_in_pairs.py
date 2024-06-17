"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/swap-nodes-in-pairs

"""Import required"""
import sys

sys.path.append("..")
from reader import LinkedListReader
from typing import Dict, Optional
from ll import ListNode, Node

"""Define global variables"""
global linkedlist
"""Reader class"""


class Reader(LinkedListReader):
    def read(self):
        global linkedlist
        with open("input.txt", "r") as f:
            """Set variables"""
            #read list
            input_data = f.readline()
            linked_list_data = [int(data) for data in input_data.split(" ")]
            linkedlist = LinkedListReader().build_linked_list_w_values(linked_list_data)


class Solution:
    """
    Class Solution
    We'll solve problems here
    """

    def solve(self, head: Optional[Node]):
        # solve here
        super_head = Node()
        super_head.next = head

        curr = super_head
        while curr and curr.next and curr.next.next:
            curr_2 = curr.next.next
            curr_1 = curr.next

            curr.next = curr_2
            curr.next.next = curr_1
            curr.next.next.next = curr_2.next
            
            if(curr.next.next):
                curr = curr.next.next
                print(curr.val)

        print(curr.val)
        pass


def app():
    """Function read input, solve and output"""
    global linkedlist
    Reader().read()

    linkedlist.print_ll()
    solution = Solution()
    solution.solve(linkedlist.head)

app()
