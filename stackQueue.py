#clrs chapter 10    Using simple array to implement stack and queue

class Stack:
    def __init__(self, size=8):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, key):
        if self.empty():
            self.top += 1
            self.stack[self.top] = key
        elif self.top < self.size-1:
            self.top += 1
            self.stack[self.top] = key
        elif self.top == self.size-1:
            self.resize()
            self.push(key)

    def resize(self):
        old = self.stack
        old_size = self.size
        self.size = self.size * 2
        self.stack = [None] * self.size
        for i in range(old_size):
            self.stack[i] = old[i]

    def __repr__(self):
        return str(self.stack)

    def pop(self):
        if self.empty() is True:
            print("Error pop operation, stack is empty, underflow")
        else:
            self.top -= 1
            return_val = self.stack[self.top+1]
            self.stack[self.top+1] = None
            return return_val

"""
myStack = Stack(4)
myStack.push(15)
myStack.push(6)
myStack.push(2)
myStack.push(9)
print(myStack)
myStack.push(17)
myStack.push(3)
print(myStack)
print(myStack.pop())
print(myStack)
print(myStack.pop())
print(myStack)
"""

class Queue:
    def __init__(self, size=8):
        self.size = size
        self.queue = [None] * self.size
        self.head = -1
        self.tail = 0

    def __repr__(self):
        return str(self.queue)

    def empty(self):
        if self.head == -1:
            return True
        else:
            return False

    def full(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def enqueue(self, key):
        if self.empty():
            self.queue[self.tail] = key
            self.head += 1
            self.tail += 1
        elif not self.full():
            self.queue[self.tail] = key
            self.tail = (self.tail + 1) % self.size
        else:
            print("queue is full, resize...")
            self.resize()
            self.enqueue(key)

    def resize(self):
        oldQueue = self.queue
        oldSize = self.size
        self.size = self.size * 2
        self.queue = [None] * self.size
        for i in range(oldSize):
            self.queue[i] = oldQueue[i]
        self.tail = oldSize

    def dequeue(self):
        return_val = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.size
        return return_val

"""
myQueue = Queue(4)
myQueue.enqueue(15)
myQueue.enqueue(6)
myQueue.enqueue(9)
myQueue.enqueue(8)
print(myQueue)
myQueue.enqueue(4)
myQueue.enqueue(17)
myQueue.enqueue(3)
print(myQueue)
myQueue.enqueue(23)
myQueue.enqueue(56)
print(myQueue)
print(myQueue.dequeue())
print(myQueue)
myQueue.enqueue(77)
myQueue.enqueue(86)
print(myQueue)
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.enqueue(6)
print(myQueue)
myQueue.dequeue()
print(myQueue)
myQueue.dequeue()
print(myQueue)
myQueue.enqueue(100)
print(myQueue)
"""