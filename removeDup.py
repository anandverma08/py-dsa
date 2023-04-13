def removeDup(arr):
    res = []
    for i in range(0,len(arr)):
        if not arr[i] in res:
            res.append(arr[i])

    return res

print(removeDup([1,1,2]))