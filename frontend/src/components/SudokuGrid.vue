<script>
import SudokuCell from './SudokuCell.vue';

export default {
  components: {
    SudokuCell
  },
  props: {
    grid: {
      type: Array,
      required: true
    },
    isEditable: {
      type: Boolean,
      default: true
    }
  },
  methods: {
    handleCellUpdate({ row, col, value }) {
      this.$emit('update-cell', { row, col, value });
    }
  }
}
</script>

<template>
  <div class="grid">
    <div v-for="(row, rowIndex) in grid" :key="rowIndex" class="row">
      <SudokuCell
        v-for="(cell, colIndex) in row"
        :key="colIndex"
        :value="cell.value"
        :is-fixed="cell.isFixed"
        :row-index="rowIndex"
        :col-index="colIndex"
        @update="handleCellUpdate"
      />
    </div>
  </div>
</template>

<style scoped>
.grid {
  display: inline-block;
  padding: 8px;
  background: #f0f0f0;
  border: 2px solid #333;
}

.row {
  display: flex;
}

.row:nth-child(3n) {
  border-bottom: 2px solid #333;
}

.row:last-child {
  border-bottom: none;
}

.cell:nth-child(3n) {
  border-right: 2px solid #333;
}

.cell:last-child {
  border-right: none;
}
</style>