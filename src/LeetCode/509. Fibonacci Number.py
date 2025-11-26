class Solution:
    def fib(self, n: int) -> int:

        sqrt5 = 5**0.5

        """формула n-ного члена последовательности фибоначчи"""
        x = -1/sqrt5 * ((1-sqrt5)/2)**n + 1/sqrt5 * ((1+sqrt5)/2)**n


        return int(round(x))