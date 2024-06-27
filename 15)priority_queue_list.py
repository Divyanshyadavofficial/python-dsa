class Priority_Queue:
    def __init__(self):
        self.items = []
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if self.is_empty():
            raise IndexError("priority queue is empty")
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)
p=Priority_Queue()
p.push("Amit",4)
p.push("sumit",1)
p.push("kunal",2)
p.push("david",3)
p.push("me",0)

while not p.is_empty():
    print(p.pop())
    