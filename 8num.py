def toh(n,a,b,c):
    if n==1:
        print(f"move {n} from {a} to {c} ")
        return
    toh(n-1,a,c,b)
    print(f"move {n} from {a} to {c} ")
    toh(n-1,b,a,c)



n=int(input("enter a number of disk"))

toh (n,'A','B','C')











