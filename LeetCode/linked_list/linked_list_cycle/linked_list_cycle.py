"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/linked-list-cycle

"""Import required"""
import sys

sys.path.append("..")
from LeetCode.linked_list.s_reader import LinkedListReader
from typing import Optional
from ll import ListNode, Node

"""Define global variables"""

"""Reader class"""


class Reader(LinkedListReader):
    @classmethod
    def read(cls):
        with open("input.txt", "r") as f:
            input_data = f.readline()

            """Set variables"""
            cls.values = [int(data) for data in input_data.split(" ")]
            pos = int(f.readline())

        super().build_linked_list()
        if(pos):
            tail = cls.linked_list.get_at_end()
            pos_node = cls.linked_list.get_at_index(pos)
            tail.next = pos_node
        
        return cls.linked_list


class Solution:
    """
    Class Solution
    We'll solve problems here
    """

    def solve(self, head: Optional[Node]):
        # solve here
        # We use Floyd's algorithm
        fast_ptr = head
        slow_ptr = head
        while(fast_ptr and fast_ptr.next):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if(fast_ptr == slow_ptr):
                return True
            
        return False

def app():
    """Function read input, solve and output"""
    linked_list = Reader().read()

    solution = Solution()
    solution.solve(linked_list.head)

app()
