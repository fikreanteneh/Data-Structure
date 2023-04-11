def bubble(list):
    c = 0
    if len(list) == 1:
        return list
    for i in range(len(list) - 1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                c += 1
    print("Array is sorted in", c, "swaps.")
    print("First Element:", list[0])
    print("Last Element:", list[-1])
    return list
print(bubble([3,2,1]))
