class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, element):
        new_node = Node(element)
        if self.isEmpty():
            self.front = self.rear = new_node
            self.rear.next = self.front  # Circular link
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front  # Circular link
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        if self.front == self.rear:  # Only one element
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front  # Maintain circular link
        self.length -= 1
        return temp.data

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data

    def isEmpty(self):
        return self.length == 0

    def size(self):
        return self.length

    def printQueue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        temp = self.front
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.front:  # Circular condition
                break
        print()

# Example usage
myQueue = CircularQueue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ")
myQueue.printQueue()
print("Dequeue: ", myQueue.dequeue())
print("Peek: ", myQueue.peek())
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())
print("Queue after operations: ")
myQueue.printQueue()
