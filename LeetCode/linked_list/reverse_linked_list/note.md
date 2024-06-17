# use stack to store the list of node
```python
	def solve(self, head: Optional[Node]):
        # solve here
        stack_nodes = []
        while(head):
            stack_nodes.append(head)
            head = head.next

        super_head = Node()
        curr = super_head
        while(len(stack_nodes) != 0):
            curr.next = stack_nodes.pop()
            curr = curr.next
            curr.next = None

        return super_head.next
```

# use two pointers and iterate
