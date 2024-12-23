export type Difficulty = 'Easy' | 'Intermediate' | 'Hard';

export interface Cell {
  value: number | null;
  isFixed: boolean;
}

export interface SudokuState {
  grid: Cell[][];
  difficulty: Difficulty;
  isCreatingMode: boolean;
  isSolvingMode: boolean;
  isAISolving: boolean;
  solveSteps: number[][][] | null;
  solutionGrid: number[][] | null;
  currentStepIndex: number;
  timeElapsed: number;
}