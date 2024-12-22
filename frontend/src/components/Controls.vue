<template>
  <div class="flex flex-col gap-4 mt-4">
    <!-- Mode Selection -->
    <div class="flex gap-4 justify-center">
      <button 
        @click="startCreating"
        class="px-4 py-2 bg-blue-500 text-white rounded"
        :disabled="store.isSolvingMode"
      >
        Create New Puzzle
      </button>
      <button 
        @click="startGenerating"
        class="px-4 py-2 bg-green-500 text-white rounded"
        :disabled="store.isSolvingMode"
      >
        Generate Puzzle
      </button>
    </div>

    <!-- Difficulty Selection -->
    <div v-if="showDifficulty" class="flex gap-4 justify-center">
      <button 
        v-for="diff in difficulties"
        :key="diff"
        @click="selectDifficulty(diff)"
        class="px-4 py-2 bg-purple-500 text-white rounded"
        :class="{ 'opacity-50': store.difficulty !== diff }"
      >
        {{ diff }}
      </button>
    </div>

    <!-- Grid Controls -->
    <div v-if="showGridControls" class="flex gap-4 justify-center">
      <button 
        @click="clearGrid"
        class="px-4 py-2 bg-red-500 text-white rounded"
      >
        Clear
      </button>
      <button 
        @click="validateAndProceed"
        class="px-4 py-2 bg-blue-500 text-white rounded"
      >
        Done Creating
      </button>
    </div>

    <!-- Solving Controls -->
    <div v-if="showSolvingControls" class="flex gap-4 justify-center">
      <button 
        @click="solveManually"
        class="px-4 py-2 bg-blue-500 text-white rounded"
      >
        Solve Manually
      </button>
      <button 
        @click="solveWithAI"
        class="px-4 py-2 bg-green-500 text-white rounded"
      >
        Solve with AI
      </button>
    </div>

    <!-- AI Navigation Controls -->
    <div v-if="showAIControls" class="flex gap-4 justify-center">
      <button 
        @click="prevStep"
        class="px-4 py-2 bg-gray-500 text-white rounded"
        :disabled="!canGoPrev"
      >
        Previous
      </button>
      <button 
        @click="nextStep"
        class="px-4 py-2 bg-gray-500 text-white rounded"
        :disabled="!canGoNext"
      >
        Next
      </button>
      <div v-if="store.timeElapsed > 0" class="text-gray-700">
        Time: {{ (store.timeElapsed / 1000).toFixed(2) }}s
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import { useSudokuStore } from '../stores/sudoku';
import type { Difficulty } from '../types/sudoku';

const store = useSudokuStore();

const difficulties: Difficulty[] = ['Easy', 'Intermediate', 'Hard'];

const showDifficulty = computed(() => !store.isCreatingMode && !store.isSolvingMode);
const showGridControls = computed(() => store.isCreatingMode);
const showSolvingControls = computed(() => !store.isCreatingMode && !store.isSolvingMode);
const showAIControls = computed(() => store.isAISolving);
const canGoPrev = computed(() => store.currentStepIndex > 0);
const canGoNext = computed(() => store.currentStepIndex < store.solveSteps.length - 1);

const startCreating = () => {
  store.isCreatingMode = true;
  store.clearGrid();
};

const startGenerating = () => {
  store.generatePuzzle();
};

const selectDifficulty = (difficulty: Difficulty) => {
  store.setDifficulty(difficulty);
};

const clearGrid = () => {
  store.clearGrid();
};

const validateAndProceed = () => {
  if (store.validateGrid()) {
    store.isCreatingMode = false;
  } else {
    alert('Invalid Sudoku configuration! Please check your input.');
  }
};

const solveManually = () => {
  store.isSolvingMode = true;
};

const solveWithAI = () => {
  store.isAISolving = true;
  // Placeholder for AI solving implementation
};

const prevStep = () => {
  if (store.currentStepIndex > 0) {
    store.currentStepIndex--;
  }
};

const nextStep = () => {
  if (store.currentStepIndex < store.solveSteps.length - 1) {
    store.currentStepIndex++;
  }
};
</script>