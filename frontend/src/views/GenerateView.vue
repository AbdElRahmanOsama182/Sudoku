<script>
import SudokuGrid from "../components/SudokuGrid.vue";
import { useSudokuStore } from "../stores/sudoku";
// import { createEmptyGrid } from '../utils/sudoku';

export default {
    components: {
        SudokuGrid,
    },
    data() {
        return {
            difficulty: "Easy",
        };
    },
    computed: {
        store() {
            return useSudokuStore(); // Access the store
        },
    },
    methods: {
        async generatePuzzle() {
            this.store.generatePuzzle();
            console.log(this.store.grid);
        },
        setDifficulty(level) {
            this.difficulty = level;
            this.store.setDifficulty(level);
            this.generatePuzzle();
        },
        async proceedToPlay() {
            try {
                const response = await this.store.validateGrid();
                // alert(response.message);
                console.log(response);
                if (response.success) {
                    this.store.solutionGrid = response.solution;
                    this.$router.push("/play");
                }
            } catch (error) {
                console.log("Error validating and proceeding");
            }
        },
    },
    mounted() {
        this.generatePuzzle();
    },
};
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
        <SudokuGrid
            :grid="this.store.grid"
            :is-editable="false"
            :showNumberBar="false"
        />
        <div class="controls">
            <button @click="generatePuzzle" class="btn">Generate Again</button>
            <!-- Home button -->
            <router-link to="/" class="btn home-btn">Go to Home</router-link>
            <button @click="proceedToPlay" class="btn primary">
                Start Playing
            </button>
        </div>
    </div>
</template>

<style scoped>
.generate {
    text-align: center;
    padding: 2rem;
}
.generate h2 {
    font-size: 2.2rem;
    font-weight: normal;
    color: #3ca540;
    text-align: center;
    margin-bottom: 20px;
    letter-spacing: 1px;
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
    background: #2196f3;
    color: white;
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
