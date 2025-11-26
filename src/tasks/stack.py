class Stack:
    
    def __init__(self):
        self.items = []  # используем list для хранения данных
        self.items_sorted = []
    
    def is_empty(self) -> bool:
        print(len(self.items) == 0)
        return len(self.items) == 0
    
    def push(self, x: float) -> None: 
        self.items.append(x)
        
        self.items_sorted = sorted(self.items)
        
    def pop(self) -> float | str:
        if len(self.items) != 0:
            x = self.items[-1]
            self.items.pop(-1)
            
            self.items_sorted = sorted(self.items)
            
            print(f"element deleted: {x}\n")
            return x
        else:
            print("Stack is empty\n")
            return "Stack is empty"
    
    def peek(self) -> float | str:
        if len(self.items) != 0:
            print(f"peek element = {self.items[-1]}\n")
            return self.items[-1]
        else:
            print("Stack is empty\n")
            return "Stack is empty"
    
    def __len__(self) -> int:
        print(f"numbers count = {len(self.items)}\n")
        return len(self.items)
    
    
    def clear(self) -> None:
        self.items = []
        self.items_sorted = []
        print("stack cleared\n")

    
    def min(self) -> float:
        if len(self.items_sorted) != 0: 
            print(f"min element = {self.items_sorted[0]}\n") # O(1)
            return self.items_sorted[0]
        else:
            print("Stack is empty\n")
            return "Stack is empty"
    
    def max(self) -> float:
        if len(self.items_sorted) != 0:
            print(f"max element = {self.items_sorted[-1]}\n") # O(1)
            return self.items_sorted[-1]
        else:
            print("Stack is empty\n")
            return "Stack is empty"
    
    def str(self):
        print(f"Stack = {self.items}\n")
        return f"Stack = {self.items}"





stack = Stack()



def main(): # pragma: no cover
    while True:
        
        user_input = [str(x) for x in input().split()]
        
        command = user_input[0]
        
        
        if command == "push":
            try:
                argument = float(user_input[1])
                if argument == -0:
                    argument = abs(argument)
            
            except ValueError:
                print(f"Not is a number: '{user_input[1]}'\n")
                continue
                
            except IndexError:
                print("Input 'push <argument>'\n")
                continue
        
        elif command != "push":
            if len(user_input) > 1:
                print(f"Input just '{command}' without <argument>\n")
                continue
            
        
        
        match user_input[0]:
            case "push":
                stack.push(argument)
            case "pop":
                stack.pop()
            case "peek":
                stack.peek()
            case "is_empty":
                stack.is_empty()
            case "len":
                stack.__len__()
            case "min":
                stack.min()
            case "max":
                stack.max()
            case "str":
                stack.str()
            case "clear":
                stack.clear()
                
            case _:
                print(f"unknown command: '{command}'\n")




if __name__ == "__main__": # pragma: no cover
    main()