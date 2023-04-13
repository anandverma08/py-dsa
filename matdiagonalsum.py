import math


def matdiagonalsum(matrix):
    sum = 0
    mid = 0
    l = len(matrix)
    isOdd = False
    for i in range(0, l):

        if len(matrix) % 2 != 0:
            isOdd = True
            mid = matrix[math.floor(len(matrix)/2)][math.floor(len(matrix)/2)]

        sum = sum + matrix[i][i]
        sum = sum + matrix[i][l-i-1]
    if isOdd is True:
        sum =  sum - mid
    print(sum)


mat = [[5]]
matdiagonalsum(mat)
