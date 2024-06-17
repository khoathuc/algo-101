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
        pre = Node()
        curr = head
        while(curr):
            post = curr.next
            pre = curr
            
            head = head.next
        
def app():
    """Function read input, solve and output"""
    global linked_list
    Reader().read()
    solution = Solution()
    solution.solve(linked_list.head)


app()
