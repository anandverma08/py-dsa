def applyOperation(nums):
    for i in range(len(nums)):
        if nums[i] == 0 and i < len(nums) - 1:
            k = i
            while nums[k] == 0:
                k += 1
            nums[i], nums[k] = nums[k], nums[i]
    return nums

print(applyOperation([1,2,2,0,2,0,2,0]))