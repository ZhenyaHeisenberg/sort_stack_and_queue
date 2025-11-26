class Queue:
    
    def __init__(self):
        self.items = []  # используем list для хранения данных
        self.items_sorted = []
    
    def is_empty(self) -> bool:
        print(len(self.items) == 0)
        return len(self.items) == 0
    
    def enqueue(self, x: float) -> None: 
        self.items.append(x)
        
        self.items_sorted = sorted(self.items)
        
    def dequeue(self) -> float | str:
        if len(self.items) != 0:
            x = self.items[0]
            self.items.pop(0)
            
            self.items_sorted = sorted(self.items)
            
            print(f"element deleted: {x}\n")
            return x
        else:
            print("queue is empty\n")
            return "queue is empty"
    
    def front(self) -> float | str:
        if len(self.items) != 0:
            print(f"front element = {self.items[-1]}\n")
            return self.items[-1]
        else:
            print("queue is empty\n")
            return "queue is empty"
    
    def __len__(self) -> int:
        print(f"numbers count = {len(self.items)}\n")
        return len(self.items)
    
    
    def clear(self) -> None:
        self.items = []
        self.items_sorted = []
        print("queue cleared\n")
        return []
    
    def min(self) -> float:
        if len(self.items_sorted) != 0: 
            print(f"min element = {self.items_sorted[0]}\n") # O(1)
            return self.items_sorted[0]
        else:
            print("queue is empty\n")
            return "queue is empty"
    
    def max(self) -> float:
        if len(self.items_sorted) != 0:
            print(f"min element = {self.items_sorted[-1]}\n") # O(1)
            return self.items_sorted[-1]
        else:
            print("queue is empty\n")
            return "queue is empty"
    
    
    def str(self):
        print(f"Queue = {self.items}\n")
        return f"Queue = {self.items}"


queue = Queue()



def main(): # pragma: no cover
    while True:
        
        user_input = [str(x) for x in input().split()]
        
        command = user_input[0]
        
        
        if command == "enqueue":
            try:
                argument = float(user_input[1])
                if argument == -0:
                    argument = abs(argument)
            
            except ValueError:
                print(f"Not is a number: '{user_input[1]}'\n")
                continue
                
            except IndexError:
                print("Input 'enqueue <argument>'\n")
                continue
        
        elif command != "enqueue":
            if len(user_input) > 1:
                print(f"Input just '{command}' without <argument>\n")
                continue
            
        
        
        match user_input[0]:
            case "enqueue":
                queue.enqueue(argument)
            case "dequeue":
                queue.dequeue()
            case "front":
                queue.front()
            case "is_empty":
                queue.is_empty()
            case "len":
                queue.len()
            case "min":
                queue.min()
            case "max":
                queue.max()
            case "str":
                queue.str()
            case "clear":
                queue.clear()
                
            case _:
                print(f"unknown command: '{command}'\n")
        
    
    
if __name__ == "__main__": # pragma: no cover
    main()