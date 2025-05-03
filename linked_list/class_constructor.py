class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


new_node = Node(5)
new_node2 = Node(7)
new_node2.next = new_node
