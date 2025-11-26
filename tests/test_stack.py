from src.tasks.stack import Stack



def test_is_empty():
    stack = Stack()


    assert stack.is_empty() is True
    

    stack.push(42)
    assert stack.is_empty() is False


    stack.clear()
    assert stack.is_empty() is True




def test_push():
    stack = Stack()
    
    assert stack.is_empty() is True
    
    stack.push(5)
    assert stack.str() == "Stack = [5]"
    
    stack.push(6)
    assert stack.str() == "Stack = [5, 6]"
    
    stack.push(-6.5)
    assert stack.str() == "Stack = [5, 6, -6.5]"



def test_pop():
    stack = Stack()
    
    assert stack.is_empty() is True
    
    stack.push(5)
    stack.push(6)
    stack.push(-6.5)
    
    assert stack.str() == "Stack = [5, 6, -6.5]"
    
    stack.pop()
    assert stack.str() == "Stack = [5, 6]"
    
    stack.pop()
    assert stack.str() == "Stack = [5]"
    
    stack.pop()
    assert stack.str() == "Stack = []"
    
    stack.pop() == "Stack is empty"




def test_peek():
    stack = Stack()
    
    assert stack.is_empty() is True
    
    stack.push(5)
    stack.push(6)
    stack.push(-6.5)
    
    assert stack.peek() == -6.5
    
    stack.push(9)
    assert stack.peek() == 9
    
    stack.pop()
    stack.pop()
    assert stack.peek() == 6
    
    stack.pop()
    assert stack.peek() == 5
    
    stack.pop()
    assert stack.peek() == "Stack is empty"



def test_len():
    stack = Stack()
    
    assert stack.is_empty() is True
    assert stack.__len__() == 0
    
    stack.push(5)
    stack.push(6)
    stack.push(-6.5)
    
    assert stack.__len__() == 3
    
    stack.push(-6.5)
    assert stack.__len__() == 4
    
    stack.pop()
    stack.pop()
    
    assert stack.__len__() == 2



def test_clear():
    stack = Stack()
    
    assert stack.is_empty() is True
    
    stack.push(5)
    stack.push(6)
    stack.push(-6.5)
    
    assert stack.__len__() == 3
    assert stack.str() == "Stack = [5, 6, -6.5]"
    
    stack.clear()
    assert stack.__len__() == 0
    assert stack.str() == "Stack = []"



def test_min():
    stack = Stack()
    
    assert stack.is_empty() is True
    
    stack.push(5)
    stack.push(6)
    stack.push(-6.5)
    

    assert stack.min() == -6.5
    
    stack.pop()
    assert stack.min() == 5
    
    stack.pop()
    stack.pop()
    
    assert stack.min() == "Stack is empty"



def test_max():
    stack = Stack()
    
    assert stack.is_empty() is True
    
    stack.push(5)
    stack.push(6)
    stack.push(-6.5)


    assert stack.max() == 6

    stack.pop()
    stack.pop()
    assert stack.max() == 5

    stack.pop()

    assert stack.max() == "Stack is empty"



def test_str():
    stack = Stack()
    
    assert stack.str() == "Stack = []"
    
    stack.push(5)
    stack.push(6)
    stack.push(-6.5)
    
    assert stack.str() == "Stack = [5, 6, -6.5]"
    
    stack.pop()
    assert stack.str() == "Stack = [5, 6]"
    
    stack.pop()
    assert stack.str() == "Stack = [5]"
    
    stack.pop()
    assert stack.str() == "Stack = []"
