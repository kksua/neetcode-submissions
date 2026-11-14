from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        seen = set()

        def dfs(row, col, i):
            if i == len(word):
                return True

            if (
                row < 0 or row >= rows
                or col < 0 or col >= cols
                or (row, col) in seen
                or board[row][col] != word[i]
            ):
                return False

            seen.add((row, col))

            found = (
                dfs(row + 1, col, i + 1)
                or dfs(row - 1, col, i + 1)
                or dfs(row, col + 1, i + 1)
                or dfs(row, col - 1, i + 1)
            )

            seen.remove((row, col))
            return found

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False