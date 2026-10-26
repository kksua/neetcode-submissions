class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            # Add the new character to the window
            char = s[right]
            counts[char] = counts.get(char, 0) + 1

            # Shrink while the window needs too many replacements
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
