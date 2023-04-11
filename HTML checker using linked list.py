class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, value):
        self.head = Node (value, self.head)
        if self.head.next is None:
            self.tail = self.head
    def pushBack(self, value):
        if self.head is None :
            self.head = Node (value, self.head)
            self.tail = self.head
            return
        newHead = Node(value, None)
        self.tail.next = newHead
        self.tail = newHead

    def topFront(self):
        if self.head is None:
            return None
        return self.head.value

    def topBack(self):
        if self.tail is None:
            return None
        return self.tail.value

    def popFront(self):
        key = self.topFront()
        if self.head is not None:
            self.head = self.head.next
        return key

    def popBack(self):
        key = self.topBack()
        if self.head is None or self.head.next is None:
            self.head, self.tail = None, None
            return key
        newHead = self.head
        newTail = self.head.next
        while newTail.next:
            newHead = newHead.next
            newTail = newTail.next
        self.tail = newHead
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

    def erase(self, key):
        if self.head is None or self.head.value == key:
            self.head, self.tail = None, None
            return
        newHead = self.head
        newTail = newHead.next
        while newTail:
            if newTail.value == key:
                newHead.next = newTail.next
            newHead, newTail = newHead.next, newTail.next
        self.tail = newHead
            
    def addBefore(self, node, value):
        newHead = self.head
        if self.head is None:
            raise Exception("The Node does not exist")
        elif newHead.value == node:
            self.head = Node (value,self.head)
            return
        while newHead.next.value != node:
            if newHead.next.value is None:
                raise Exception("The Node does not exist")
            newHead = newHead.next  
        new = Node(value,newHead.next)
        newHead.next = new
        
    def list(self):
        list = []
        new = self.head
        while new:
            list.append(new.value)
            new = new.next
        return list

    def sortList(self):
        if self.head is None:
            return
        new = self.head.next
        self.head = Node(self.head.value)
        self.tail = self.head
        while new:
            sorted = self.head
            sorted2 = self.head.next
            if new.value <= self.head.value :
                self.head = Node (new.value, self.head)
            else:
                while sorted:
                    if sorted.next is None:
                        key = Node(new.value)
                        sorted.next = key
                        self.tail = key
                        break
                    elif new.value <= sorted2.value:
                        key = Node(new.value,sorted)
                        sorted.next = key
                        break
                    sorted = sorted.next
                    sorted2 = sorted2.next
            new = new.next

class Stack:
    def __init__(self, size, type):
        self.__stack__ = LinkedList()
        
    def isEmpty(self):
        return self.__stack__.empty()
        
    def s_push(self, value):
        self.__stack__.pushFront(value)
 
    def s_pop(self):
        return self.__stack__.popFront()
        
    def length(self):
        return self.__stack__.size()
        
    def peek(self):
        return self.__stack__.topFront()

class Checker:
    def __init__(self, value):
        with open(value, "r") as file:
            self.lines = file.readlines()            
        self.__checkerStack__ = Stack(len(self.lines) * 4, str)
        self.validate()
    def validate(self):
        tags = ''
        record  = False
        emptyElements = ['!doctype', 'area',  'base', 'br','col','embed', 'hr', 'img', 'input', 'link', 'meta', 'param','source', 'track', 'wbr']
        for line in range (len(self.lines)):
            lengthLine = len(self.lines[line])
            for text in range (lengthLine):
                if self.lines[line][text] == '<':
                    record = True

                if record :
                    if self.lines[line][text] != ' ' and self.lines[line][text] != '<' and self.lines[line][text] != '>' and self.lines[line][text] != '\n':
                        tags += self.lines[line][text].lower()
                    if tags == '' or tags[0] == '/':
                        pass
                    elif tags !='' and self.lines[line][text] == ' ':
                         record = False

                if self.lines[line][text] == '>':
                    record = False
                    if tags in emptyElements or tags[:-1] in emptyElements:
                        tags = ''
                        continue
                    elif tags != '' and tags[0] == '/':
                        if tags[1:] == self.__checkerStack__.peek():
                            self.__checkerStack__.s_pop()
                            tags = ''
                            continue
                        raise Exception ("Expected: </" + self.__checkerStack__.peek() + "> tag but Found: <" + tags + "> at line " + str(line+1))
                    self.__checkerStack__.s_push(tags)
                    tags = ''    
                             
        if self.__checkerStack__.isEmpty():
            print('HTML is well structured')
            return
        raise Exception ("Expected: </" + self.__checkerStack__.peek() + "> tag but Found: <" + tags + "> at line " + str(line+1))
y =Checker("index.html")
