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
        # We use a map visited to track if the node is visited
        # When the node is visited 2 time, that is the node tail connect to
        visited: Dict[Node, bool] = dict()
        temp = head

        while(temp):
            if(temp in visited):
                return temp
            else:
                visited[temp] = True
                temp = temp.next
        
        return None
        

def app():
    """Function read input, solve and output"""
    linked_list = Reader().read()

    solution = Solution()
    solution.solve(linked_list.head)

app()
