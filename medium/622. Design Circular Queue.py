class MyCircularQueue:

    def __init__(self, k: int):
        self.max_size = k
        self.queue = [-1] * self.max_size
        self.size = 0
        self.front = 0
        self.rear = -1


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.size += 1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.front = self.size = 0
            self.rear = -1
            return True
        self.front += 1
        self.front %= self.max_size
        self.size -= 1
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]


    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]


    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
