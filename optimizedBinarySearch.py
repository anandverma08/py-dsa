# import math
import time
#
# # record start time
#
#
input = list(range(10000000,0,-1))
value = 3;
#
#
# def binarySearch(arr,val):
#     result = isFound(arr,0,len(arr)-1,val);
#     print(result)
#
# def isFound(arr,start,end,val):
#
#
#     while start <=end:
#         mid = math.floor((start + end) / 2)
#         isFoundResult = card_locater(arr,value,mid)
#         if(isFoundResult=="found"):
#             return mid;
#         elif(isFoundResult == "left"):
#             end = mid-1;
#         elif(isFoundResult=="right"):
#             start = mid+1
#         elif(isFoundResult==-1):
#             return -1;
#
#
# def card_locater(arr,val,mid):
#
#     if(arr[mid]==val):
#         if(arr[mid-1]>=0 and arr[mid-1]==val):
#             return "left"
#         else:
#             return "found"
#     if(val>arr[mid]):
#         return "left"
#     elif(val<arr[mid]):
#         return "right"
#     else:
#         return -1
#
# start = time.time()
# binarySearch(input,value)
# end = time.time()
#
# print("The time of execution of above program is :",
#       (end-start) * 10**3, "ms")


def search(input, val):
    for i in range(len(input)):

        if input[i] == val:
            return i

    return -1
start = time.time()
print(search(input,value))
end = time.time()

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
