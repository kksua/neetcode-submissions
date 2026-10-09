class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for op in operations:
            if op == "+":
                # Add the last two scores
                scores.append(scores[-1] + scores[-2])
            elif op == "D":
                # Double the last score
                scores.append(scores[-1] * 2)
            elif op == "C":
                # Remove the last score
                scores.pop()
            else:
                # Convert the string to an integer
                scores.append(int(op))

        return sum(scores)