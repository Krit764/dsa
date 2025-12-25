def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibo(n-1)+fibo(n-2)



n=int(input("\nenter a number\n"))
i=0
print("fibonanci series for ",n,"=",end=" ")
for i in range(n):
    print(fibo(i),end=" ")

