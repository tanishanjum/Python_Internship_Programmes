#operations on queue:
#1.Enqueue:insert the data into the queue
#dequeue:delete the data from the queue
from collections import deque
class QueueExample:
    def __init__(self):

        
        self.queue=deque([])
    def enqueue(self,data):
        self.queue.append(data)
        return self.queue
    def dequeue(self):
        if self.queue==[]:
            print('Queue is underflow')
        else:
            self.queue.popleft()
    def display(self):
        if self.queue==[]:
            print('queue is empty')
        else:
            for i in range(len(self.queue)):
                print(self.queue[i])
obj=QueueExample()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.dequeue()
obj.display()

