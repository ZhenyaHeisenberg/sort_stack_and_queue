from src.tasks.factorial_and_Fibonacci.fibo import fibo
from src.tasks.factorial_and_Fibonacci.fibo_recursive import fibo_recursive



def test_fibo():
    
    assert fibo(10) == 55
    assert fibo(30) == 832_040
    
    assert fibo_recursive(10) == 55
    assert fibo_recursive(30) == 832_040
