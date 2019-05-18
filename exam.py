import random
import numpy as np
#arr = np.random.uniform(13,25,1000000)
arr = [13,14,17,23,25]
print(arr)
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         new_elem = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > new_elem:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = new_elem
#     return arr
# #print(arr)
# print(insertion_sort(arr))


# def sort(container):
#
#     if len(container) <= 1:
#         return container
#     else:
#         sup_elem = random.choice(container)
#         left_cont = [elem for elem in container if elem < sup_elem]
#
#         mid = [sup_elem]
#
#         right_cont = [elem for elem in container if elem > sup_elem]
#         return sort(left_cont) + mid + sort(right_cont)
#
# print(sort(arr))


def sort(arr):
    scope = max(arr) + 1
    sub_arr = [0] * scope
    for x in arr:
         sub_arr[x] += 1
    arr[:] = []
    for num in range(scope):
        arr += [num] * sub_arr[num]
    return arr
print(sort(arr))

# arr_sorted = sorted(arr)
# print(arr_sorted)