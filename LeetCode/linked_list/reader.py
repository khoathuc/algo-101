import sys

sys.path.append("../ll")

from ll import ListNode, Node


class LinkedListReader:
    """Linked list reader class """

    def build_linked_list_w_values(self, values):
        linked_list = ListNode()
        if(values is None):
            return linked_list
        
        for(i, value) in enumerate(values):
            linked_list.insert_at_end(value)

        return linked_list
    
