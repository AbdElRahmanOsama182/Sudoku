<script>
import SudokuGrid from '../components/SudokuGrid.vue';
import { createEmptyGrid } from '../utils/sudoku';

export default {
  components: {
    SudokuGrid
  },
  data() {
    return {
      grid: createEmptyGrid(),
      difficulty: 'Easy'
    }
  },
  methods: {
    generatePuzzle() {
      // TODO: Add backend integration for puzzle generation
      this.grid = createEmptyGrid();
    },
    setDifficulty(level) {
      this.difficulty = level;
      this.generatePuzzle();
    },
    proceedToPlay() {
      this.$router.push('/play');
    }
  },
  mounted() {
    this.generatePuzzle();
  }
}
</script>

<template>
  <div class="generate">
    <h2>Generate Sudoku Puzzle</h2>
    <div class="difficulty-controls">
      <button 
        v-for="level in ['Easy', 'Intermediate', 'Hard']" 
        :key="level"
        @click="setDifficulty(level)"
        :class="{ active: difficulty === level }"
        class="btn"
      >
        {{ level }}
      </button>
    </div>
    <SudokuGrid :grid="grid" :is-editable="false" />
    <div class="controls">
      <button @click="generatePuzzle" class="btn">Generate Again</button>
      <button @click="proceedToPlay" class="btn primary">Start Playing</button>
    </div>
  </div>
</template>

<style scoped>
.generate {
  text-align: center;
  padding: 2rem;
}

.difficulty-controls {
  margin-bottom: 1rem;
  display: flex;
  gap: 1rem;
  justify-content: center;
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

.btn.active {
  background: #2196F3;
  color: white;
}

.btn.primary {
  background: #4CAF50;
  color: white;
}
</style>