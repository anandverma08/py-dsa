import array

# arr1 = array.array('i',[1,2,3,4,5])
# arr2 = array.array('i',[6,7,8,9,10])
# # arr1.extend(arr2)
# print(arr1)
#
#
# l1 = [11,12,13,"anand"]
# try:
#     arr1.fromlist(l1)
# except:
#     print("Cannot add values from list")
# print(arr1)


import numpy as nm

arr1 = nm.array([[5,6,7,8],[9,10,11,12],[13,14,15,16]])
arr2 = nm.insert(arr1,0,[1,2,3],axis=1)
print(arr2)
