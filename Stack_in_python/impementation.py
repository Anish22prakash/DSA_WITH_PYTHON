class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self):
        return self.list == []
    
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    def push(self,values):
        if self.isFull():
            return "Stack is full"
        else :
            self.list.append(values)
            return f"element is added in the stack , value {values}"
    
    def pop(self):
        if self.isEmpty():
            return "there is not any element in the stack"
        else :
            return self.list.pop()
    

customStack = Stack(5)
print(customStack.push(1))
print(customStack.push(2))
print(customStack.push(3))
print(customStack.push(4))
print(customStack.push(5))
print(customStack.push(6))
print(f"stack is full : {customStack.isFull()}")
print(customStack.pop())
print(f"stack is full : f{customStack.isFull()}")
print(customStack)

