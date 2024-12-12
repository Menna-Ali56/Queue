#Queue data structure can be implemented in two ways.
#2-Using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None: 
            self.front = self.rear = new_node
            return
        self.rear.next = new_node  
        self.rear = new_node 
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None: 
            self.rear = None
        return temp.data

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data

    def isEmpty(self):
        return self.front is None

    def size(self):
        return self.length

    def print_queue(self):  
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Create and use the queue
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)

my_queue.print_queue()  # Output: 10 20 30 40
print(my_queue.dequeue())  # Output: 10
my_queue.print_queue()  # Output: 20 30 40