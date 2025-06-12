# Delete a Node from a Circular Singly Linked List
# Implement a method in the CircularLinkedList class to delete a node by value.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def delete_by_value(self, value):
        if self.head.value == value:
            self.head = self.head.next
            self.tail.next = self.head
        else : 
            temp = self.head.next
            prev = self.head
            while temp:
                if temp.value == value:
                    prev.next = temp.next
                    temp.next = None
                temp = temp.next
                prev = prev.next

newLinkedList = CSLinkedList()
newLinkedList.append(1)
newLinkedList.append(2)
newLinkedList.append(3)
newLinkedList.append(4)
newLinkedList.append(5)
newLinkedList.append(6)
newLinkedList.delete_by_value(3)
newLinkedList.delete_by_value(4)
newLinkedList.delete_by_value(1)
newLinkedList.delete_by_value(6)
print(newLinkedList.__str__())

