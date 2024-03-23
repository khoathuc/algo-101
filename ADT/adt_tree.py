from tree import Tree
from node import Node

def initTree():
    for node_label in node_labels:
        node = Node(node_label)
        tree.addNode(node)
    
    for key in node_childs:
        node = tree.getNode(key)
        node_children = tree.getNode(node_childs[key])
        for i in range (0, len(node_children)):
            node_child = tree.getNode(node_children[i])
            right_sibling = tree.getNode(node_children[i + 1])

            if(isinstance(node, Node)):
                tree.updateNode(node_child, node, right_sibling)
            


def read():
    with open('input.txt', 'r') as f:
        while True:
            cur_line = f.readline()
            node_data = cur_line.split()

            if(len(cur_line) == 0):
                break
            else:
                node_label = node_data[0]
                node_labels.append(node_label)

                node_child_list = node_data[1:-1]
                node_childs[node_label] = node_child_list

def app():
    global tree 
    global node_labels
    global node_childs

    node_labels = []
    node_childs = dict()
    tree = Tree()
    read()
    initTree()

app()