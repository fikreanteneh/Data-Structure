from gettext import npgettext
from hashlib import new


class Node:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def topFront(self):
        if self.head is None:
            return None
        return self.head.value

    def topBack(self):
        if self.tail is None:
            return None
        return self.tail.value

    def pushFront(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return
        new = Node(value, None, self.head)
        self.head.prev = new
        self.head = new
    
    def pushBack(self, value):
        if self.tail is None:
            self.tail = Node(value)
            self.head = self.tail
            return
        new = Node(value, self.tail, None)
        self.tail.next =  new
        self.tail = new

    def popFront(self):
        key = self.topFront()
        if self.head.next is None:
            self.tail,self.head = None,None
            return key
        self.head = self.head.next
        self.head.prev = None
        return key
    
    def popBack(self):
        key = self.topBack()
        if self.tail.prev is None:
            self.tail,self.head = None,None
            return key
        self.tail = self.tail.prev
        self.tail.next = None
        return key

    def find(self, value):
        newHead = self.head
        while newHead is not  None:
            if newHead.value == value:
                return True
            newHead = newHead.next
        return False

    def isEmpty(self):
        if self.head == None :
            return True
        return False
            
    def addBefore(self, node, value):
        newHead = self.head
        if self.head is None:
            raise Exception("The Node does not exist")
        elif newHead.value == node:
            self.head = Node (value,None,self.head)
            return
        while newHead.next.value != node:
            if newHead.next.value is None:
                raise Exception("The Node does not exist")
            newHead = newHead.next  
        new = Node(value, newHead, newHead.next)
        newHead.next = new
        
    def list(self, i = -1):
        list = []
        new = self.head
        while new:
            list.append(new.value)
            new = new.next
        return list

    def sortList(self):
        #using list
        list = self.list()
        list.sort()
        self.head, self.tail = None, None
        for i in list:
            self.pushBack(i)

        #by creating linked list
        """if self.head is None:
            return
        old = self.head.next
        self.head = Node(self.head.value)
        self.tail = self.head
        while old:
            new = self.head
            while new:
                if old.value <= new.value:
                    key = Node(old.value, new.prev, new)
                    if new.prev is None:
                        self.head = key
                    else:
                        new.prev.next = key
                    break
                elif new.next is None:
                    #print(self.head.value,self.tail.value)
                    key = Node(old.value, new, None)
                    new.next = key
                    self.tail = key
                    break
                new = new.next
            old = old.next"""
            

x = LinkedList()
x.pushFront(4)

x.pushFront(4)
x.pushFront(2)
x.pushFront(1)

x.pushFront(-1)
x.pushBack(100)
x.pushBack(200)
x.addBefore(4,-1)
print(x.list())
x.sortList()
print(x.list())
