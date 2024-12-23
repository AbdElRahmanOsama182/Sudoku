import { defineStore } from 'pinia';
import type { Cell, Difficulty, SudokuState } from '../types/sudoku';
import { createMockGrid } from '../utils/sudoku';

export const useSudokuStore = defineStore('sudoku', {
  state: (): SudokuState => ({
    grid: Array(9).fill(null).map(() => 
      Array(9).fill(null).map(() => ({
        value: null,
        isFixed: false,
      }))
    ),
    difficulty: 'Easy',
    isCreatingMode: false,
    isSolvingMode: false,
    isAISolving: false,
    solveSteps: [],
    currentStepIndex: -1,
    timeElapsed: 0
  }),

  actions: {
    setDifficulty(difficulty: Difficulty) {
      this.difficulty = difficulty;
    },

    clearGrid() {
      this.grid = this.grid.map(row => 
        row.map(cell => ({
          ...cell,
          value: cell.isFixed ? cell.value : null, // Preserve value for fixed cells
        }))
      );
    },

    setCellValue(row: number, col: number, value: number | null) {
      if (row >= 0 && row < 9 && col >= 0 && col < 9) {
        this.grid[row][col].value = value;
      }
    },

    validateGrid(): boolean {
      // const grid = this.grid;
      // TODO: validate from backend
      return true;
    },

    generatePuzzle() {
      // TODO: Generate from backend
      // Full mock grid for testing    
      // Assign the mock grid to the store's state
      this.grid = createMockGrid();
    }    
  }
});