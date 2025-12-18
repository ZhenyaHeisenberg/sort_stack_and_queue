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


class Stack:
    
    def __init__(self):
        self.items = []  # используем list для хранения данных
        self.min_elm = None
        self.max_elm = None
    
    def is_empty(self) -> bool:
        print(len(self.items) == 0)
        return len(self.items) == 0
    
    def push(self, x: float) -> None: 
        self.items.append(x)
        if self.min_elm is None or x < self.min_elm:
            self.min_elm = x
        if self.max_elm is None or x > self.max_elm:
            self.max_elm = x
        
    def pop(self) -> float | str:
        if len(self.items) != 0:
            x = self.items[-1]
            self.items.pop()
            
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
            print("Stack is empty\n")
            logger.error("Stack is empty")
            return "Stack is empty"
    
    def peek(self) -> float | str:
        if len(self.items) != 0:
            print(f"peek element = {self.items[-1]}\n")
            return self.items[-1]
        else:
            print("Stack is empty\n")
            logger.error("Stack is empty")
            return "Stack is empty"
    
    def __len__(self) -> int:
        print(f"numbers count = {len(self.items)}\n")
        return len(self.items)
    
    
    def clear(self) -> None:
        self.items = []
        self.min_elm = None
        self.max_elm = None
        print("stack cleared\n")

    
    def min(self) -> float:
        if len(self.items) != 0: 
            print(f"min element = {self.min_elm}\n")
            return self.min_elm
        else:
            print("Stack is empty\n")
            logger.error("Stack is empty")
            return "Stack is empty"
    
    def max(self) -> float:
        if len(self.items) != 0:
            print(f"max element = {self.max_elm}\n")
            return self.max_elm
        else:
            print("Stack is empty\n")
            logger.error("Stack is empty")
            return "Stack is empty"
    
    def str(self) -> str:
        print(f"Stack = {self.items}\n")
        return f"Stack = {self.items}"





stack = Stack()



def main(): # pragma: no cover
    while True:
        
        user_input = [str(x) for x in input().split()]
        
        if not user_input:
            continue
        
        command = user_input[0]
        
        commands = ["push", "pop", "peek", "is_empty", "len", "min", "max", "str", "clear"]
        
        if command not in commands:
            print(f"unknown command: '{command}'\n")
            logger.error(f"unknown command: '{command}'")
            continue
        
        
        if command == "push":
            try:
                argument = float(user_input[1])
                if argument == -0:
                    argument = abs(argument)
            
            except ValueError:
                print(f"Not is a number: '{user_input[1]}'\n")
                logger.error(f"Not is a number: '{user_input[1]}'")
                continue
                
            except IndexError:
                print("Input 'push <argument>'\n")
                logger.error("Input 'push <argument>'")
                continue
        
        elif command != "push":
            if len(user_input) > 1:
                print(f"Input just '{command}' without <argument>\n")
                logger.error(f"Input just '{command}' without <argument>")
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
                logger.error(f"unknown command: '{command}'")




if __name__ == "__main__": # pragma: no cover
    main()