def fact(n):
    if n==1 or n==0:
        return n
    return n*fact(n-1)


n=int(input("enter a num\n"))
print("factorial of",n," is ",fact(n))



















