class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_rows = set()
        seen_columns = set()
        seen_squares = set()

        for row in range(9):
            for column in range(9):
                value = board[row][column]

                if value == ".":
                    continue

                row_key = (value, row)
                column_key = (value, column)
                square_key = (value, row // 3, column // 3)

                if (
                    row_key in seen_rows
                    or column_key in seen_columns
                    or square_key in seen_squares
                ):
                    return False

                seen_rows.add(row_key)
                seen_columns.add(column_key)
                seen_squares.add(square_key)

        return True