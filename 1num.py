while True :
    print("\n cube operations")
    print("1:volume")
    print("2:cube")
    print("3:tSA")
    print("4:exit")
 

    a=int(input(""))

    if a==4:
        print("exiting...")
        break;

    b=float(input("enter side of cube:"))
    if a==1:
        v=b**3
        print("volume=",v)

    elif a==3:
        tsa=6*b*b
        print("total surface area",tsa)
        
    elif a==2:
        cube=b*b*b
        print("cube",cube)
    else:
         print ("nono")
 

