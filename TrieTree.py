from copy import copy
from operator import ne


class Node:

    def __init__(self):
        self.child = [None]*95
        self.end = False

class TrieTree:

    def __init__(self):
        self.root = Node()
        
    def add(self,value):
        new = self.root
        length = len(value)
        for i in range (length):
            index = ord(value[i])-32
            if new.child[index] is None:
                new.child[index] = Node()
            new = new.child[index]
        if new.end:
            raise Exception("Already exists")
        new.end = True

    def delete(self, value):
        new = self.root
        length = len(value)
        for i in range (length):
            index = ord(value[i])-32
            if new.child[index] is None:
                raise Exception("It does not exist")
            new = new.child[index]
        new.end = False

    def search(self, value):
        new = self.root
        length = len(value)
        for i in range (length):
            index = ord(value[i]) - 32
            if new.child[index] is None:
                return False
            new = new.child[index]
        return new.end

    def related(self, value):
        new = self.root
        length = len(value)
        li = []
        for i in range (length):
            index = ord(value[i]) - 32
            if new.child[index] is None:
                return li
            new = new.child[index]
        if new.end:
            li = [value]
        return li + self.show(value, new.child, [])

    def show(self, string = '', new = 0, list = []):
        if new == 0:
            new = self.root.child
        length = 95
        for i in range(length):
            if new[i] is None:
                continue
            word = string + chr(i+32)
            if new[i].end:
                list.append(word)
            child = new[i].child
            self.show(word, child, list)
        return list

        
    

x = TrieTree()
x.add("bebi")
x.add("abebe")
x.add("kebede")
x.add("the")
x.add("their")
x.add("theirs playing")
x.add("lion")
x.add("lioness")
x.add("zebra")
x.add("giraffe")
x.add("tiger")
print(x.show())
print(x.related("t"))


        


        


        
