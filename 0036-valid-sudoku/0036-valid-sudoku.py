class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def is_valid_row(row):
            seen = set()
            for val in row:
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)
            return True
        
        def is_valid_box(box):
            seen = set()
            for row in box:
                for val in row:
                    if val == ".":
                        continue
                    if val in seen:
                        return False
                    seen.add(val)
            return True
        
        def get_boxes(board):
            for row in range(0, 10, 3):
                for col in range(0, 10, 3):
                    yield [rw[col:col+3] for rw in board[row:row+3]]
        
        for row in board:
            if not is_valid_row(row):
                return False
            
        for col in zip(*board):
            if not is_valid_row(col):
                return False
            
        for box in get_boxes(board):
            if not is_valid_box(box):
                return False
            
        return True