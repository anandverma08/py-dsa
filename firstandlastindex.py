import math


def first_position(nums, value):
    def condition(mid):
        if(nums[mid]==value):
            if(mid>0 and nums[mid-1]==value):
                return "left"
            else:
                return "found"
        elif(value>nums[mid]):
            return "right"
        else:
            return "left"

    return binary_search(nums, 0, len(nums)-1, condition)

def last_position(nums, value):
    def condition(mid):
        if(nums[mid]==value):
            if(mid>0 and nums[mid+1]==value):
                return "right"
            else:
                return "found"
        elif(value>nums[mid]):
            return "right"
        else:
            return "left"

    return binary_search(nums, 0, len(nums)-1, condition)



def binary_search(nums,low,high, condition):
    while(low<=high):
        mid = math.floor((low+high)/2)
        result = condition(mid);
        if(result=="found"):
            return mid
        if(result=="left"):
            high = mid-1
        else:
            low = mid+1
    return -1

arr = [1,1,1,1,1,1,1,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
print(last_position(arr, 3))
