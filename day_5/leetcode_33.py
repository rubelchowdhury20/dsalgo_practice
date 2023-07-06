########################
# Rotated sorted array #
########################


import math
import random

lst = random.sample(list(range(20)), 10)
lst.sort()
rotation = random.randint(0, 10)
lst = lst[rotation:] + lst[:rotation]
query = random.randint(0, 20)

# lst = [4,5,6,7,0,1,2]
# query = 3

# lst = [1]
# query = 0

lst = [2,3,4,5,6,7,8,9,1]
query = 9

print(lst)
print(query)


def search(nums, target):
        
    l = 0
    r = len(nums)-1
    m = math.floor((l+r)/2)
    while(l <= r):
        print(l, m, r)
        if (r-l+1) <= 2:
            for i in range(l,r+1):
                if nums[i] == target:
                        return i
            return -1
        if target == nums[m]:
            return m
        
        if nums[l] <= nums[m-1]:
                if target <= nums[m-1] and target >= nums[l]:
                    r = m-1
                    m = math.floor((l+r)/2)
                else:
                    l = m+1
                    m = math.floor((l+r)/2)
        else:
            if target >= nums[m+1] and target <= nums[r]:
                l = m+1
                m = math.floor((l+r)/2)
            else:
                r = m-1
                m = math.floor((l+r)/2)
    
    return -1





print(search(lst, query))