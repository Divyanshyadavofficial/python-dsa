class Queue:
    def __init__(self):
        self.items=[]
        self.item_count=0
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,data):
        self.items.append(data)
        self.item_count+=1
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
            self.item_count-=1
        else:
            raise IndexError("queue under flow")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue underflow")
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("queue underflow")
    def size(self):
        return self.item_count
ob1=Queue()
ob1.enqueue(12)
ob1.enqueue(13)
ob1.enqueue(14)
print(ob1.get_front())
print(ob1.size())
