s=5
q=[0] * s
front = -1
rear = -1
def enque():
    global front, rear 
    if (rear+1)%s==front:
        print ("que is full")
        return
    item = int(input("enter a num"))
    if (front==-1):
        front =0
        rear =0
    else:
        rear=(rear+1)%s
    q[rear]=item
    print("inserted",end="")
def deque():
    global front, rear
    if (front == -1):
        print("que is empty",end= "")
        return
    print("deleted:",q[front],end="")
    if (front==rear):
        front=-1
        rear=-1
    else:
        front=(front+1)%s
def display():
    if(front ==-1):
        print("empty queue",end="")
        return
    i=front
    while True:
        print(q[i],end = " ")
        if i == rear:
            return
        i = (i+1)%s
print (" circular queue menu")
print ("1=enque 2=deque 3=display 4=exit")
print("enter choice",end="")
while True:
    print()
    c=int(input(""))
    if c==1:
        enque()
    elif c==2:
        deque()
    elif c==3:
        print("queue=",end="")
        display()
    elif c==4:
        break
    else:
        print("dumb choice")







