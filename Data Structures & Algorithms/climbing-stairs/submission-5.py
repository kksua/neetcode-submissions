class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def recursiveStairs(i):
            if i >= n:
                return int(i == n)

            if i in cache:
                return cache[i]

            cache[i] = recursiveStairs(i + 1) + recursiveStairs(i + 2)
            return cache[i]

        return recursiveStairs(0)
