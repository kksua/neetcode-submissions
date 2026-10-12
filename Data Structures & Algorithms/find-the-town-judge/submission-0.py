class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = [0] * (n + 1)
        trusts = [0] * (n + 1)

        for first, second in trust:
            trusts[first] += 1       
            trusted_by[second] += 1  

        for person in range(1, n + 1):
            if trusts[person] == 0 and trusted_by[person] == n - 1:
                return person

        return -1