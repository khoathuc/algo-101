from typing import Any, Optional
class Node: 
    """Node class"""
    def __init__(self, x: Any):
        self.val = x
        self.next: Optional[Node] = None
    

class ListNode:
    """Definition for singly-linked list
    """
    def __init__(self) -> None:
        self.head: Node = None


    #INSERT
    def insert_at_begin(self, data):
        """insert at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_at_index(self, data, index):
        """insert at the index of the list"""
        new_node = Node(data)
        pos = 0

        if(index == pos):
            self.insert_at_begin(data)
        else:
            temp = self.head
            while(temp):
                if(pos == index):
                    new_node.next = temp.next
                    temp.next = new_node
                    break
                else:
                    temp = temp.next
                    pos += 1


    def insert_at_end(self, data):
        """insert at the end of the list"""
        new_node = Node(data)
        temp = self.head
        
        if(temp is None):
            self.head = new_node
            return 
        
        while(temp.next):
            temp = temp.next
        
        temp.next = new_node

    #UPDATE
    def update_node(self, data, index):
        "update node in the list"
        temp = self.head
        pos = 0

        if(index == pos):
            temp.val = data
        else:
            while(temp):
                if(pos == index):
                    temp.val = data
                    break
                else:
                    temp = temp.next
                    pos += 1
    

    #DELETE
    def delete_at_begin(self):
        """delete at the beginning of the list"""
        if(self.head is None):
            return
        self.head = self.head.next

    
    def delete_at_index(self, index):
        """delete node at index"""
        temp = self.head
        pos = 0

        if(index == pos):
            self.delete_at_begin()
        else:
            while(temp != None and pos != index):
                pos = pos+1
                temp = temp.next
 
            if temp != None:
                temp.next = temp.next.next

    # GET
    def get_at_index(self, index):
        """get node at index"""
        temp = self.head
        pos = 0

        if(index == pos):
            return temp
        else:
            while(temp != None and pos != index):
                pos = pos+1
                temp = temp.next
            if temp is not None:
                temp.next = temp.next.next

        return temp
    
    def get_at_end(self):
        """get tail of the list"""
        temp = self.head
        if(temp is None):
            return 
        
        while(temp.next):
            temp = temp.next
        
        return temp
    
    def print_ll(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next
    

    def has_cycle(self):
        """check if the list has cycle"""
        """using floyd's algorithm"""
        fast_ptr = self.head
        slow_ptr = self.head
        while(fast_ptr and fast_ptr.next):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            if(fast_ptr == slow_ptr):
                return True
        return False