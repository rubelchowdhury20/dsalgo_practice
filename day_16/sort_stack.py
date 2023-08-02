class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        n = len(s)
        for i in range(n):
            dummy_stack = []
            while(len(s) > i):
                last = s.pop()
                if len(dummy_stack) > 0:
                    if dummy_stack[-1] < last:
                        flag = dummy_stack.pop()
                        dummy_stack.append(last)
                        dummy_stack.append(flag)
                    else:
                        dummy_stack.append(last)
                else:
                    dummy_stack.append(last)
            for i in dummy_stack[::-1]:
                s.append(i)
        return s
        # Code here



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends