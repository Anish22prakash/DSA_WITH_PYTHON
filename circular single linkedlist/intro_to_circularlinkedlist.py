class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
     
    def __str__(self):
        if not self.head:
            return "Empty List"

        result = ''
        temp = self.head
        while True:
            result += str(temp.data)
            temp = temp.next
            if temp != self.head:
                result += ' -> '
            else:
                break
        return result + ' -> (back to head)'
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1


newLinkedList = CircularLinkedList()
newLinkedList.append(10)
newLinkedList.append(20)
newLinkedList.append(30)
newLinkedList.append(40)
newLinkedList.append(50)
newLinkedList.prepend(60)
newLinkedList.prepend(70)
print(newLinkedList.__str__())

