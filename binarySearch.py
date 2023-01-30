import math

nums = [13,11,4,3,1]
value = 11


def binarySearch(array):
    if(len(array)>0):
        found = isFound(array, 0, len(nums)-1, value)
        print("Position", found)
    else:
        print("Array is empty")


def isFound(arr, start, end, value):
    mid = math.floor((start + end) / 2)
    if (arr[mid] == value):
        return mid
    if (start > end):
        return "Not Found";
    if (value < arr[mid]):
        return isFound(arr, mid+1, end, value)
    else:
        return isFound(arr, start, mid-1, value)
    return False


binarySearch(nums)