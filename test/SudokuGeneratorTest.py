import unittest
from SudokuGenerator import SudokuGenerator
from sudoku import Sudoku
import time

class SudokuGeneratorTest(unittest.TestCase):
    def test_generateSudoku(self):
        iterations = 100
        times = []
        sudoku = SudokuGenerator()
        for _ in range(iterations):
            start = time.time()
            sudoku.generateSudoku()
            end = time.time()
            times.append(end - start)
            sudokuL = Sudoku(3, 3, sudoku.board)
            self.assertTrue(sudokuL.validate())
            self.assertFalse(sudokuL.has_multiple_solutions())
            self.assertTrue(sudokuL.solve())
        print(f"Average time: {sum(times) / iterations:.6f} seconds")
        print(f"Minimum time: {min(times):.6f} seconds")
        print(f"Maximum time: {max(times):.6f} seconds")

    def test_checkUserBoard_valid(self):
        sudoku = SudokuGenerator()
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        valid, message, validatedBoard = sudoku.checkUserBoard(board)
        sudokuL = Sudoku(3, 3, board).solve()
        self.assertTrue(valid)
        self.assertEqual("Valid board", message)
        self.assertEqual(validatedBoard, sudokuL.board)

    def test_checkUserBoard_invalid(self):
        sudoku = SudokuGenerator()
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 8]
        ]
        valid, message, validatedBoard = sudoku.checkUserBoard(board)
        self.assertFalse(valid)
        self.assertEqual("Invalid board, at least one of the numbers is repeated in the same row, column or box", message)

    def test_checkUserBoard_manySolutions(self):
        sudoku = SudokuGenerator()
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 0]
        ]
        valid, message, validatedBoard = sudoku.checkUserBoard(board)
        self.assertFalse(valid)
        self.assertTrue(Sudoku(3, 3, board).has_multiple_solutions())
        self.assertEqual("Invalid board, multiple solutions", message)

    def test_uniqueSolution(self):
        sudoku = SudokuGenerator()
        iterations = 100
        times = []
        for _ in range(iterations):
            sudoku.generateSudoku("Hard")
            start = time.time()
            sudokuL = Sudoku(3, 3, sudoku.board)
            end = time.time()
            times.append(end - start)
            self.assertFalse(sudokuL.has_multiple_solutions())

if __name__ == '__main__':
    unittest.main()


