from math import *


def find_max_sum(arr):
    sum = 0
    max_value = -100000000
    initial = 0
    final = 0

    for i in range(0,len(arr)):

        sum = sum + arr[i]
        print(sum,arr[i])
        if arr[i] >= max_value:
            initial = i
            print("initial",initial)
        if(max_value < sum):
            final = i+1

            max_value = sum
            print("final", final, max_value)
        if(sum<0):
            sum = 0

    print(initial,final)
    return arr[initial:final]


print(find_max_sum([20,-30,40,10]))

