class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        new_node = Node(value)
        if self.head != None or self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        self.length += 1
    
    def insert(self,value):
        new_node = Node(value)
        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def __str__(self):
        current = self.head
        result = ''
        while current != None:
            result +=  str(current.value)
            if current.next != None:
             result += ' -> '
            current = current.next
        return result

newlinkedlist = Linkedlist()
newlinkedlist.append(10)
newlinkedlist.append(20)
newlinkedlist.append(50)
newlinkedlist.append(60)
newlinkedlist.append(70)
newlinkedlist.append(30)
newlinkedlist.insert(5)

# print(newlinkedlist.__str__())


def traversalOfLinkedlist(linkedlist):
    if linkedlist :
        current = linkedlist.head
        while current is not None:
            print(current.value)
            current = current.next

# traversalOfLinkedlist(newlinkedlist)

def searchInLinkedList(linkedlist,value):
    current = linkedlist.head
    while current is not None:
        if current.value == value:
            return True
        current = current.next
    return False

# print(searchInLinkedList(newlinkedlist,60))

def getValueByIndex(linkedlist,index):
    current = linkedlist.head
    if linkedlist.head is None or index < 0:
        return None
    for _ in range(index):
        current = current.next
    return current

# print(getValueByIndex(newlinkedlist,0).value)

def setValueByIndex(linkedlist,index,value):
    current = linkedlist.head
    if linkedlist.head is None or index < 0 or index >= linkedlist.length:
        return None
    for _ in range(index):
        current = current.next
    current.value = value
    return linkedlist

# traversalOfLinkedlist(setValueByIndex(newlinkedlist,0,99))

def pop_first_element(linkedlist):
    temp = linkedlist.head
    if temp and temp.next is None:
        linkedlist.head = None
        linkedlist.tail = None
        linkedlist.length -= 1
        return linkedlist
    elif  temp is None:
        return None
    else:
        linkedlist.head = temp.next
        linkedlist.length -= 1
        return linkedlist
    
traversalOfLinkedlist(pop_first_element(newlinkedlist))
print(f"now the length of linkedlist {newlinkedlist.length}")
