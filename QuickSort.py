class QuickSort:
    def __init__ (self,list):
        self.list = self.quick(list)
    def quick(self,list):
        if len(list) == 1:
            return list
        pindex = len(list)//2
        pivot = list[pindex]
        index1, index2 = 0, len(list)-1
        while index1 < index2:
            if list[index1] > pivot:
                while list[index2] > pivot:
                    index2 -= 1
                list[index1], list[index2] == list[index2], list[index1]
            index1 += 1
        return self.quick(list[:pindex]) + self.quick(list[pindex:])
x = QuickSort([21,25,7,10,13,56,15])
print(x.list)