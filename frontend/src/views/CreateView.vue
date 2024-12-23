<script>
import SudokuGrid from '../components/SudokuGrid.vue';
import { createEmptyGrid } from '../utils/sudoku';

export default {
  components: {
    SudokuGrid
  },
  data() {
    return {
      grid: createEmptyGrid()
    }
  },
  methods: {
    clearGrid() {
      this.grid = createEmptyGrid();
    },
    updateCell({ row, col, value }) {
      this.grid[row][col].value = value;
    },
    async validateAndProceed() {
      try {
        // TODO: Add backend validation
        const isValid = true; // Placeholder for backend validation
        if (isValid) {
          this.$router.push('/play');
        } else {
          alert('Invalid Sudoku configuration!');
        }
      } catch (error) {
        alert('Error validating the puzzle');
      }
    }
  }
}
</script>

<template>
  <div class="create">
    <h2>Create New Sudoku Puzzle</h2>
    <SudokuGrid 
      :grid="grid"
      :showNumberBar="true"
      @update-cell="updateCell"
    />
    <div class="controls">
      <button @click="clearGrid" class="btn">Clear Grid</button>
      <button @click="validateAndProceed" class="btn primary">Done Creating</button>
    </div>
  </div>
</template>

<style scoped>
.create {
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

.btn.primary {
  background: #4CAF50;
  color: white;
}
</style>