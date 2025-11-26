def factorial(n: int) -> int:
    num = 1
    for i in range(1, n+1):
        num *= i
    return num
