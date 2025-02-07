from random import randrange


def random():
    global arr
    arr = []
    for i in range(10):
        arr.append(randrange(0,101))
    return arr
print(*random())  #print kh co [] va ,

def sum_array(arr):
    s = sum(arr)
    return s
print('sum of array =', sum_array(arr))

def count_odd(arr):
    odd = []
    for value in arr:
        if value % 2 != 0:
            odd.append(value)
    return odd
print('number of odd numbers:', len(count_odd(arr)))
print('sum of odd numbers =', sum(count_odd(arr)))

def smallest(arr):
    smallest_num = arr[0]
    for value in arr:
        if value < smallest_num:
            smallest_num = value
    return smallest_num
print('the smallest element:', smallest(arr))

arr.sort()
print('ascending order:', *arr)
arr.reverse()
print(' descending order:', *arr)  #them * dang trc thi print ko co [] va ,