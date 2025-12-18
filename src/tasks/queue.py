import os
import sys
import logging

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.dirname(current_dir)
sys.path.insert(0, src_dir)


try: #pragma: no cover
    from common.config import LOGGING_CONFIG
except ImportError: #pragma: no cover
    from src.common.config import LOGGING_CONFIG 

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


class Queue:
    
    def __init__(self):
        self.items = []  # используем list для хранения данных
        self.min_elm = None
        self.max_elm = None
    
    def is_empty(self) -> bool:
        print(len(self.items) == 0)
        return len(self.items) == 0
    
    def enqueue(self, x: float) -> None:
        self.items.append(x)
        if self.min_elm is None or x < self.min_elm:
            self.min_elm = x
        if self.max_elm is None or x > self.max_elm:
            self.max_elm = x
        
    def dequeue(self) -> float | str:
        if len(self.items) != 0:
            x = self.items[0]
            self.items.pop(0)
            
            if len(self.items) != 0:
                if x == self.min_elm:
                    self.min_elm = min(self.items)
                if x == self.max_elm:
                    self.max_elm = max(self.items)
            else:
                self.min_elm = None
                self.max_elm = None
            
            print(f"element deleted: {x}\n")
            return x
        else:
            print("queue is empty\n")
            logger.error("queue is empty")
            return "queue is empty"
    
    def front(self) -> float | str:
        if len(self.items) != 0:
            print(f"front element = {self.items[0]}\n")
            return self.items[0]
        else:
            print("queue is empty\n")
            logger.error("queue is empty")
            return "queue is empty"
    
    def __len__(self) -> int:
        print(f"numbers count = {len(self.items)}\n")
        return len(self.items)
    
    
    def clear(self) -> None:
        self.items = []
        self.min_elm = None
        self.max_elm = None
        print("queue cleared\n")
    
    def min(self) -> float:
        if len(self.items) != 0:
            print(f"min element = {self.min_elm}\n")
            return self.min_elm
        else:
            print("queue is empty\n")
            logger.error("queue is empty")
            return "queue is empty"

    
    def max(self) -> float:
        if len(self.items) != 0:
            print(f"max element = {self.max_elm}\n")
            return self.max_elm
        else:
            print("queue is empty\n")
            logger.error("queue is empty")
            return "queue is empty"
    
    
    def str(self) -> str:
        print(f"Queue = {self.items}\n")
        return f"Queue = {self.items}"


queue = Queue()



def main(): # pragma: no cover
    while True:
        
        user_input = [str(x) for x in input().split()]
        
        if not user_input:
            continue
        
        command = user_input[0]
        
        commands = ["enqueue", "dequeue", "front", "is_empty", "len", "min", "max", "str", "clear"]
        
        if command not in commands:
            print(f"unknown command: '{command}'\n")
            logger.error(f"unknown command: '{command}'")
            continue
        
        
        if command == "enqueue":
            try:
                argument = float(user_input[1])
                if argument == -0:
                    argument = abs(argument)
            
            except ValueError:
                print(f"Not is a number: '{user_input[1]}'\n")
                logger.error(f"Not is a number: '{user_input[1]}'")
                continue
                
            except IndexError:
                print("Input 'enqueue <argument>'\n")
                logger.error("Input 'enqueue <argument>'")
                continue
        
        elif command != "enqueue":
            if len(user_input) > 1:
                print(f"Input just '{command}' without <argument>\n")
                logger.error(f"Input just '{command}' without <argument>")
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
                queue.__len__()
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
                logger.error(f"unknown command: '{command}'")
        
    
    
if __name__ == "__main__": # pragma: no cover
    main()