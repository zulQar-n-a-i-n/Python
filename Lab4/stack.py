class stack:
    def __init__(self):
        self.mylist = []

    def push(self,num):
        self.mylist.append(num)

    def isempty(self):
        if len(self.mylist)==0:
            return True
        
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print(f"{self.mylist[-1]} popped !")
            self.mylist.pop()
            

    def top(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print( f"Top element of stack is {self.mylist[-1]}")
    
    def size(self):
        print(f"Size of stack is {len(self.mylist)}")

    def showstack(self):
        print("Stack ",self.mylist)



stack1 = stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(6)
stack1.showstack()
stack1.top()
stack1.pop()
stack1.showstack()

    