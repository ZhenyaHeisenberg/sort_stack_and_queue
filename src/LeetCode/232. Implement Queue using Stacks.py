class MyQueue:

    def __init__(self):
        self.items = []
        

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        x = self.items[0]
        self.items.pop(0)
        return x
        
    def peek(self) -> int:
        x = self.items[0]
        return x

    def empty(self) -> bool:
        print(len(self.items) == 0)
        return len(self.items) == 0
