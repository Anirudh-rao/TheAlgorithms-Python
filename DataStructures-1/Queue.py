class Queue:
    def __init__(self):
        self.queue = []
    #Add an Element
    def enqueue(self, item):
        self.queue.append(item)

    #Remove an Element
    def  dequeue(self):
        if len(self.queue) <  1:
            return none
        return  self.queue.pop(0)

    #Display the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

#creating the Queue
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After Removing an element")
q.display()
