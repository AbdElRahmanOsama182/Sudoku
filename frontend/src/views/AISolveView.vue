<script>
import SudokuGrid from "../components/SudokuGrid.vue";
import { useSudokuStore } from "../stores/sudoku"; // Import the store

export default {
    components: {
        SudokuGrid,
    },
    data() {
        return {
            grid: [],
            steps: [],
            isSolving: false,
            currentStepIndex: 0,
            playing: false,
            timeElapsed: 0,
        };
    },
    computed: {
        store() {
            return useSudokuStore(); // Access the store
        },
    },
    methods: {
        async startSolving() {
            this.isSolving = true;
            this.grid = JSON.parse(JSON.stringify(this.store.grid));
            await this.store.computeSolvingSteps();
            this.currentStepIndex = this.store.currentStepIndex;
            let gridTemp = JSON.parse(JSON.stringify(this.grid));
            this.steps = this.store.solveSteps;
            this.timeElapsed = this.store.timeElapsed;
            console.log("Time elapsed: ", this.timeElapsed);
            this.isSolving = false;
        },
        async prevStep() {
            if (this.currentStepIndex > 0) {
                this.playing = true;
                this.currentStepIndex--;
                let step = JSON.parse(
                    JSON.stringify(this.steps[this.currentStepIndex])
                );
                for (let i = step.length - 1; i >= 0; i--) {
                    this.grid[step[i][0]][step[i][1]].value = null;
                    if (i > 0)
                        await new Promise((resolve) =>
                            setTimeout(resolve, 300)
                        );
                }
                this.playing = false;
            }
        },
        async nextStep() {
            if (this.currentStepIndex < this.steps.length) {
                this.playing = true;
                let step = JSON.parse(
                    JSON.stringify(this.steps[this.currentStepIndex])
                );
                console.log(step);
                for (let i = 0; i < step.length; i++) {
                    this.grid[step[i][0]][step[i][1]].value = step[i][2];
                    if (i < step.length - 1)
                        await new Promise((resolve) =>
                            setTimeout(resolve, 300)
                        );
                }
                this.currentStepIndex += 1;
                this.playing = false;
            }
        },
    },
    mounted() {
        this.startSolving();
    },
};
</script>

<template>
    <div class="ai-solve">
        <h2>AI Solver</h2>
        <SudokuGrid :grid="grid" :is-editable="false" :showNumberBar="false" />
        <div v-if="!isSolving" class="controls">
            <button
                @click="prevStep"
                :disabled="currentStepIndex <= 0 || playing"
                class="btn"
            >
                Previous
            </button>
            <!-- Home button -->
            <router-link to="/" class="btn home-btn">Go to Home</router-link>
            <button
                @click="nextStep"
                :disabled="currentStepIndex >= steps.length || playing"
                class="btn"
            >
                Next
            </button>
        </div>
        <div v-if="timeElapsed > 0" class="time">
            Time taken: {{ timeElapsed.toFixed(2) }}s
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
    color: #3ca540;
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
    font-size: 1.2rem;
    color: #3ca540;
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
