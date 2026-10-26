from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)


        rows = len(board)
        cols = len(board[0])
       

        for r in range(rows):
            for c in range(cols):
                print(f'row is:{r}')
                print(f'col is:{c}')
                print((r//3, c//3))
                if board[r][c] =='.':
                    continue
                if board[r][c] in row_set[r] or board[r][c] in col_set[c] or board[r][c] in square_set[(r//3,c//3)]:
                    
                    return False
                else:
                    row_set[r].add(board[r][c])
                    col_set[c].add(board[r][c])
                    square_set[r//3,c//3].add(board[r][c])

        return True