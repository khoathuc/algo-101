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
global linked_list
"""Reader class"""


class Reader(LinkedListReader):
    def read(self):
        global linked_list
        with open("input.txt", "r") as f:

            """Set variables"""
            # read list
            input_data = f.readline()
            linked_list_data = [int(data) for data in input_data.split(" ")]
            linked_list = LinkedListReader().build_linked_list_w_values(
                linked_list_data
            )


class Solution:
    """
    Class Solution
    We'll solve problems here
    """

    def solve(self, head: Optional[Node]):
        # solve here
        # create dummy node for swap head
        super_head = Node(0, head)

        curr = super_head
        while curr:
            if (curr.next is None) or (curr.next.next is None):
                break
            else:
                tmp = curr.next

                curr.next = tmp.next
                tmp.next = curr.next.next
                curr.next.next = tmp

                curr = curr.next.next

        return super_head.next
def app():
    """Function read input, solve and output"""
    global linked_list
    Reader().read()
    solution = Solution()
    solution.solve(linked_list.head)


app()
