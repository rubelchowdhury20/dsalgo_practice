#####################
#      pow(x,n)     #
#####################

x = int(input("Enter the number : "))
n = int(input("Enter the power : "))

def pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n%2 == 0:
        if (n>0):
            return pow(x, n//2) ** 2
        else:
            return 1/(pow(x, abs(n)//2) ** 2)
    else:
        if (n>0):
            return x * pow(x, n//2) ** 2
        else:
            return 1/(x * pow(x, abs(n)//2) ** 2)
        
print(pow(x,n))