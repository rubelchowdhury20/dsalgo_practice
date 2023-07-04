# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)

def insertion_sort(array):
    n = len(array)
    for i in range(1,n):
        j = i-1
        while j >= 0 and array[j] > array[j+1]:
            flag = array[j]
            array[j] = array[j+1]
            array[j+1] = flag
            j = j-1
    return array

print(insertion_sort(lst))