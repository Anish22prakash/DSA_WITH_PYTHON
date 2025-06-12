class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def reverse(self):
        pass

def reverse(linkedList):
        prev = None
        current = linkedList.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        linkedList.head, linkedList.tail = linkedList.tail, linkedList.head
        return prev

def traversalOfLinkedlist(linkedlist):
    if linkedlist :
        current = linkedlist.head
        while current is not None:
            print(current.value)
            current = current.next


newliskedList = LinkedList()
newliskedList.append(20)
newliskedList.append(30)
reverse(newliskedList)
traversalOfLinkedlist(newliskedList)


        