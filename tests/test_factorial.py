from src.tasks.factorial_and_Fibonacci.factorial import factorial
from src.tasks.factorial_and_Fibonacci.factorial_recursive import factorial_recursive




def test_factorial():

    assert factorial(5) == 120
    assert factorial(10) == 3_628_800
    assert factorial(20) == 2_432_902_008_176_640_000
    
    assert factorial_recursive(5) == 120
    assert factorial_recursive(10) == 3_628_800
    assert factorial_recursive(20) == 2_432_902_008_176_640_000



