# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)

def selection_sort(array):
    for i in range(len(array)):
        smallest = array[i]
        smallest_idx = i
        for j in range(i, len(array)):
            if array[j] < smallest:
                smallest = array[j]
                smallest_idx = j
        flag = array[i]
        array[i] = smallest
        array[smallest_idx] = flag
    return array

print(selection_sort(lst))
