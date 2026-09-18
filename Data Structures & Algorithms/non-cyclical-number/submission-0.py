class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            total = 0

            for i in range(len(str(n))):
                total += int(str(n)[i]) ** 2

            n = total

            if n == 1:
                return True

        return False

        