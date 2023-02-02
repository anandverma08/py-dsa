nums = [3,2,4]
target = 6
arr = {}

def printer():
    for index,x in enumerate(nums):
        temp = target - x
        print(nums.index(x))
        if arr.get(temp) is not None and x == list(arr.get(temp))[0]:
            return [list(arr.get(temp))[1], index]
        else:
            arr[x] = [temp,index]

    return []

print(printer())

