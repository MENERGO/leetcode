class MyStack:

    def __init__(self):
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        x = self.list[0]
        self.list = self.list[1:]
        return x

    def peek(self) -> int:
        if len(self.list) != 0:
            return self.list[0]
        return []

    def empty(self) -> bool:
        if len(self.list) == 0:
            return True
        return False

# Your MyQueue object will be instantiated and called as such :
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
