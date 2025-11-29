import sys
import os
import logging.config

# Добавляем корневую директорию проекта в Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from common.config import LOGGING_CONFIG

# Настраиваем логирование
logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger(__name__)



from sort.bubble_sort import bubble_sort
from sort.bucket_sort import bucket_sort
from sort.counting_sort import counting_sort
from sort.heap_sort import heap_sort
from sort.quick_sort import quick_sort
from sort.radix_sort import radix_sort

from factorial_and_Fibonacci.factorial import factorial
from factorial_and_Fibonacci.fibo import fibo





def sort():
    print("Straight or reverse sort:\n1. Straight\n2. Reverse\n")
    
    flag_type = input() # Straight or Reverse
    
    if flag_type not in ["1", "2"]:
        print("Input just a number from 1 to 2")
        return None
    
    

    print("\nWhich type of sort you want to use:\n1. bubble_sort\n2. bucket_sort\n3. counting_sort\n4. heap_sort\n5. quick_sort\n6. radix_sort\n")
    
    sort_type = input("Sort type: ") # function sort
    
    inputed = input("Array: ")
    inputed = inputed.replace(" ", "")
    inputed = inputed.replace("[", "")
    inputed = inputed.replace("]", "")
    arr_str = inputed.split(",")
    
    
    arr = [float(x) for x in arr_str]
    
    
    
    match sort_type:
        
        case "1":
            arr = bubble_sort(arr)
            log_massage = (f"Array sorted by bubble_sort: {arr}")
            
        case "2":
            arr = bucket_sort(arr)
            log_massage = (f"Array sorted by bucket_sort: {arr}")
            
        case "3":
            arr = counting_sort(arr)
            log_massage = (f"Array sorted by counting_sort: {arr}")
            
        case "4":
            arr = heap_sort(arr)
            log_massage = (f"Array sorted by heap_sort: {arr}")
            
        case "5":
            arr = quick_sort(arr)
            log_massage = (f"Array sorted by quick_sort: {arr}")
            
        case "6":
            arr = radix_sort(arr)
            log_massage = 1
            log_massage = (f"Array sorted by radix_sort: {arr}")
            
        case _:
            print("Input just a number from 1 to 6")
            logger.error("nput just a number from 1 to 6")
            return None
    
    match flag_type:
        case "1":
            print(f"Sorted array: {arr}") # Straight
            logger.info(f"{log_massage} (Straight)")
        case "2":
            print(f"Sorted array: {arr[::-1]}") # Reverse
            logger.info(f"{log_massage} (Reverse)")
        case _:
            print("Input just a number from 1 to 2")
            return None

def solve_factorial():
    number = int(input("Input a natural number: "))
    
    if number >= 0:    
        print(f"\nfactorial({number}) = {factorial(number)}\n")
        logger.info(f"factorial({number}) = {factorial(number)}")
        return None
    else:
        print("Input a natural or '0'")
        logger.error("Input a natural or '0'")


def solve_fibonacci():
    number = int(input("Input a natural number: "))
    
    if number >= 0:
        print(f"\nfibonacci({number}) = {fibo(number)}\n")
        logger.info(f"fibonacci({number}) = {fibo(number)}")
    else:
        print("Input a natural or '0'")
        logger.error("Input a natural or '0'")

def main():
    
    print("What do you want:\n1. Sort array\n2. Solve factorial\n3. Solve Fibonacci\n(1/2/3)")
    
    user_input = input()
    
    match user_input:
        case "1":
            sort()
        case "2":
            solve_factorial()
        case "3":
            solve_fibonacci()
        case _:
            print("Input just a number from 1 to 3")
            logger.error("Input just a number from 1 to 3")
            return None
    
if __name__ == "__main__":
    main()