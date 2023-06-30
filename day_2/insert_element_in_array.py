# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    lst.append(ele)
 
while(True):
    p = int(input("Enter the position to be included : "))
    if(p < n):
        break
    else:
        print("wrong position entered")

c = int(input("Enter the character to be inserted : "))

lst.append(" ")
for i in range(p, n):
    lst[p + n - i] = lst[p + n - i - 1]
lst[p] = c
print(lst)
