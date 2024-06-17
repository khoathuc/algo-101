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
        # generate list from linked list then evaluate if list is palindrome
        ll_values = []
        while head:
            ll_values.append(head.val)
            head = head.next
        
        def check_palindrome(list: List[int])->bool:
            l = 0
            r = len(list) - 1
            
            while(l < r):
                if(list[l]!= list[r]):
                    return False
                l += 1
                r -= 1
            return True
        
        return check_palindrome(ll_values)
        
def app():
    """Function read input, solve and output"""
    global linked_list
    Reader().read()
    solution = Solution()
    solution.solve(linked_list.head)


app()
