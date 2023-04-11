import time
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
            sortedL = self.head
            sorted2 = self.head.next
            if old.value <= self.head.value :
                self.head = Node (old.value, self.head)
            else:
                while sortedL:
                    if sortedL.next is None:
                        key = Node(old.value)
                        sortedL.next = key
                        self.tail = key
                        break
                    elif old.value <= sorted2.value:
                        key = Node(old.value,sorted2)
                        sortedL.next = key
                        break
                    sortedL = sortedL.next
                    sorted2 = sorted2.next
            old = old.next"""

x = LinkedList()

x.pushBack(4)
x.pushBack(4)
x.pushBack(2)
x.pushBack(0)
x.pushBack(1)

x.pushBack(-1)
x.pushBack(4)
x.pushBack(100)
x.pushBack(200)
x.pushBack(4)



a =[5328, 696, 2473, 7304, 8216, 6915, 3306, 2718, 2732, 7683, 4575, 5340, 3336, 3580, 7362, 346, 8811, 2485, 1935, 8732, 819, 1424, 9888, 6800, 5514, 8872, 7183, 1676, 3254, 7848, 129, 4801, 2631, 9405, 1339, 9879, 5804, 1208, 3522, 135, 5053, 5390, 6210, 655, 9840, 3193, 9382, 8009, 3281, 4518, 5381, 5892, 4448, 5482, 6909, 7530, 2457, 6033, 7217, 5173, 7401, 687, 9861, 1913, 5764, 1940, 1019, 3018, 4187, 7119, 826, 4749, 4371, 6168, 2962, 6570, 7037, 8570, 4256, 6405, 1212, 6287, 732, 4839, 1338, 7002, 2264, 8192, 6956, 7195, 9582, 6178, 8723, 6115, 5261, 4013, 5953, 263, 3715, 4538]*100
for i in a:
    x.pushBack(i)
start = time.time()
x.sortList()
end = time.time()
print(end - start)
print(x.list())




            
                
