class Node:
    """Class for creating a Node for every node creation step we can use it directly:"""
    def __init__(self,value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self,value):
        new_node = Node(value)
        self.head=new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
            self.length =1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1
        return True
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepand(self,value):
        if self.length == 0:
            node = Node(value)
            self.head = node
            self.tail = node 
            self.length += 1
        else:
            node = Node(value)
            node.next = self.head
            self.head= node
            self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0 :
            return None
        pre = self.head
        self.head = self.head.next
        pre.next = None
        self.length -=1
        if self.length ==0:
            self.tail = None
        return pre
    def get(self,index):
        temp  = self.head
        if self.length == 0 or self.length <= index or index < 0:
            return None
        for _ in range(index):
            temp = temp.next
        return (temp)
    # def set_value(self,index,value):
    #     temp = self.head
    #     if self.length == 0 or self.length <= index or index<0:
    #         return "Invalide value"
    #     for _ in range(index):
    #         temp = temp.next
    #     temp.value = value
    #     return True
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    def insert(self,index,value):
        node = Node(value)
        if self.length < index or index < 0:
            return False
        if index ==0:
            return self.prepand(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index-1)
        node.next = temp.next
        temp.next = node
        self.length +=1
        return True
    def remove(self,index):
        if self.length < index or index < 0:
            return None
        if index ==0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        



my_linked_list = Linked_list(4)
my_linked_list.append(5)
print(my_linked_list.print_list()) 
my_linked_list.pop()
print(my_linked_list.print_list())
my_linked_list.prepand(7)
print(my_linked_list.print_list())
my_linked_list.pop_first()
print(my_linked_list.print_list())
my_linked_list.prepand(1)
my_linked_list.append(7)
my_linked_list.append(9)
print(my_linked_list.print_list())
#print(my_linked_list.get(1))
print(my_linked_list.set_value(2,12))
print(my_linked_list.print_list())
my_linked_list.insert(1,1)
my_linked_list.print_list()