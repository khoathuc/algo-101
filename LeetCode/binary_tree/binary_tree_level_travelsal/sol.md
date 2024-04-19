### SOL 1:


Setting up 2 lists.

- res: List[List[int]]: result - each element in list is a list of node value in same level
- node_queue: Queue[List[TreeNode]]: queue that store nodes in next level


1. get next level node in node_queue => **tmp_nodes**
2. set up 2 list: 
    - level: list of node's values in same level
    - queue: list of next node level
3. iterate through **tmp_nodes**, then:
    - append node value in level
    - append node children in queue
4. after iterate through all **tmp_nodes**, we then have the list of node in that level.
5. continuosly until node_queue have no list => no level available.