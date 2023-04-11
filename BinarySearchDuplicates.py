
def BinarySearch(n, values, key):
    left, right = 0, n-1
    while left <= right:
        mid = left + ((right - left) // 2)
        if values[mid] == key:
            if mid == 0 or values[mid - 1] != key:
                return mid
            right = mid - 1
        elif values[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    return -1


n = 7
values = [2, 4, 4, 4, 7, 7, 9]
m = 4
keys = [9, 4, 5, 2]
for i in range(m):
    print(BinarySearch(n, values, keys[i]))


# def BBinarySearch(n, values, key, left=0, right=n - 1):
#     left, right = 0, n-1
#     while left <= right:
#         mid = left + ((right - left) // 2)
#         if values[mid] == key:
#             # if mid > 0 and values[mid - 1] != key:
#             return mid
#             rigth = mid
#         elif values[mid] > key:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1
