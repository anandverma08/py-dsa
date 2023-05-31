list1= [3,4,5,6,7,0,1,2]
# rotation=1
# l = len(list1)
#
# for i in range(l-1,-1,-1):
#
#     if list1[i]>list1[i-1]:
#
#         rotation+=1
#     else:
#         break
# print(rotation)

def rotation(list1):
    start = 0
    end = len(list1)-1

    while start<=end:
        mid = int((start+end)/2)
        if list1[mid]<list1[mid-1] and list1[mid]<list1[mid+1]:
            return mid
        elif list1[mid]<list1[start]:
            end = mid-1
        elif list1[mid]>list1[end]:
            start = mid+1
    return -1
print(rotation(list1))