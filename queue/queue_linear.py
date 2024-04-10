class Queue:
    def __init__(self, queue=[]):
        self.queue = queue
        self.front = 0
    
    def pop(self):
        if not self.queue:
            return
        frontVal = self.queue[self.front]
        self.front += 1
        if self.front == len(self.queue):
            self.queue = []
            self.front = 0
        return frontVal

    def push(self, val):
        self.queue.append(val)

    def print(self):
        print(self.queue[self.front:])

def test():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.pop()
    queue.print()
    queue.pop()
    print(queue.queue)
