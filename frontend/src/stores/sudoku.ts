import { defineStore } from 'pinia';
import type { Cell, Difficulty, SudokuState } from '../types/sudoku';
import { createMockGrid } from '../utils/sudoku';
import { validatePuzzle, generatePuzzle, solvePuzzleSteps } from '../api/sudokuApi';
import type { GeneratePuzzleResponse, ValidationResponse, SolveStepsResponse} from '../api/sudokuApi';

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
    solveSteps: null,
    solutionGrid: null,
    currentStepIndex: -1,
    timeElapsed: 0.0
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

    async validateGrid(): Promise<ValidationResponse> {
      try {
        const response = await validatePuzzle(
          this.grid.map(row => row.map(cell => cell.value ?? 0))
        );
        this.solutionGrid = response.solution;
        return response;
      } catch (error) {
        console.error('Error validating grid:', error);
        return { success: false, message: 'Validation failed.', solution: null };
      }
    },

    async generatePuzzle() {
      try {
        const response: GeneratePuzzleResponse = await generatePuzzle(this.difficulty);
          this.grid = response.grid.map(row =>
            row.map(value => ({
              value,
              isFixed: value !== null,
            }))
          );
      } catch (error) {
        console.error('Error generating puzzle:', error);
      }
    }, 
    
    async computeSolvingSteps() {
      try {
        this.isAISolving=true;
        const response: SolveStepsResponse = await solvePuzzleSteps(
          this.grid.map(row => row.map(cell => cell.value ?? 0))
        );
        this.solveSteps = response.steps;
        this.timeElapsed = response.timeElapsed;
        this.currentStepIndex = 0; // Start from the first step
      }
      catch (error) {
        console.error('Error getting steps using AI:', error);
      }
      finally {
        this.isAISolving = false;
      }
    }
  }
});