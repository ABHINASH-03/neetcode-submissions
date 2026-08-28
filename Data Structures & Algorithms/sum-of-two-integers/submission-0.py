class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            # Calculate carry
            carry = (a & b) << 1

            # Calculate sum without carry
            a = (a ^ b) & MASK

            # Keep only 32 bits
            b = carry & MASK

        # Convert back to negative number if needed
        if a > MAX_INT:
            return ~(a ^ MASK)

        return a