import random
from Domain import Domain
import time
class SudokuGenerator:
    def __init__(self, debug=False):
        self.difficulty = "Intermediate"
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

    def printBoard(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- " * 11)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(self.board[i][j], end=" ")
            print()

    def naiveBoardValidation(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
                num = self.board[i][j]
                self.board[i][j] = 0
                if not self.isValid(i, j, num):
                    return False
                self.board[i][j] = num
        return True

    def isFull(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True

    def countSolutions(self):
        if self.isFull():
            return 1
        count = 0
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    for num in range(1, 10):
                        if self.isValid(i, j, num):
                            self.board[i][j] = num
                            count += self.countSolutions()
                            self.board[i][j] = 0
                            # we don't need to know the exact number of solutions so we can return early
                            if count > 1:
                                return count
                    return count
        return count

    def removeNumbers(self, indexes):
        row, col = random.choice(indexes)
        temp = self.board[row][col]
        self.board[row][col] = 0
        if self.countSolutions() != 1:
            self.board[row][col] = temp
            indexes.remove((row, col))
            return 0
        else:
            indexes.remove((row, col))
            return 1 + self.removeNumbers(indexes)

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
        while toBeRemoved > 0 and len(indexes) > 0:
            toBeRemoved -= self.removeNumbers(indexes)
            # print("Indexes remaining:", len(indexes))
        
if __name__ == '__main__':
    sudoku = SudokuGenerator()
    iterations = 10
    times = []
    for _ in range(iterations):
        start = time.time()
        sudoku.generateSudoku("Easy")
        # sudoku.generateSudoku("Intermediate")
        # sudoku.generateSudoku("Hard")
        end = time.time()
        times.append(end - start)
        print(f"Time: {end - start:.6f} seconds")
    print(f"Average time: {sum(times) / iterations:.6f} seconds")
    print(f"Minimum time: {min(times):.6f} seconds")
    print(f"Maximum time: {max(times):.6f} seconds")
