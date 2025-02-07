import 1_singly_linked_list
from 1_singly_linked_list import *
class Stack:
    def __init__(self):
        self.mylist=sll()
        self.item_count=0
    def is_empty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
            self.mylist.delete_first()
            self.item_count-=1
    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item
    def size(self):
        return self.item_count
s=Stack()
s.push(10)
s.push(20)
print()
print("Top element is ",s.peek()) 
