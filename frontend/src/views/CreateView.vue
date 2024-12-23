<script>
import SudokuGrid from "../components/SudokuGrid.vue";
import { createEmptyGrid } from "../utils/sudoku";
import { useSudokuStore } from "../stores/sudoku";

export default {
    components: {
        SudokuGrid,
    },
    data() {
        return {
            grid: createEmptyGrid(),
        };
    },
    methods: {
        clearGrid() {
            this.grid = createEmptyGrid();
        },
        updateCell({ row, col, value }) {
            this.grid[row][col].value = value;
        },
        async validateAndProceed() {
            const store = useSudokuStore();
            store.grid = this.grid;
            try {
                const response = await store.validateGrid();
                console.log(response);
                alert(response.message);
                if (response.success) {
                    store.isCreatingMode = false;
                    store.solutionGrid = response.solution;
                    for (let i = 0; i < this.grid.length; i++) {
                        for (let j = 0; j < this.grid[i].length; j++) {
                            // Mark each cell as fixed if it contains value
                            if (this.grid[i][j].value !== null)
                                this.grid[i][j].isFixed = true;
                        }
                    }
                    store.grid = this.grid;
                    this.$router.push("/play");
                }
            } catch (error) {
                alert("Error validating the puzzle");
            }
        },
    },
};
</script>

<template>
    <div class="create">
        <h2>Create New Sudoku</h2>
        <SudokuGrid
            :grid="grid"
            :showNumberBar="true"
            @update-cell="updateCell"
        />
        <div class="controls">
            <button @click="clearGrid" class="btn">Clear Grid</button>
            <!-- Home button -->
            <router-link to="/" class="btn home-btn">Go to Home</router-link>
            <button @click="validateAndProceed" class="btn primary">
                Done Creating
            </button>
        </div>
    </div>
</template>

<style scoped>
.create {
    text-align: center;
    padding: 2rem;
}

.create h2 {
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

.btn.primary {
    background: #4caf50;
    color: white;
}
.home-btn {
    background-color: #007bff; /* Blue color for the home button */
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
