class Merge:
    def __init__(self,arr):
        self.list = arr
        self.sorted = self.sorting(self.list)

    def merge(self,l1,l2):
        i1,i2 = 0, 0
        merged = []
        while i1 < len(l1) and i2 < len(l2):        
            if l1[i1] == l2[i2]:
                merged.append(l1[i1])
                merged.append(l2[i2])
                i1,i2 = i1+1, i2+1  
            elif l1[i1] < l2[i2]:
                merged.append(l1[i1])
                i1 += 1
            elif l1[i1] > l2[i2]:
                merged.append(l2[i2])
                i2 += 1
        merged = merged + l1[i1:]
        merged = merged + l2[i2:]
        return merged

    def sorting(self, list):
        if len(list) == 1:
            return list
        return self.merge(self.sorting(list[:len(list)//2]), self.sorting(list[len(list)//2:]))

x = Merge([100,10])
print(x.sorted)
