#Queue data structure can be implemented in two ways.
#1-using Array 
class Queue:
    def __init__(self):
        self.queue=[]
        
    def enqueue(self,element):
        return self.queue.append(element)
    
    def dequeue (self):
        if self.isEmpty():
            return "the queue is empty"
        return self.queue.pop(0)
    
    def peek (self):
        if self.isEmpty():
            return "the queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    
my_queue=Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)
print(my_queue.queue)# Output: 10 20 30 40
my_queue.dequeue()
print(my_queue.queue)# Output:  20 30 40
print(my_queue.peek())# Output: 20
print(my_queue.isEmpty())#  False



