<script>
import SudokuGrid from '../components/SudokuGrid.vue';
import { useSudokuStore } from '../stores/sudoku'; // Import the store

export default {
  components: {
    SudokuGrid
  },
  data() {
    return {
      steps: [],
      isSolving: false
    }
  },
  computed: {
    store() {
      return useSudokuStore(); // Access the store
    },
    grid() {
      return this.store.grid;
    },
    timeElapsed() {
      return this.store.timeElapsed;
    },
    currentStepIndex() {
      return this.store.currentStepIndex;
    }
  },
  methods: {
    async startSolving() {
      this.isSolving = true;
      this.store.computeSolvingSteps();
      this.store.solveSteps.forEach((step) => {
        // For each step, apply the moves and store the grid state
        step.forEach(([row, col, value]) => {
          this.grid[row][col] = value; // Update the grid based on the move
        });

        // Push the grid state into steps
        this.steps.push(JSON.parse(JSON.stringify(this.grid)));
      });
    },
    prevStep() {
      if (this.currentStepIndex > 0) {
        this.currentStepIndex--;
        this.grid = JSON.parse(JSON.stringify(this.steps[this.currentStepIndex]));
      }
    },
    nextStep() {
      if (this.currentStepIndex < this.steps.length - 1) {
        this.currentStepIndex++;
        this.grid = JSON.parse(JSON.stringify(this.steps[this.currentStepIndex]));
      }
    }
  },
  mounted() {
    this.startSolving();
  }
}
</script>

<template>
  <div class="ai-solve">
    <h2>AI Solver</h2>
    <SudokuGrid 
      :grid="grid"
      :is-editable="false"
      :showNumberBar="false"
    />
    <div v-if="!isSolving" class="controls">
      <button 
        @click="prevStep" 
        :disabled="currentStepIndex <= 0"
        class="btn"
      >
        Previous
      </button>
      <!-- Home button -->
      <router-link to="/" class="btn home-btn">Go to Home</router-link>
      <button 
        @click="nextStep"
        :disabled="currentStepIndex >= steps.length - 1"
        class="btn"
      >
        Next
      </button>
    </div>
    <div v-if="timeElapsed > 0" class="time">
      Time taken: {{ (timeElapsed / 1000).toFixed(2) }}s
    </div>
  </div>
</template>

<style scoped>
.ai-solve {
  text-align: center;
  padding: 2rem;
}

.ai-solve h2 {
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
  opacity: 1;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.time {
  margin-top: 1rem;
  font-weight: bold;
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