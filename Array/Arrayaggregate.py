import random

l = []
# average = 0
# try:
#     while(True):
#         inp = input("Enter a number :")
#         if inp == "done":
#             average = sum(l) / len(l)
#             print(average)
#             break
#         l.append(int(inp))
# except:
#     print("Invalid entry")
#


# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])
#
# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
#
# random.shuffle(fruit_list1)
#
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
#
# print(fruit_list1)
# print(fruit_list2)
# print(fruit_list3)
#
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
#
# print(sum)
# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# def fun(m):
#     v = m[0][0]
#
#     for row in m:
#         for element in row:
#             if v < element: v = element
#
#     return v
#
#
# print(fun(data[0]))

# inp = input("Enter number of days: ")
# i = 1
# l = []
# print(int(inp))
# while(i<=int(inp)):
#     l.append(int(input(f"Enter {i} day tempreture ")))
#     i+=1
#
# av = sum(l)/len(l)
# print("Average is",av)

# def rotate(matrix):
#     n = len(matrix)
#
#     # Transpose the matrix
#     for i in range(n):  # Iterate over the rows
#         for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
#             # Swap the elements at positions (i, j) and (j, i)
#             print(i,j)
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
#     # Reverse each row
#     for row in matrix:  # Iterate over each row in the matrix
#         row.reverse()  # Reverse the elements in the current row
#     print(matrix)
#
# rotate([[0,0,0],[0,1,0],[1,1,1]])


