class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0

        # Binary exponentiation
        while n > 0:
            # If n is odd
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        return result