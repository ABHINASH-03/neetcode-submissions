class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            max_freq = max(max_freq, count[s[right]])

            # Number of characters we need to replace
            replacements = (right - left + 1) - max_freq

            while replacements > k:
                count[s[left]] -= 1
                left += 1

                replacements = (right - left + 1) - max_freq

            max_length = max(max_length, right - left + 1)

        return max_length