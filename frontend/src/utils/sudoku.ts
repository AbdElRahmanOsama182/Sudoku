import type { Cell } from '../types/sudoku'

// Function to create an empty grid (9x9)
export function createEmptyGrid(): Cell[][] {
  return Array(9).fill(null).map(() =>
    Array(9).fill(null).map(() => ({
      value: null,
      isFixed: false
    }))
  );
}

// Function to create a mock grid (9x9) with random pre-filled values
export function createMockGrid(): Cell[][] {
  return Array(9).fill(null).map(() =>
    Array(9).fill(null).map(() => {
      const cell: Cell = { value: null, isFixed: false };
      // 40% chance to have a pre-filled value, 60% chance to be null
      cell.isFixed = Math.random() < 0.4;
      cell.value = cell.isFixed ? Math.floor(Math.random() * 9) + 1 : null; 
      // cell.isFixed = false;

      return cell;
    })
  );
}
