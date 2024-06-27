class Node:
    def __init__(self,item,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    def is_empty(self):
        return self.front == None
    def enqueue(self,data):
        n= Node(data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        self.item_count+=1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        elif self.front == self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.item_count-=1
    def get_first(self):
        if self.is_empty():
            raise IndexError("No data present in the queue")
        else:
            return self.front.item
    def get_last(self):
        if self.is_empty():
            raise IndexError("No data is present in the queue")
        else:
            return self.rear.item
    def size(self):
        return self.item_count
obj = Queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
print(obj.get_first())