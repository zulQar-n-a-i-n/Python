class Queue:
    def __init__(self) :
        self.myqueue = []

    def enqueue(self,num):
        self.myqueue.append(num)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print(f"{self.myqueue[0]} dequeued")
            del self.myqueue[0]

    def front(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print(f"{self.myqueue[0]} is on front")

    def isempty(self):
        if len(self.myqueue)==0:
            return True

    def size(self):
        return len(self.myqueue)

    def showQueue(self):
        print("Queue : ",self.myqueue)
    

q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
q1.enqueue(6)
q1.showQueue()
q1.front()
q1.dequeue()
q1.showQueue()
q1.front()
print(q1.size())
