class InsertionSort:
    def __init__(self, list):
        self.list = list
        self.sorting(list)
        
    def sorting(self, list):
        if len(list) <= 1:
            self.list = list
            return
        for index1 in range (1, len(list)):
            key1 = list[index1]
            index2 = index1 - 1
            while index2 > 0 and  list[index2] > key1:
                list[index2 + 1]= list[index2]
                index2 -= 1
            list[index2 + 1] = key1                 
        self.list = list


x = InsertionSort([10,9,8,7,6,5,4,3,2,1])
print(x.list)
                    