class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Stack:
    def __init__(self,start=None):
        self.start = start
        self.count = 0
    def is_empty(self):
        return self.start==None
    def push(self,data):
        n= Node(data,self.start)
        self.start=n

        self.count+=1
    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            data = self.start.item
            self.start=self.start.next
            self.count-=1
            return data
        
    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            return self.start.item
    def size(self):
        return self.count

obj=Stack()
obj.push(10)
print(obj.peek())