def factorial_recursive(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return factorial_recursive(n-1) * n
