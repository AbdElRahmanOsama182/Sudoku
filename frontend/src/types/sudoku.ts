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
  solveSteps: Cell[][][];
  currentStepIndex: number;
  timeElapsed: number;
}