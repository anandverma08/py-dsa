def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_array = arr[:mid]
        right_array = arr[mid:]
        mergesort(left_array)
        mergesort(right_array)
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i = i + 1
            else:
                arr[k] = right_array[j]
                j = j + 1
            k = k + 1

        while i < len(left_array):
            arr[k] = left_array[i]
            i = i + 1
            k = k + 1

        while j < len(right_array):
            arr[k] = right_array[j]
            j = j + 1
            k = k + 1

        return arr


arra = [2, 5, 4, 8, 6, 3, 1]
print(mergesort(arra))
