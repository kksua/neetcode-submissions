class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0]  

        for i in range(1, n + 1):
            count = output[i // 2] + (i % 2)
            output.append(count)

        return output