class Array:
    
    def __init__(self, size, type):
        self.size = size
        self.type = type
        self.__array__= [None] * self.size
        self.count = 0
    def isFull(self):
        if self.count == self.size:
            return True
        return False
    def array(self, index = - 1):
        if index == -1 :
            return self.__array__
        return self.__array__[index]

    def checkArguments(self,value,index): 
        if not isinstance(value, self.type):
            raise Exception ('Invalid input type for value')
        if not (0 <= index <= self.size) :
            raise Exception ('Index is out of bound')
        return True

    def insert(self, value, index):
        if not self.checkArguments(value, index):
            return
        if self.__array__[self.size - 1] is not None:
            raise Exception ('Array is full')
        if index != 0 and self.__array__[index - 1] is None :
            raise Exception ('Enter the correct index')
        key = self.__array__[index]
        self.__array__[index] = value
        while key is not None and index < self.size - 1 :
            index += 1
            key2 = self.__array__[index]
            self.__array__[index] = key
            key = key2
        self.count += 1

    def  replace(self,value,index):
        if not self.checkArguments(value,index):
            return
        self.__array__[index] = value

    def delete(self, index):
        if not (0 <= index < self.size):
            raise Exception ('Wrong index')
            return
        self.__array__[index] = None
        key = 0
        while  key is not None and index < self.size - 1:
            index += 1  
            key = self.__array__[index]
            self.__array__[index - 1] = key
            self.__array__[index] = None
        self.count -= 1

    def append(self,value):
        index = self.length()
        self.insert(value, index)
        self.count += 1   

    def reverse(self):
        temp = []
        for i in range(self.size-1,-1,-1):
            temp.append(self.__array__[i])
        self.__array__ = temp

    def length(self):
        return self.count


class Stack:
    def __init__(self, size, type):
        self.__stack__ = Array(size, type)
        self.index = 0
        self.size = size
    def isEmpty(self):
        if self.index == 0:
            return True
        return False
    def isFull(self):
        if self.index == self.size:
            return True
        return False
    def stack(self):
        return self.__stack__.array()
    def s_push(self, value):
        self.__stack__.insert(value, self.index)
        if self.index < self.size:
            self.index += 1
    def s_pop(self):
        if self.index == 0:
            return None
        key = self.__stack__.array()[self.index-1]
        self.__stack__.delete(self.index-1)
        self.index -= 1
        return key
    def Length(self):
        return self.index
    def top(self):
        return self.index - 1
    def peek(self):
        return self.__stack__.array()[self.top()]

class Checker:
    def __init__(self, value):
        with open(value, "r") as file:
            self.lines = file.readlines()            
        self.__checkerStack__ = Stack(len(self.lines) * 4, tuple)
        self.validate()
    def validate(self):
        tag = ''
        record  = False
        emptyTags = ['!doctype', 'br', 'area', 'base','meta','col','embed', 'hr','img','link','source','wbr', 'param','input', 'track']
        for line in range (len(self.lines)):
            lengthLine = len(self.lines[line])
            for text in range (lengthLine):
                if self.lines[line][text] == '<':
                    record = True
                if record :
                    if self.lines[line][text] != ' ' and self.lines[line][text] != '<' and self.lines[line][text] != '>':
                        tag += self.lines[line][text].lower()
                    if tag !='' and self.lines[line][text] == ' ':
                         record = False
                if self.lines[line][text] == '>':
                    record = False
                    if tag in emptyTags :
                        tag = ''
                        continue
                    elif tag[0] == '/':
                        if tag[1:] == self.__checkerStack__.peek()[0]:
                            self.__checkerStack__.s_pop()
                            tag = ''
                            continue
                        raise Exception ('the TAG "',self.__checkerStack__.peek()[0], '" at line',self.__checkerStack__.peek()[1], 'did not closed at line',line + 1)
                    self.__checkerStack__.s_push((tag, line))
                    tag = ''             
        if self.__checkerStack__.isEmpty():
            print('Valid HTML')
            return
        raise Exception ('the TAG "',self.__checkerStack__.peek()[0], '" at line',self.__checkerStack__.peek()[1], 'did not closed at',line + 1)
x = Checker('index.html')
                    



