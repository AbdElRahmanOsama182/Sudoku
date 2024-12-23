<script>
import SudokuGrid from '../components/SudokuGrid.vue';
import { validateGrid } from '../utils/sudoku';

export default {
  components: {
    SudokuGrid
  },
  data() {
    return {
      grid: [], // Will be populated from store
      isComplete: false
    }
  },
  methods: {
    updateCell({ row, col, value }) {
      this.grid[row][col].value = value;
      this.checkCompletion();
    },
    validateCurrentProgress() {
      if (validateGrid(this.grid)) {
        alert('Valid progress so far!');
      } else {
        alert('There are some errors in your solution.');
      }
    },
    clearGrid() {
      this.grid = this.grid.map(row =>
        row.map(cell => ({
          ...cell,
          value: cell.isFixed ? cell.value : null
        }))
      );
    },
    checkCompletion() {
      const isComplete = this.grid.every(row =>
        row.every(cell => cell.value !== null)
      );
      if (isComplete && validateGrid(this.grid)) {
        this.isComplete = true;
        alert('Congratulations! You solved the puzzle!');
      }
    }
  }
}
</script>

<template>
  <div class="manual-play">
    <h2>Solve Manually</h2>
    <SudokuGrid 
      :grid="grid"
      :showNumberBar="true"
      @update-cell="updateCell"
    />
    <div class="controls">
      <button @click="validateCurrentProgress" class="btn">Validate Progress</button>
      <button @click="clearGrid" class="btn">Clear Input</button>
    </div>
  </div>
</template>

<style scoped>
.manual-play {
  text-align: center;
  padding: 2rem;
}

.controls {
  margin-top: 1rem;
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background: #f0f0f0;
}
</style>