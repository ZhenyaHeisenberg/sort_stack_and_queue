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
    
    flag_type = input()

    print("\nWhich type of sort you want to use:\n1. bubble_sort\n2. bucket_sort\n3. counting_sort\n4. heap_sort\n5. quick_sort\n6. radix_sort\n")
    
    sort_type = input("Sort type: ")
    
    inputed = input("Array: ")
    inputed = inputed.replace(" ", "")
    inputed = inputed.replace("[", "")
    inputed = inputed.replace("]", "")
    arr_str = inputed.split(",")
    
    
    arr = [float(x) for x in arr_str]
    
    
    match sort_type:
        case "1":
            arr = bubble_sort(arr)
        case "2":
            arr = bucket_sort(arr)
        case "3":
            arr = counting_sort(arr)
        case "4":
            arr = heap_sort(arr)
        case "5":
            arr = quick_sort(arr)
        case "6":
            arr = radix_sort(arr)
        case _:
            print("Input just a number from 1 to 6")
    
    match flag_type:
        case "1":
            print(f"Sorted array: {arr}")
        case "2":
            print(f"Sorted array: {arr[::-1]}")
        case _:
            print("Input just a number from 1 to 2")

def solve_factorial():
    number = int(input("Input a natural number: "))
    
    print(f"\nfactorial({number}) = {factorial(number)}\n")


def solve_fibonacci():
    number = int(input("Input a natural number: "))
    print(f"\nfibonacci({number}) = {fibo(number)}\n")

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
    
if __name__ == "__main__":
    main()