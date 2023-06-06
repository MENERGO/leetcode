class MyStack:

    def __init__(self):
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        x = self.list[-1]
        self.list = self.list[:-1]
        return x

    def top(self) -> int:
        if len(self.list) != 0:
            return self.list[-1]
        return []

    def empty(self) -> bool:
        if len(self.list) == 0:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(11)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
