# Constructor
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.pre = None
# Doubbly Linked List
class DDL:
    def __init__(self,value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1

    def print_ddl(self):
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next
    
    # Functions
    
    ## Append function
    def append(self,value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
        self.length += 1
        return True

    ## pop function
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.pre
            self.tail.next = None
            temp.pre = None
        self.length -= 1
        return temp
    
    ## Prepand function 
    def prepand(self,value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node 
        self.length += 1
        return True

    ## pop_first function
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.pre = None
            temp.next = None
        self.length -=1
        return temp
    
    ## get method
    def get(self,index):
        if self.length ==0:
            return None
        if index <= self.length/2:
            temp = self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index,-1):
                temp = temp.pre
        return temp
    
    ## set_value function
    def set_value(self,index,value):
        temp = self.get(index)
        if temp != None:
            temp.value = value
            return True
        return False

    ## insert function
    def insert(self,index,value):
        node = Node(value)
        if (index > self.length and index >=0) or (index < -(self.length + 1) and index <0):
            return False
        if index == 0:
            return self.prepand(value)
        if index == self.length:
            return self.append(value)
        if index > 0 and index <= self.length:
           index = index
        if index < 0 and index >= -(self.length):
            index = (self.length + (index +1))
        before = self.get(index-1)
        after = self.get(index)
        node.pre = before
        node.next = after
        before.next = node
        after.pre = node
        self.length += 1
        return True
    
    ## Remove function
    def remove(self,index):
        if (index > self.length and index >=0) or (index < -(self.length + 1) and index <0):
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        temp = self.get(index)

        temp.next.pre = temp.pre
        temp.pre.next = temp.next
        temp.next = None
        temp.pre = None
        self.length -= 1
        return temp
            
        
        

ddl1 = DDL(4)
ddl1.print_ddl()
ddl1.append(5)
print("-----------------")
ddl1.print_ddl()
ddl1.prepand(3)
print("-----------------")
ddl1.print_ddl()
ddl1.pop_first()
print("-----------------")
ddl1.print_ddl()
ddl1.append(6)
ddl1.append(7)
ddl1.append(8)
ddl1.append(9)
ddl1.append(10)
print("-----------------")
ddl1.print_ddl()
print("-----------------")
print(ddl1.get(5).value)
print(ddl1.get(0).value)
print(ddl1.get(1).value)
print(ddl1.get(2).value)
print("-----------------")
ddl1.print_ddl()
print("-----------------")
ddl1.set_value(4,17)
ddl1.print_ddl()
print("-----------------")
ddl1.insert(2,100)
ddl1.print_ddl()
print("-----------------")
ddl1.insert(-3,88)
ddl1.print_ddl()
print("-----------------")
ddl1.remove(5)
ddl1.print_ddl()



