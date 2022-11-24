class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        self.board = board
        self.word = word
        for row in range(len(board)):
            for col in range(len(board[0])):
                cell = row, col
                self.used = set()
                if self.is_word_here(cell, word):
                    return True

        return False

    def is_word_here(self, cell: tuple[int, int], word: str) -> bool:
        output = False
        row, col = cell

        if self.board[row][col] == word[0]:
            self.used.add(cell)
            if len(word) == 1:
                return True
            queue = self.valid_adjacent_cells(cell)
            if not queue:
                self.used.remove(cell)
                return False
            for next_cell in queue:
                output = self.is_word_here(next_cell, word[1:]) or output
            if not output:
                self.used.remove(cell)

        return output

    def valid_adjacent_cells(self, cell: tuple[int, int]
                             ) -> list[tuple[int, int]]:
        output = []
        row, col = cell
        adjacents = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for r_adj, c_adj in adjacents:
            new_cell = (row + r_adj, col + c_adj)
            if self.is_valid_cell(new_cell):
                output.append(new_cell)
        return output

    def is_valid_cell(self, cell):
        row, col = cell
        rows, cols = len(self.board), len(self.board[0])
        return cell not in self.used and 0 <= row < rows and 0 <= col < cols