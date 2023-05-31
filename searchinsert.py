import math

nums = [1,3,5,7,8]
target = 6


def binarySearch(array):
    start = 0
    end = len(nums) - 1

    # Traverse an array
    while (start <= end):

        mid =  math.floor((start + end) / 2)

        # if target value found.
        if nums[mid] == target:
            return mid

        # If target value is greater then mid elements's value
        elif target > nums[mid]:
            start = mid + 1

        # otherwise target value is less,
        else:
            end = mid - 1
    # Return the insertion position
    return end + 1


print(binarySearch(nums))