def gcd(a, b):
    if b == 0:        # base case
        return a
    else:
        return gcd(b, a % b)

print("enter 2 number")
a=int(input())
b=int(input())
print("GCD is:", gcd(a, b))










