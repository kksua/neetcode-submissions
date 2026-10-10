class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = {}

        # Store each letter's position in the alien alphabet
        for i, letter in enumerate(order):
            table[letter] = i

        # Compare each word with the next word
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]

            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    # The first different letters determine the order
                    if table[first[j]] > table[second[j]]:
                        return False

                    # This pair is correctly ordered
                    break
            else:
                # All compared letters match:
                # the longer word cannot come first
                if len(first) > len(second):
                    return False

        return True