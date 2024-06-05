"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/add-two-numbers

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

    def solve(self, l1: Optional[Node], l2: Optional[Node]):
        # solve here
        sum_ll = Node()
        carry = 0
        tmp_digit = sum_ll

        curr1 = l1
        curr2 = l2
        while curr1 or curr2:
            dig1 = curr1.val if curr1 else 0
            dig2 = curr2.val if curr2 else 0

            tmp_digit.next = Node()
            tmp_digit.next.val = (dig1 + dig2 + carry)%10

            carry = (dig1 + dig2 + carry)//10

            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            tmp_digit = tmp_digit.next
        
        if(carry):
            tmp_digit.next = Node()
            tmp_digit.next.val = carry

        return sum_ll.next  
def app():
    """Function read input, solve and output"""
    Reader().read()

    solution = Solution()
    solution.solve(list1.head, list2.head)

app()
