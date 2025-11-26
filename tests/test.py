import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.tasks.sort.bubble_sort import bubble_sort
from src.tasks.sort.bucket_sort import bucket_sort
from src.tasks.sort.counting_sort import counting_sort
from src.tasks.sort.heap_sort import heap_sort
from src.tasks.sort.quick_sort import quick_sort
from src.tasks.sort.radix_sort import radix_sort

from src.tasks.factorial_and_Fibonacci.factorial import factorial
from src.tasks.factorial_and_Fibonacci.factorial_recursive import factorial_recursive
from src.tasks.factorial_and_Fibonacci.fibo import fibo
from src.tasks.factorial_and_Fibonacci.fibo_recursive import fibo_recursive



import random

arr_int = []
arr_float = []
arr_string = []

n = random.randint(10, 20) # Случайная длинна списка

"""Проверка сортировки для массива целых чисел"""
for i in range(n): # Случайные целые числа
    arr_int.append(random.randint(-1000, 1000))


"""Проверка сортировки для массива вещественных чисел"""
for i in range(n): # Случайные вещественные числа
    arr_float.append(random.uniform(-1000, 1000))


"""Проверка сортировки для массива строк"""
for i in range(n): # Случайные строки
    word = ""
    for length in range(random.randint(1, 10)): # Случайная длина слова
        unicode_index = random.randint(90, 122) # Случайный индекс символа a-z в unicode
        word = word + str(chr(unicode_index))
    arr_string.append(word)

# Тесты sort()
def test_sort():

    assert bubble_sort(arr_int) == sorted(arr_int)
    assert bubble_sort(arr_float) == sorted(arr_float)
    assert bubble_sort(arr_string) == sorted(arr_string)
    
    assert bucket_sort(arr_int) == sorted(arr_int)
    assert bucket_sort(arr_float) == sorted(arr_float)
    assert bucket_sort(arr_int, 0) == "The number of baskets must be >= 1"
    
    assert counting_sort(arr_int) == sorted(arr_int)
    
    assert heap_sort(arr_int) == sorted(arr_int)
    assert heap_sort(arr_float) == sorted(arr_float)
    assert heap_sort(arr_string) == sorted(arr_string)
    
    assert quick_sort(arr_int) == sorted(arr_int)
    assert quick_sort(arr_float) == sorted(arr_float)
    assert quick_sort(arr_string) == sorted(arr_string)
    
    assert radix_sort(arr_int, 10) == sorted(arr_int)
    assert radix_sort(arr_int, 1) == "base must be >= 2"


def test_factorial():

    assert factorial(5) == 120
    assert factorial(10) == 3_628_800
    assert factorial(20) == 2_432_902_008_176_640_000
    
    assert factorial_recursive(5) == 120
    assert factorial_recursive(10) == 3_628_800
    assert factorial_recursive(20) == 2_432_902_008_176_640_000
    



def test_fibo():
    
    assert fibo(10) == 55
    assert fibo(30) == 832_040
    
    assert fibo_recursive(10) == 55
    assert fibo_recursive(30) == 832_040
    
    
    
    
if __name__ == "__main__":
    # Запускаем все тестовые функции
    try:
        print("Тестирование sort...")
        test_sort()
        
        print("Тестирование factorial...")
        test_factorial()
        
        print("Тестирование fibonacci...")
        test_fibo()
        
        print("✅ Все тесты прошли успешно!")
    except Exception:
        print("❌ Неверный ответ")
