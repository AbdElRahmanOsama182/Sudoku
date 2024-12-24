<script>
export default {
    props: {
        value: {
            type: Number,
            default: null,
        },
        isFixed: {
            type: Boolean,
            default: false,
        },
        rowIndex: {
            type: Number,
            required: true,
        },
        colIndex: {
            type: Number,
            required: true,
        },
        isSelected: {
            type: Boolean,
            default: false,
        },
        isIncorrect: {
            type: Boolean,
            default: false
        }
    },
    methods: {
        selectCell() {
            if (!this.isFixed) {
                this.$emit("select-cell", {
                    row: this.rowIndex,
                    col: this.colIndex,
                });
            }
        },
        toggleselectCell() {
            if (!this.isFixed) {
                this.$emit("toggle-select-cell", {
                    row: this.rowIndex,
                    col: this.colIndex,
                });
            }
        },
    },
};
</script>

<template>
    <div
        class="cell"
        :class="{ isfixed: isFixed, selected: isSelected, isincorrect: isIncorrect}"
        @click="toggleselectCell"
    >
        <span>{{ value }}</span>
    </div>
</template>

<style scoped>
.cell {
    width: 40px;
    height: 40px;
    border: 1px solid #ccc;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.cell.isfixed {
    background-color: #f0f0f0; /* Different background color */
    font-weight: bold; /* Mark fixed cells with bold text */
}

.cell.selected {
    background-color: #7f9eb6;
}

.cell.isincorrect {
    background-color: #f8d7da; /* Light red background */
    border-color: #f5c2c7; /* Light red border */
    color: #842029; /* Dark red text for visibility */
}
</style>
