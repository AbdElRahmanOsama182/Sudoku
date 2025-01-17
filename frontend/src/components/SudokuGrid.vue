<script>
import SudokuCell from "./SudokuCell.vue";

export default {
    components: {
        SudokuCell,
    },
    props: {
        grid: {
            type: Array,
            required: true,
        },
        isEditable: {
            type: Boolean,
            default: true,
        },
        showNumberBar: {
            type: Boolean,
            default: true,
        },
        incorrectCell: {
            type: Array,
            default: () => Array.from({ length: 9 }, () => Array(9).fill(false))
        }
    },
    data() {
        return {
            selectedCell: null, // Track the currently selected cell
        };
    },
    methods: {
        selectCell({ row, col }) {
            this.selectedCell = { row, col };
        },
        toggleSelectCell({ row, col }) {
            if (this.selectedCell) {
                if (
                    this.selectedCell.row === row &&
                    this.selectedCell.col === col
                ) {
                    this.selectedCell = null; // Deselect if already selected
                } else {
                    this.selectedCell = { row, col }; // Select a different cell
                }
            } else {
                this.selectedCell = { row, col }; // Select if no cell is selected
            }
        },
        updateSelectedCell(value) {
            if (this.selectedCell) {
                this.$emit("update-cell", {
                    row: this.selectedCell.row,
                    col: this.selectedCell.col,
                    value,
                });
                this.selectedCell = null; // Deselect after updating
            }
        },
        clearSelectedCell() {
            if (this.selectedCell) {
                this.$emit("update-cell", {
                    row: this.selectedCell.row,
                    col: this.selectedCell.col,
                    value: null, // Clear the value
                });
                this.selectedCell = null; // Deselect after clearing
            }
        },
    },
};
</script>

<template>
    <div class="grid-wrapper">
        <div class="grid">
            <div
                v-for="(row, rowIndex) in this.grid"
                :key="rowIndex"
                class="row"
            >
                <SudokuCell
                    v-for="(cell, colIndex) in row"
                    :key="colIndex"
                    :value="cell.value"
                    :is-fixed="cell.isFixed"
                    :row-index="rowIndex"
                    :col-index="colIndex"
                    :is-selected="
                        selectedCell &&
                        selectedCell.row === rowIndex &&
                        selectedCell.col === colIndex
                    "
                    :isIncorrect="this.incorrectCell[rowIndex][colIndex]"
                    @select-cell="selectCell"
                    @toggle-select-cell="toggleSelectCell"
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
            <button @click="clearSelectedCell" class="clear-btn">
                <span role="img" aria-label="clear">❌</span>
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
    border-right: 1px solid #ccc;
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
    background: #2196f3;
    color: white;
}
.clear-btn {
    width: 40px;
    height: 40px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    background: #f0f0f0;
    font-size: 16px;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
}

.clear-btn:hover {
    background: #ff5722;
    color: white;
}
</style>
