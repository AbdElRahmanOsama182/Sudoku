<script>
import SudokuGrid from '../components/SudokuGrid.vue';

export default {
  components: {
    SudokuGrid
  },
  data() {
    return {
      grid: [], // Will be populated from store/props
      mode: null // 'manual' or 'ai'
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
</style>