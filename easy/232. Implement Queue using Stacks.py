class Node:
    def __init__(self, val= 0, next= None):
        self.val = val
        self.next = next
class MyQueue:

    def __init__(self):
        self.head = None
        self.tail = None
    def push(self, x: int) -> None:
        new_node = Node(x, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def pop(self) -> int:
        temp = self.head.val
        self.head = self.head.next
        return temp
    def peek(self) -> int:
        return self.head.val

    def empty(self) -> bool:
        return not self.head


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
