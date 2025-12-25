def s(n):
	if n==1:
		return 1;
	else:
		return (n + s(n-1))
n=int(input("enter a number\n"))
s=s(n)
print ("sum=",s)
























