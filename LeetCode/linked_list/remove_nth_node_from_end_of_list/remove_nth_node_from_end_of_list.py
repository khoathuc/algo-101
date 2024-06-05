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
        tmp = head
        pos = 0

        if(n == pos):
            return head.next
        else:
            while(tmp is not None) and pos != n:
                pos = pos+1
                tmp = tmp.next
            
            if(tmp is not None):
                tmp.next = tmp.next.next
        
        def print_ll(node: Node):
            if node is None:
                return 
            print(node.val)
            print_ll(node.next)
        
        print_ll(head)



def app():
    """Function read input, solve and output"""
    global head, n
    Reader().read()

    solution = Solution()
    solution.solve(head.head, n)

app()
