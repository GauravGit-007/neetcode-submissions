class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes={}
     
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                elif (board[r][c] in rows[r] or board[r][c] in cols[c]     or board[r][c] in boxes.get((r//3,c//3),set())):
                
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    boxes.setdefault((r//3,c//3),set()).add(board[r][c])
        return True


        
        