import sys

sys.path.append("../ll")

from ll import ListNode, Node


class SLinkedListReader:
    """Linked list reader class (build class linkedlist)"""

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
    
