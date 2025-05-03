class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList having only one element
class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.Head = new_node
        self.Tail = new_node
        self.length =  1
class EmplyLinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None

new_linkedList  = LinkedList(10)
print(new_linkedList.Head.value)
print(new_linkedList.length)