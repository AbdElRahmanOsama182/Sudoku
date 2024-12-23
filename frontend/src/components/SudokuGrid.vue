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
    },
    showNumberBar: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      selectedCell: null // Track the currently selected cell
    };
  },
  methods: {
    selectCell({ row, col }) {
      this.selectedCell = { row, col };
    },
    updateSelectedCell(value) {
      if (this.selectedCell) {
        this.$emit('update-cell', {
          row: this.selectedCell.row,
          col: this.selectedCell.col,
          value
        });
        this.selectedCell = null; // Deselect after updating
      }
    }
  }
};
</script>

<template>
  <div class="grid-wrapper">
    <div class="grid">
      <div v-for="(row, rowIndex) in grid" :key="rowIndex" class="row">
        <SudokuCell
          v-for="(cell, colIndex) in row"
          :key="colIndex"
          :value="cell.value"
          :is-fixed="cell.isFixed"
          :row-index="rowIndex"
          :col-index="colIndex"
          :is-selected="selectedCell && selectedCell.row === rowIndex && selectedCell.col === colIndex"
          @select-cell="selectCell"
        />
      </div>
    </div>
    <div class="number-bar" v-if="showNumberBar">
      <button
        v-for="num in 9"
        :key="num"
        @click="updateSelectedCell(num)"
        class="number-btn"
      >
        {{ num }}
      </button>
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

.number-bar {
  margin-top: 16px;
  display: flex;
  justify-content: center;
  gap: 8px;
}

.number-btn {
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  background: #f0f0f0;
  font-size: 16px;
  font-weight: bold;
}

.number-btn:hover {
  background: #2196F3;
  color: white;
}
</style>