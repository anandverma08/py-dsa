def partition(arr,low,high):
    i = low-1
    pivot = arr[high]

    for j in range(low,high):

        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1


def quickSort(arr,low,high):
    if low<high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)

        quickSort(arr,pi+1,high)
        print(arr)


arra = [2,5,4,8,6,3,1]
quickSort(arra,0,len(arra)-1)