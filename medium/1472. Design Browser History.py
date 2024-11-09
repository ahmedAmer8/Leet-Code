class Node:
    def __init__(self, val= None, next= None, prev= None):
        self.val = val
        self.next = next
        self.prev = prev
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)

    def visit(self, url: str) -> None:
        newPage = Node(url)
        newPage.prev = self.head
        self.head.next = newPage
        self.head = self.head.next


    def back(self, steps: int) -> str:
        while self.head.prev and steps > 0:
            self.head = self.head.prev
            steps -= 1
        return self.head.val

    def forward(self, steps: int) -> str:
        while self.head.next and steps > 0:
            self.head = self.head.next
            steps -= 1
        return self.head.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
