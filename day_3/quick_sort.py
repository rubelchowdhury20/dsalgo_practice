# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)

# lst = [1, 5, 2, 4, 3]

# import random
# lst = []
# for i in range(20):
#     lst.append(random.randint(0, 20))

def quick_sort(array, p, r):
    if p<r:
        q, array = partition(array, p, r)
        array = quick_sort(array, p, q-1)
        array = quick_sort(array, q+1, r)
    return array

def partition(array, p, r):
    x = array[r]
    i = p-1
    for j in range(p, r):
        if array[j] < x:
            i = i+1
            flag = array[i]
            array[i] = array[j]
            array[j] = flag
    flag = array[r]
    array[r] = array[i+1]
    array[i+1] = flag
    return i+1, array

print(quick_sort(lst, 0, len(lst)-1))

