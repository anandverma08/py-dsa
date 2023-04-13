# def insertion_sort(arr):
#     count = 0
#     for i in range(1,len(arr)):
#         value = arr[i]
#         j = i-1
#         print(i,j)
#         while j >= 0 and arr[j]>value:
#             # count = count+1
#             print(j)
#             arr[j+1] = arr[j]
#             print(arr)
#             j -= 1
#         arr[j+1] = value
#     print(count)
#     return arr
#
# arr = list(range(1,10000))
# arr.reverse()
# print(insertion_sort(arr))

# def insertion_sort(arr,n):
#
#     if n <=1:
#        return
#
#     insertion_sort(arr,n-1)
#
#     value = arr[n-1]
#     j = n-2
#     while j >= 0 and arr[j]>value:
#         arr[j+1] = arr[j]
#         j -= 1
#     arr[j+1] = value
#
#     return arr


# print(insertion_sort([12,5,23,125,67]))







def insertion_sort(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        j = i-1
        while j>=0 and arr[j]>value:
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1]=value
        print(arr)

    return arr

print(insertion_sort([4,3,5,2,9,1]))






