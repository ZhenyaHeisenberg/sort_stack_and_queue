from src.tasks.queue import Queue



def test_is_empty():
    queue = Queue()


    assert queue.is_empty() is True
    

    queue.enqueue(42)
    assert queue.is_empty() is False


    queue.clear()
    assert queue.is_empty() is True




def test_enqueue():
    queue = Queue()
    
    assert queue.is_empty() is True
    
    queue.enqueue(5)
    assert queue.str() == "Queue = [5]"
    
    queue.enqueue(6)
    assert queue.str() == "Queue = [5, 6]"
    
    queue.enqueue(-6.5)
    assert queue.str() == "Queue = [5, 6, -6.5]"



def test_dequeue():
    queue = Queue()
    
    assert queue.is_empty() is True
    
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(-6.5)
    
    assert queue.str() == "Queue = [5, 6, -6.5]"
    
    queue.dequeue()
    assert queue.str() == "Queue = [6, -6.5]"
    
    queue.dequeue()
    assert queue.str() == "Queue = [-6.5]"
    
    queue.dequeue()
    assert queue.str() == "Queue = []"
    
    queue.dequeue() == "queue is empty"




def test_front():
    queue = Queue()
    
    assert queue.is_empty() is True
    
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(-6.5)
    
    assert queue.front() == -6.5
    
    queue.enqueue(9)
    assert queue.front() == 9
    
    queue.dequeue()
    queue.dequeue()
    assert queue.front() == 9
    
    queue.dequeue()
    assert queue.front() == 9
    
    queue.dequeue()
    assert queue.front() == "queue is empty"



def test_len():
    queue = Queue()
    
    assert queue.is_empty() is True
    assert queue.__len__() == 0
    
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(-6.5)
    
    assert queue.__len__() == 3
    
    queue.enqueue(-6.5)
    assert queue.__len__() == 4
    
    queue.dequeue()
    queue.dequeue()
    
    assert queue.__len__() == 2



def test_clear():
    queue = Queue()
    
    assert queue.is_empty() is True
    
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(-6.5)
    
    assert queue.__len__() == 3
    assert queue.str() == "Queue = [5, 6, -6.5]"
    
    queue.clear()
    assert queue.__len__() == 0
    assert queue.str() == "Queue = []"



def test_min():
    queue = Queue()
    
    assert queue.is_empty() is True
    
    queue.enqueue(-6.5)
    queue.enqueue(6)
    queue.enqueue(5)
    

    assert queue.min() == -6.5
    
    queue.dequeue()
    assert queue.min() == 5
    
    queue.dequeue()
    queue.dequeue()
    
    assert queue.min() == "queue is empty"



def test_max():
    queue = Queue()
    
    assert queue.is_empty() is True
    
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(-6.5)


    assert queue.max() == 6

    queue.dequeue()
    queue.dequeue()
    assert queue.max() == -6.5

    queue.dequeue()

    assert queue.max() == "queue is empty"



def test_str():
    queue = Queue()
    
    assert queue.str() == "Queue = []"
    
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(-6.5)
    
    assert queue.str() == "Queue = [5, 6, -6.5]"
    
    queue.dequeue()
    assert queue.str() == "Queue = [6, -6.5]"
    
    queue.dequeue()
    assert queue.str() == "Queue = [-6.5]"
    
    queue.dequeue()
    assert queue.str() == "Queue = []"
