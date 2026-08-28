class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is 0
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        # Maximum possible digits
        result = [0] * (n + m)

        # Multiply digit by digit
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')

                product = digit1 * digit2

                pos1 = i + j
                pos2 = i + j + 1

                total = product + result[pos2]

                result[pos2] = total % 10
                result[pos1] += total // 10

        # Convert result digits to string
        answer = ""

        for digit in result:
            if answer or digit != 0:
                answer += chr(digit + ord('0'))

        return answer