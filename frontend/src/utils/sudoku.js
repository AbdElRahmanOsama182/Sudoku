export function createEmptyGrid() {
  return Array(9).fill(null).map(() =>
    Array(9).fill(null).map(() => ({
      value: null,
      isFixed: false
    }))
  );
}

export function validateGrid(grid) {
  // Basic validation implementation
  for (let i = 0; i < 9; i++) {
    if (!validateRow(grid, i) || !validateColumn(grid, i) || !validateBox(grid, Math.floor(i/3)*3, (i%3)*3)) {
      return false;
    }
  }
  return true;
}

function validateRow(grid, row) {
  const values = new Set();
  for (let col = 0; col < 9; col++) {
    const value = grid[row][col].value;
    if (value !== null) {
      if (values.has(value)) return false;
      values.add(value);
    }
  }
  return true;
}

function validateColumn(grid, col) {
  const values = new Set();
  for (let row = 0; row < 9; row++) {
    const value = grid[row][col].value;
    if (value !== null) {
      if (values.has(value)) return false;
      values.add(value);
    }
  }
  return true;
}

function validateBox(grid, startRow, startCol) {
  const values = new Set();
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      const value = grid[startRow + i][startCol + j].value;
      if (value !== null) {
        if (values.has(value)) return false;
        values.add(value);
      }
    }
  }
  return true;
}