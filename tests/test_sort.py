from src.tasks.sort.bubble_sort import bubble_sort
from src.tasks.sort.bucket_sort import bucket_sort
from src.tasks.sort.counting_sort import counting_sort
from src.tasks.sort.heap_sort import heap_sort
from src.tasks.sort.quick_sort import quick_sort
from src.tasks.sort.radix_sort import radix_sort




import random

arr_int_n1 = []
arr_int_n2 = []
arr_int_n3 = []
arr_float = []
arr_string = []
arr_empty = []


n1 = random.randint(1, 49) # Случайная длинна списка №1
n2 = random.randint(100, 200) # Случайная длинна списка №2
n3 = random.randint(1000, 1100) # Случайная длинна списка №3

"""Проверка сортировки для массива целых чисел"""
for i in range(n1): # Случайные целые числа
    arr_int_n1.append(random.randint(-1000, 1000))

"""Проверка сортировки для массива целых чисел"""
for i in range(n2): # Случайные целые числа
    arr_int_n2.append(random.randint(-1000, 1000))

"""Проверка сортировки для массива целых чисел"""
for i in range(n3): # Случайные целые числа
    arr_int_n3.append(random.randint(-1000, 1000))


"""Проверка сортировки для массива вещественных чисел"""
for i in range(n1): # Случайные вещественные числа
    arr_float.append(random.uniform(-1000, 1000))


"""Проверка сортировки для массива строк"""
for i in range(n1): # Случайные строки
    word = ""
    for length in range(random.randint(1, 10)): # Случайная длина слова
        unicode_index = random.randint(90, 122) # Случайный индекс символа a-z в unicode
        word = word + str(chr(unicode_index))
    arr_string.append(word)

# Тесты sort()
def test_sort():

    assert bubble_sort(arr_int_n1) == sorted(arr_int_n1)
    assert bubble_sort(arr_int_n2) == sorted(arr_int_n2)
    assert bubble_sort(arr_int_n3) == sorted(arr_int_n3)
    assert bubble_sort(arr_float) == sorted(arr_float)
    assert bubble_sort(arr_string) == sorted(arr_string)
    assert bubble_sort(arr_empty) == []
    
    assert bucket_sort(arr_int_n1) == sorted(arr_int_n1)
    assert bucket_sort(arr_int_n1, 10) == sorted(arr_int_n1)
    assert bucket_sort(arr_int_n2) == sorted(arr_int_n2)
    assert bucket_sort(arr_int_n3) == sorted(arr_int_n3)
    assert bucket_sort(arr_float) == sorted(arr_float)
    assert bucket_sort(arr_int_n1, -2) == "The number of baskets must be >= 1"
    assert bucket_sort(arr_empty) == []
    
    assert counting_sort(arr_int_n1) == sorted(arr_int_n1)
    assert counting_sort(arr_int_n2) == sorted(arr_int_n2)
    assert counting_sort(arr_empty) == []
    
    assert heap_sort(arr_int_n1) == sorted(arr_int_n1)
    assert heap_sort(arr_int_n2) == sorted(arr_int_n2)
    assert heap_sort(arr_int_n3) == sorted(arr_int_n3)
    assert heap_sort(arr_float) == sorted(arr_float)
    assert heap_sort(arr_string) == sorted(arr_string)
    assert heap_sort(arr_empty) == []
    
    assert quick_sort(arr_int_n1) == sorted(arr_int_n1)
    assert quick_sort(arr_int_n2) == sorted(arr_int_n2)
    assert quick_sort(arr_int_n3) == sorted(arr_int_n3)
    assert quick_sort(arr_float) == sorted(arr_float)
    assert quick_sort(arr_string) == sorted(arr_string)
    assert quick_sort(arr_empty) == []
    
    assert radix_sort(arr_int_n1, 10) == sorted(arr_int_n1)
    assert radix_sort(arr_int_n2) == sorted(arr_int_n2)
    assert radix_sort(arr_int_n3) == sorted(arr_int_n3)
    assert radix_sort(arr_int_n1, 1) == "base must be >= 2"
    assert radix_sort(arr_empty) == []

