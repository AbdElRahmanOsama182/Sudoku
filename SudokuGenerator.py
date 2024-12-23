import random
from Domain import Domain
import time
from sudoku import Sudoku
class SudokuGenerator:
    def __init__(self, debug=False):
        self.debug = debug
        self.board = []
        
    def generateSudoku(self, difficulty="Intermediate"):
        self.generateFullBoard()
        if self.debug:
            print("Full Board:")
            self.printBoard()
            print("=" * 25)
        self.removeByDifficulty(difficulty)
        if self.debug:
            print("Sudoku Board:")
            self.printBoard()

    def generateFullBoard(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.fillDiagonal()
        self.fillBoard()

    def fillDiagonal(self):
        for i in range(0, 9, 3):
            self.fillBox(i, i)

    def fillBox(self, row, col):
        boxDomain = Domain()
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                num = random.choice(boxDomain.get_domain())
                self.board[i][j] = num
                boxDomain.remove(num)
    
    def fillBoard(self, i=0, j=0):
        if i == 8 and j == 9:
            return True
        if j == 9:
            i += 1
            j = 0
        if self.board[i][j] != 0:
            return self.fillBoard(i, j + 1)
        for num in range(1, 10):
            if self.isValid(i, j, num):
                self.board[i][j] = num
                if self.fillBoard(i, j + 1):
                    return True
                self.board[i][j] = 0
        return False

    def isValid(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        bRow, bCol = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[i + bRow][j + bCol] == num:
                    return False
        return True

    def removeByDifficulty(self, difficulty):
        # generate a list with all the indexes of the board
        indexes = [(i, j) for i in range(9) for j in range(9)]
        toBeRemoved = 0
        if difficulty == "Easy":
            toBeRemoved = 30
        elif difficulty == "Intermediate":
            toBeRemoved = 40
        else:
            toBeRemoved = 50
        # any board with 74 or more numbers is guaranteed to have a unique solution
        # so we can remove the first 7 numbers without checking for the number of solutions
        empty = 0
        while len(indexes) > 74:
            row, col = random.choice(indexes)
            self.board[row][col] = 0
            indexes.remove((row, col))
            empty += 1
        
        toBeRemoved -= empty
        while toBeRemoved > 0 and len(indexes) > 0:
            removed = self.removeNumbers(indexes, empty)
            toBeRemoved -= removed
            empty += removed
            # print("Indexes remaining:", len(indexes))
        
    def removeNumbers(self, indexes, empty):
        row, col = random.choice(indexes)
        temp = self.board[row][col]
        self.board[row][col] = 0
        if self.countSolutions(empty + 1) != 1:
            self.board[row][col] = temp
            indexes.remove((row, col))
            return 0
        else:
            indexes.remove((row, col))
            return 1 + self.removeNumbers(indexes, empty + 1)

    def countSolutions(self, empty):
        if empty == 0:
            return 1
        # board must have at least 17 numbers to have a unique solution
        if empty > 81 - 17:
            return 2
        count = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    for num in range(1, 10):
                        if self.isValid(i, j, num):
                            self.board[i][j] = num
                            count += self.countSolutions(empty - 1)
                            self.board[i][j] = 0
                            # we don't need to know the exact number of solutions so we can return early
                            if count > 1:
                                return count
                    return count
        return count

    def isFull(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True

    def checkUserBoard(self, userBoard):
        self.board = userBoard
        if not self.boardValidation():
            return False, "Invalid board, at least one of the numbers is repeated in the same row, column or box"
        empty = sum([row.count(0) for row in self.board])
        # print(empty)
        solutions = self.countSolutions(empty)
        if solutions == 0:
            return False, "Invalid board, no solution"
        if solutions > 1:
            return False, "Invalid board, multiple solutions"
        return True, "Valid board"

    def boardValidation(self):
        rows = [Domain() for _ in range(9)]
        cols = [Domain() for _ in range(9)]
        boxes = [[Domain() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    continue
                num = self.board[i][j]
                if not rows[i].remove(num) or not cols[j].remove(num) or not boxes[i // 3][j // 3].remove(num):
                    return False
        return True

    def printBoard(self):
        board = ''
        for i, row in enumerate(self.board):
            if i == 0 or i % 3 == 0:
                board += ('+-' + '-' * 6) * 3 + '+\n'
            board += (('| ' + '{} ' * 3) * 3 + '|\n').format(
                *[str(x) if x != 0 else ' ' * 1 for x in row]
            )
        board += ('+-' + '-' * 6) * 3 + '+\n'
        print(board)



if __name__ == '__main__':
    sudoku = SudokuGenerator()
    iterations = 100
    times = []
    for _ in range(iterations):
        start = time.time()
        # sudoku.generateSudoku("Easy")
        # sudoku.generateSudoku("Intermediate")
        sudoku.generateSudoku("Hard")
        valid, message = sudoku.checkUserBoard(sudoku.board)
        # verify the board is valid with the library
        sudokuL = Sudoku(3, 3, sudoku.board)
        if not valid:
            sudoku.printBoard()
            print(message)
        if not sudokuL.validate():
            sudoku.printBoard()
            print("Invalid board")
        if sudokuL.has_multiple_solutions():
            sudoku.printBoard()
            print("Multiple solutions")
        end = time.time()
        times.append(end - start)
        print(f"Time: {end - start:.6f} seconds")
    print(f"Average time: {sum(times) / iterations:.6f} seconds")
    print(f"Minimum time: {min(times):.6f} seconds")
    print(f"Maximum time: {max(times):.6f} seconds")

    # test board validation
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 1, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    print(sudoku.checkUserBoard(board))
    # verify the board is valid with the library
    sudokuL = Sudoku(3, 3, board)
    print("Board is valid:", sudokuL.validate())
    print("Board has many solutions:", sudokuL.has_multiple_solutions())
