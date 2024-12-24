<script>
export default {
  methods: {
    navigateTo(route) {
      this.$router.push(route);
    }
  }
}
</script>

<template>
  <div class="home">
    <h1><img class="welcome-logo" src="../assets/sudoku_home.PNG" alt="Sudoku Game" /></h1>
    <div class="buttons">
      <button @click="navigateTo('/create')" class="btn">Create New Sudoku Puzzle</button>
      <button @click="navigateTo('/generate')" class="btn">Generate Random Puzzle</button>
    </div>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
  padding: 2rem;
}

.welcome-logo {
  width: auto;
  max-height: 50vh;
  display: block;
  margin: auto;
}

.buttons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 300px;
  margin: 2rem auto;
}

.btn {
  padding: 1rem;
  font-size: 1.1rem;
  border: none;
  border-radius: 4px;
  background: #4CAF50;
  color: white;
  cursor: pointer;
  transition: background 0.3s;
}

.btn:hover {
  background: #45a049;
}
</style>