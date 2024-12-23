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
  methods: {
    startManualPlay() {
      this.mode = 'manual';
      this.$router.push('/manual-play');
    },
    startAIPlay() {
      this.mode = 'ai';
      this.$router.push('/solve-ai');
    }
  }
}
</script>

<template>
  <div class="play">
    <h2>Play Sudoku</h2>
    <SudokuGrid :grid="grid" :is-editable="false" :showNumberBar="false" />
    <div class="controls">
      <button @click="startManualPlay" class="btn">Play Manually</button>
      <!-- Home button -->
      <router-link to="/" class="btn home-btn">Go to Home</router-link>
      <button @click="startAIPlay" class="btn primary">Solve with AI</button>
    </div>
  </div>
</template>

<style scoped>
.play {
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