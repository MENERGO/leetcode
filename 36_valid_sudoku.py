class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        board_t = [*zip(*board)]
        for n in range(9):
            count_points_row = board[n].count('.')
            count_points_col = board_t[n].count('.')
            if len(set(board[n])) - 1 != 9 - count_points_row or len(set(board_t[n])) - 1 != 9 - count_points_col:
                return False
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                sub_board = [i[c:c + 3] for i in board[r:r + 3]]
                sub_board = sub_board[0] + sub_board[1] + sub_board[2]
                count_points = sub_board.count('.')
                if len(set(sub_board)) - 1 != 9 - count_points:
                    return False
        return True


print(Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                   , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                   , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                   , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                   , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                   , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                   , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                   , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                   , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
