from node import Node

# read input
input_nodes = []

def initNode(node_data):
    root = Node(node_data[0])

    for i in range(1, len(node_data)):
        child_node = Node(node_data[i])
        root.addNode(child_node)

    input_nodes.append(root)
    return root

def readFlat():
    with open('input_tree.txt', 'r') as f:
        while True:
            cur_line = f.readline()

            node_data = cur_line.split()
            if(len(cur_line) == 0):
                break
            else:
                initNode(node_data)
                
def printOut():
    for node in input_nodes:
        print(node.__repr__() + '\n')


readFlat()
printOut()