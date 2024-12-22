import { defineStore } from 'pinia';
import type { Cell, Difficulty, SudokuState } from '../types/sudoku';

export const useSudokuStore = defineStore('sudoku', {
  state: (): SudokuState => ({
    grid: Array(9).fill(null).map(() => 
      Array(9).fill(null).map(() => ({
        value: null,
        isFixed: false,
        notes: []
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
        row.map(() => ({
          value: null,
          isFixed: false,
          notes: []
        }))
      );
    },

    setCellValue(row: number, col: number, value: number | null) {
      if (row >= 0 && row < 9 && col >= 0 && col < 9) {
        this.grid[row][col].value = value;
      }
    },

    validateGrid(): boolean {
      // Basic validation implementation
      for (let i = 0; i < 9; i++) {
        if (!this.validateRow(i) || !this.validateColumn(i) || !this.validateBox(Math.floor(i/3)*3, (i%3)*3)) {
          return false;
        }
      }
      return true;
    },

    validateRow(row: number): boolean {
      const values = new Set();
      for (let col = 0; col < 9; col++) {
        const value = this.grid[row][col].value;
        if (value !== null) {
          if (values.has(value)) return false;
          values.add(value);
        }
      }
      return true;
    },

    validateColumn(col: number): boolean {
      const values = new Set();
      for (let row = 0; row < 9; row++) {
        const value = this.grid[row][col].value;
        if (value !== null) {
          if (values.has(value)) return false;
          values.add(value);
        }
      }
      return true;
    },

    validateBox(startRow: number, startCol: number): boolean {
      const values = new Set();
      for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
          const value = this.grid[startRow + i][startCol + j].value;
          if (value !== null) {
            if (values.has(value)) return false;
            values.add(value);
          }
        }
      }
      return true;
    },

    generatePuzzle() {
      // Placeholder for puzzle generation logic
      // This would be implemented with proper Sudoku generation algorithms
      this.clearGrid();
      // Example: Set some initial values based on difficulty
      const fillCount = {
        'Easy': 35,
        'Intermediate': 30,
        'Hard': 25
      }[this.difficulty];
      
      // For now, just fill some random valid numbers
      for (let i = 0; i < fillCount; i++) {
        const row = Math.floor(Math.random() * 9);
        const col = Math.floor(Math.random() * 9);
        if (this.grid[row][col].value === null) {
          this.grid[row][col].value = Math.floor(Math.random() * 9) + 1;
          this.grid[row][col].isFixed = true;
        }
      }
    }
  }
});