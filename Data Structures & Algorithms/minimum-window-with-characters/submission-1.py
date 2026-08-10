class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}

        have = 0
        need_count = len(need)

        left = 0
        best_length = float("inf")
        best_left = 0
        best_right = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            # This character now satisfies one required count
            if c in need and window[c] == need[c]:
                have += 1

            # Current window contains everything we need
            while have == need_count:
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_left = left
                    best_right = right + 1

                # Remove the leftmost character
                left_char = s[left]
                window[left_char] -= 1

                # Window is no longer valid if we removed
                # a required character below its needed count.
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return s[best_left:best_right] if best_length != float("inf") else ""