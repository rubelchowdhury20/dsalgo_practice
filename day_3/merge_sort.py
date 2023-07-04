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

def merge_sort(array, p, r):
    if p<r:
        q = math.floor((p+r)/2)
        if r-p>=2:
            array = merge_sort(array, p, q)
            array = merge_sort(array, q, r)
        array = combine(array, p, q, r)
    return array


def combine(array, p, q, r):
    left = array[p:q]
    right = array[q:r]
    left.append(math.inf)
    right.append(math.inf)
    combined_array = []
    li = 0
    ri = 0
    while(li!=len(left) and ri!=len(right)):
        if left[li] < right[ri]:
            combined_array.append(left[li])
            li += 1
        else:
            combined_array.append(right[ri])
            ri += 1
    if li!=len(left):
        combined_array.extend(left[li:])
    else:
        combined_array.extend(right[ri:])
    array[p:r] = combined_array[:-2]
    return array

print(merge_sort(lst, 0, len(lst)))