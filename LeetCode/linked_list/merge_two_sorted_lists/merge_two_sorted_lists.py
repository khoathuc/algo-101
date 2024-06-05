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
global list1, list2
"""Reader class"""


class Reader(LinkedListReader):
    def read(self):
        global list1, list2
        with open("input.txt", "r") as f:

            """Set variables"""
            #read list1
            input_data = f.readline()
            list1_data = [int(data) for data in input_data.split(" ")]
            list1 = LinkedListReader().build_linked_list_w_values(list1_data)
            #read list2
            input_data = f.readline()
            list2_data = [int(data) for data in input_data.split(" ")]
            list2 = LinkedListReader().build_linked_list_w_values(list2_data)

        


class Solution:
    """
    Class Solution
    We'll solve problems here
    """

    def solve(self, list1: Optional[Node], list2: Optional[Node]):
        # solve here
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        curr1 = list1
        curr2 = list2

        head = Node()
        tmp = head
        while curr1 or curr2:
            if curr1 is None:
                tmp.next = curr2
                break
            elif curr2 is None:
                tmp.next = curr1
                break
            else:
                if curr1.val < curr2.val:
                    tmp.next = curr1
                    curr1 = curr1.next
                else:
                    tmp.next = curr2
                    curr2 = curr2.next
    
            tmp = tmp.next

        return head.next

def app():
    """Function read input, solve and output"""
    Reader().read()

    solution = Solution()
    solution.solve(list1.head, list2.head)

app()
