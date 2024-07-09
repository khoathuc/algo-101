"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/linked-list-cycle

"""Import required"""
import sys

sys.path.append("..")
from reader import LinkedListReader
from typing import List, Optional
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
        stack_nodes: List[Node] = []
        while(head):
            stack_nodes.append(head)
            head = head.next
        
        super_head = Node()
        curr = super_head
        while(len(stack_nodes) != 0):
            curr.next = stack_nodes.pop()
            curr = curr.next
            #reset next node of current node
            curr.next = None

        def print_ll(node: Node):
            if node is None:
                return 

            print(node.val)
            print_ll(node.next)

        print_ll(super_head.next)
                
def app():
    """Function read input, solve and output"""
    global linked_list
    Reader().read()
    solution = Solution()
    solution.solve(linked_list.head)


app()
