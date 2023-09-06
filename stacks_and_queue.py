class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

# Stack Constructure
class stack:
    def __init__(self,value):
        node = Node(value)
        self.top = node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        node = Node(value)
        if self.height == 0:
            self.top = node
        
        else:
            node.next = self.top
            self.top = node
        self.height +=1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        top.next = None
        self.height -=1
        return temp

# queue 
class queue:
    def __init__(self,value):
        node= Node(value)
        self.first = node
        self.last = node
        self.length = 1

    def enqueue(self,value):
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.height += 1
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

