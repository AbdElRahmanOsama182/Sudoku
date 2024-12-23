<script>
import SudokuGrid from '../components/SudokuGrid.vue';
import { useSudokuStore } from '../stores/sudoku'; // Import the store

export default {
  components: {
    SudokuGrid
  },
  computed: {
    store() {
      return useSudokuStore(); // Access the store
    },
    grid() {
      return this.store.grid;
    }
  },
  data() {
    return {
      isComplete: false
    }
  },
  methods: {
    updateCell({ row, col, value }) {
      this.store.setCellValue(row, col, value);
      this.checkCompletion();
    },
    validateCurrentProgress() {
      // TODO: implement logic for validate current progress
    },
    clearGrid() {
      this.store.clearGrid(); // Clear the grid in the store
    },
    checkCompletion() {
      const isComplete = this.grid.every(row =>
        row.every(cell => cell.value !== null)
      );
      if (isComplete && this.store.validateGrid()) {
        this.isComplete = true;
        alert('Congratulations! You solved the puzzle!');
      }
    }
  },
  mounted() {
    this.checkCompletion();
  }
}
</script>

<template>
  <div class="manual-play">
    <h2>Your Turn to Play Sudoku!</h2>
    <SudokuGrid 
      :grid="grid"
      :showNumberBar="true"
      @update-cell="updateCell"
    />
    <div class="controls">
      <button @click="validateCurrentProgress" class="btn">Validate Progress</button>
      <!-- Home button -->
      <router-link to="/" class="btn home-btn">Go to Home</router-link>
      <button @click="clearGrid" class="btn">Clear Input</button>
    </div>
  </div>
</template>

<style scoped>
.manual-play {
  text-align: center;
  padding: 2rem;
}
.manual-play h2 {
  font-size: 2.2rem;
  font-weight: normal;
  color: #317133;
  text-align: center;
  margin-bottom: 20px;
  letter-spacing: 1px;
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
.home-btn {
  background-color: #007BFF; /* Blue color for the home button */
  color: white;
  text-decoration: none; /* Remove the default underline from the link */
}

.home-btn:hover {
  background-color: #0056b3; /* Darker blue when hovered */
}

.home-btn:active {
  background-color: #004085; /* Even darker blue when clicked */
}
</style>