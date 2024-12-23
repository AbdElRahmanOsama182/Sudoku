import random
from Domain import Domain
from copy import deepcopy
class SudokuGenerator:
    def __init__(self, difficulty="medium", mrv=False, debug=False):
        self.difficulty = difficulty
        self.mrv = mrv
        self.debug = debug
        
    def generateSudoku(self):
        self.generateFullBoard()
        if self.debug:
            self.printBoard()
            print("="*30)
        self.removeByDifficulty()
        if self.debug:
            self.printBoard()
        return self.board

    def generateFullBoard(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        domains = [[Domain() for _ in range(9)] for _ in range(9)]
        self.fillDiagonal(domains)
        if not self.mrv:
            self.fillBoard()
        else:
            self.fillBoardMRV(domains)

    def fillDiagonal(self, domains):
        for i in range(0, 9, 3):
            self.fillBox(i, i, domains)

    def fillBox(self, row, col, domains):
        boxDomain = Domain()
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                num = random.choice(boxDomain.get_domain())
                self.board[i][j] = num
                boxDomain.remove(num)
                if self.mrv:
                    domains[i][j] = Domain(0)
                    for k in range(9):
                        domains[i][k].remove(num)
                        domains[k][j].remove(num)

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

    def getMRV(self, domains):
        minDomain = 10
        minIndex = (-1, -1)
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0 and domains[i][j].domain_size() < minDomain:
                    minDomain = domains[i][j].domain_size()
                    minIndex = (i, j)
        if minIndex == (-1, -1):
            return None, None
        return minIndex, domains[minIndex[0]][minIndex[1]].get_domain()

    def updateDomains(self, domains, row, col, num):
        newDomains = deepcopy(domains)
        newDomains[row][col] = Domain(0)
        for i in range(9):
            newDomains[row][i].remove(num)
            newDomains[i][col].remove(num)
        bRow, bCol = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                newDomains[i + bRow][j + bCol].remove(num)
        return newDomains

    def fillBoardMRV(self, domains):
        index, domain = self.getMRV(domains)
        if index is None:
            return True
        r, c = index
        for num in domain:
            self.board[r][c] = num
            newDomains = self.updateDomains(domains, r, c, num)
            if self.fillBoardMRV(newDomains):
                return True
            self.board[r][c] = 0
        return False
    
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

    def removeNumbers(self):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while self.board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        temp = self.board[row][col]
        self.board[row][col] = 0
        if self.countSolutions() != 1:
            self.board[row][col] = temp
            return 0
        else:
            return 1 + self.removeNumbers()

    def removeByDifficulty(self):
        toBeRemoved = 0
        if self.difficulty == "easy":
            toBeRemoved = 40
        elif self.difficulty == "medium":
            toBeRemoved = 46
        else:
            toBeRemoved = 50
        while toBeRemoved > 0:
            toBeRemoved -= self.removeNumbers()
        
if __name__ == '__main__':
    sudoku = SudokuGenerator("hard")
    sudoku.printBoard()
