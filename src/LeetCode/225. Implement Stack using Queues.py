class MyStack:

    def __init__(self):
        self.items = []


    def push(self, x: int) -> None:
        self.items.append(x)


    def pop(self) -> int:
        x = self.items[-1]
        self.items.pop(-1)
        return x

    def top(self) -> int:
        x = self.items[-1]
        return x

    def empty(self) -> bool:
        print(len(self.items) == 0)
        return len(self.items) == 0
        
