from functools import lru_cache

@lru_cache(maxsize=None)
def factorial_recursive(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return factorial_recursive(n-1) * n