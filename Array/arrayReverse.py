# def reverseArray(arr):
#     l = len(arr)-1
#     for i in range(len(arr)//2):
#         temp = arr[i]
#         arr[i] = arr[l-i]
#         arr[l-i]=temp
#     return arr
#
# arr = [1,2,3,4,5,6]
# # print(reverseArray(arr))
#
# dic = {
#     "name" : "anand",
#     "Age" : 28,
#     "address" : "College Park"
# }
# #
# # newdic = dic.fromkeys(["gender","height"],0)
# # for key in newdic:
# #     newdic[key] = "some value"
# # print(newdic)
#
#
# print(dic.items())


# def merge_dicts(d1,d2):

#
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# res = dict1.copy()
# for key in dict2:
#    if key not in res:
#        res[key] = dict2[key]
#    else:
#        res[key]+=dict2[key]
#
# print(res)
# my_dict = {'a': 5, 'b': 9, 'c': 2}
# def fu(my_dict):
#     for key in my_dict:
#        return {v: k for k, v in my_dict.items()}
# print(fu(my_dict))

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
li = []
for i,j in zip(tuple1, tuple2):
    print(i)
    if i in tuple1 and i in tuple2:
        li.append(i)
print(tuple(li))