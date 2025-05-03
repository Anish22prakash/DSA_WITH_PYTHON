class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.Head = None
        self.Tail = None
        self.Length = 0

    def __str__(self):
        temp_node = self.Head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
# insertation at the end of the linkedlist
    def append(self,value):
        new_node = Node(value)
        if self.Head is None:
            self.Head = new_node
            self.Tail = new_node
        else:
            self.Tail.next = new_node
            self.Tail = new_node
        self.Length += 1
# insertation at the beginning of the linkedlist
    def prepend(self,value):
        new_node = Node(value)
        if self.Head is None:
            self.Head = new_node
            self.Tail = new_node
        else:
            new_node.next = self.Head
            self.Head = new_node


newlinkedList = LinkedList()
newlinkedList.append(10)
newlinkedList.append(20)
newlinkedList.append(30)
print(newlinkedList)
newlinkedList.prepend(7)
print(newlinkedList)