# def insertion_sort(arr):
#     count = 0
#     for i in range(1,len(arr)):
#         value = arr[i]
#         j = i-1
#         while j >= 0 and arr[j]>value:
#             count = count+1
#
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = value
#     print(count)
#     return arr
#
# arr = list(range(1,10000))
# arr.reverse()
# print(insertion_sort(arr))

def insertion_sort(arr,n):

    if n <=1:
       return

    insertion_sort(arr,n-1)

    value = arr[n-1]
    j = n-2
    while j >= 0 and arr[j]>value:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = value

    return arr


print(insertion_sort([2,5,23,12,67],5))


