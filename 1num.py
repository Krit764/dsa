queue = []

def enqueue():
    x = int(input("Enter element: "))
    queue.append(x)
    print("Inserted")

def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Removed:", queue.pop(0))

def peek():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Front element:", queue[0])

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue:", queue)

while True:
    print("\n1.Enqueue  2.Dequeue  3.Peek  4.Display  5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        peek()
    elif ch == 4:
        display()
    elif ch == 5:
        break
    else:
        print("Invalid choice")

