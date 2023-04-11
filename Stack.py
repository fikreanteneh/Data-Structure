class Array:
    def __init__(self, size, type):
        self.size = size
        self.type = type
        self.__array__= [None] * self.size
    def array(self, index = - 1):
        if index == -1 :
            return self.__array__
        return self.__array__[index - 1]
    def checkArguments(self,value,index): 
        if not isinstance(value, self.type):
            print('Invalid input type for value')
            return False
        if not (0 <= index <= self.size) :
            print ('Index is out of bound')
            return  False
        return True
    def insert(self, value, index):
        if not self.checkArguments(value, index):
            return
        if self.__array__[self.size - 1] is not None:
            print('Array is full')
            return
        if index != 0 and self.__array__[index - 1] is None :
            print('Enter the correct index')
            return
        key = self.__array__[index]
        self.__array__[index] = value
        while key is not None and index < self.size - 1 :
            index += 1
            key2 = self.__array__[index]
            self.__array__[index] = key
            key = key2
    def  replace(self,value,index):
        if not self.checkArguments(value,index):
            return
        self.__array__[index] = value
    def delete(self, index):
        if not (0 <= index < self.size):
            print('Wrong index')
            return
        self.__array__[index] = None
        key = 0
        while  key is not None and index < self.size - 1:
            index += 1  
            key = self.__array__[index]
            self.__array__[index - 1] = key
            self.__array__[index] = None
    def append(self,value):
        index = self.length()
        self.insert(value, index)       
    def reverse(self):
        temp = []
        for i in range(self.size-1,-1,-1):
            temp.append(self.__array__[i])
        self.__array__ = temp
    def length(self):
        for i in range(self.size):
            if self.__array__[i] == None:
                return i
        return self.size

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