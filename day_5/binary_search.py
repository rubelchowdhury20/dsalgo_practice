import math

# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))

 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)

q = int(input("Enter the query element : "))


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

def binary_serach(array, query):
    s_array = quick_sort(array, 0, len(array)-1)
    l = 0
    r = len(array)-1
    m = math.floor((l+r)/2)
    while(l <= r):
        if s_array[m] == query:
            return True
        else:
            if s_array[m] < query:
                l = m+1
                m = math.floor((l+r)/2)
            else:
                r = m-1
                m = math.floor((l+r)/2)
    return False

print(binary_serach(lst, q))