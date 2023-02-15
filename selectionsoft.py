def selection_sort(arr,n):
    for i in range(0,n-2):
        iMin = i
        for j in range(i+1, n-1):
            if arr[j] < arr[iMin]:
                iMin = j
                print(iMin)


        arr[i],arr[iMin] = arr[iMin],arr[i]
    return arr



print(selection_sort([1,4,3,5,23,12,45],7))
