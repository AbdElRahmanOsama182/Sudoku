import axios from 'axios';

const BASE_URL = 'http://localhost:8080/api/sudoku';

// Types for API Responses
export interface ValidationResponse {
  success: boolean;
  message: string;
  solution: number[][] | null;
}

export interface GeneratePuzzleResponse {
  grid: number[][];
}

export interface SolveStepsResponse {
  steps: [number, number, number][][];
  timeElapsed: number; 
}


// API Methods

/**
 * Validates the Sudoku grid in creation mode.
 * @param grid - 2D array representing the Sudoku grid.
 * @returns A promise resolving to the validation response.
 */
export const validatePuzzle = async (grid: number[][]): Promise<ValidationResponse> => {
  try {
    const response = await axios.post<ValidationResponse>(`${BASE_URL}/validate`, { grid });
    return response.data;
  } catch (error) {
    console.error('Error validating the puzzle:', error);
    throw new Error('Failed to validate the puzzle.');
  }
};

/**
 * Generates a Sudoku puzzle based on the difficulty level.
 * @param difficulty - Difficulty level ("Easy", "Intermediate", "Hard").
 * @returns A promise resolving to the generated puzzle response.
 */
export const generatePuzzle = async (difficulty: string): Promise<GeneratePuzzleResponse> => {
  try {
    const response = await axios.post<GeneratePuzzleResponse>(`${BASE_URL}/generate`, { difficulty });
    return response.data;
  } catch (error) {
    console.error('Error generating the puzzle:', error);
    throw new Error('Failed to generate the puzzle.');
  }
};

/**
 * Solves the Sudoku puzzle using an AI CSP solver and returns steps.
 * @param grid - 2D array representing the Sudoku grid.
 * @returns A promise resolving to the steps response.
 */
export const solvePuzzleSteps = async (grid: number[][]): Promise<SolveStepsResponse> => {
  try {
    const response = await axios.post<SolveStepsResponse>(`${BASE_URL}/solve-steps`, { grid });
    return response.data;
  } catch (error) {
    console.error('Error solving the puzzle with steps:', error);
    throw new Error('Failed to solve the puzzle with steps.');
  }
};
