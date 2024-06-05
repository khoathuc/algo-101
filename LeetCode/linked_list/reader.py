import sys

sys.path.append("../ll")

from ll import ListNode, Node


class LinkedListReader:
    """Linked list reader class"""

    @classmethod
    def read_input(cls):
        with open("input.txt", "r") as file:
            input_data = file.read().strip()
        
        values = input_data.split(" ")

        for(i, value) in enumerate(values):
            if value.lower() == "null":
                values[i] = None
            else:
                values[i] = int(value)
        
        cls.values = values


    @classmethod
    def build_linked_list(cls):
        cls.linked_list = ListNode()
        if(cls.values is None):
            return cls.linked_list
        
        values = cls.values
        for(i, value) in enumerate(values):
            cls.linked_list.insert_at_end(value)

    def build_linked_list_w_values(self, values):
        linked_list = ListNode()
        if(values is None):
            return linked_list
        
        for(i, value) in enumerate(values):
            linked_list.insert_at_end(value)

        return linked_list