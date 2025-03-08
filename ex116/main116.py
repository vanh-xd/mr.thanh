import numpy as np

arr = np.random.randint(-100, 500, 10)
#q1: print all
print(arr)
#q2: index 2 -> 5
arr2 = arr[[2,3,4,5]]
print(arr2)
#or
arr2_2 = arr[2:6]
print(arr2_2)
#q3: negative values
arr3 = arr[arr < 0]
print(arr3)
#q4: enter x, y. ouput from x -> y
x = int(input('input x: '))
y = int(input('input y: '))
#arr.extend(x,y)
arr4 = arr[arr >= x]
arr4_1 = arr4[arr4 <= y]
print(arr4_1)
#q5: filter negative numbers
#q6: asc
arr6 = np.sort(arr)
print(arr6)
#q7: desc
arr7 = np.sort(arr)[::-1]
print(arr7)
#q8: min, max, mean, median, std
min_elmt = np.min(arr)
max_elmt = np.max(arr)
mean_value = np.mean(arr)
median_value = np.median(arr)
std_value = np.std(arr)
print(min_elmt, max_elmt, mean_value, median_value, std_value)
#q9: del perfect square

#q10: insert X to index V where X & V enter from keyboard
