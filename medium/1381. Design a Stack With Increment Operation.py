class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize 
        self.stack = [0] * maxSize
        self.values = [0] * maxSize
        self.cur = -1


    def push(self, x: int) -> None:
        if self.cur == self.maxSize-1:
            return
        self.cur += 1
        self.stack[self.cur] = x
        self.values[self.cur] = 0
        


    def pop(self) -> int:
        if self.cur == -1:
            return -1
        val, inc = self.stack[self.cur], self.values[self.cur]
        self.cur -= 1
        if self.cur >= 0:
            self.values[self.cur] += inc
        return val + inc


    def increment(self, k: int, val: int) -> None:
        if self.cur >= 0:
            self.values[min(k-1, self.cur)] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
