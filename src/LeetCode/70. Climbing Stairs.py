class Solution:
    def climbStairs(self, n: int) -> int:

        sqrt5 = 5**0.5

        """формула n+1-ого члена последовательности фибоначчи"""
        x = -1/sqrt5 * ((1-sqrt5)/2)**(n+1) + 1/sqrt5 * ((1+sqrt5)/2)**(n+1)


        return int(round(x))