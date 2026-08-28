class Solution:
    def checkValidString(self, s: str) -> bool:
        # low = minimum possible number of open parentheses
        # high = maximum possible number of open parentheses
        low = 0
        high = 0

        for char in s:
            if char == '(':
                low += 1
                high += 1

            elif char == ')':
                low = max(0, low - 1)
                high -= 1

            else:  # char == '*'
                # '*' can be ')' or '(' or empty
                low = max(0, low - 1)
                high += 1

            # Too many ')' even when '*' are used optimally
            if high < 0:
                return False

        # If minimum possible open parentheses is 0,
        # we can make the string valid.
        return low == 0