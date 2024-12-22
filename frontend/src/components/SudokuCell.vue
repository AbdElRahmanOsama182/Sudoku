<script>
export default {
  props: {
    value: {
      type: Number,
      default: null
    },
    isFixed: {
      type: Boolean,
      default: false
    },
    rowIndex: {
      type: Number,
      required: true
    },
    colIndex: {
      type: Number,
      required: true
    }
  },
  methods: {
    handleInput(event) {
      const value = event.target.value;
      if (value === '' || (value >= 1 && value <= 9)) {
        this.$emit('update', {
          row: this.rowIndex,
          col: this.colIndex,
          value: value === '' ? null : parseInt(value)
        });
      }
    }
  }
}
</script>

<template>
  <div class="cell" :class="{ 'fixed': isFixed }">
    <input 
      v-if="!isFixed"
      type="number"
      :value="value || ''"
      min="1"
      max="9"
      @input="handleInput"
      class="cell-input"
    />
    <span v-else>{{ value }}</span>
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
}

.cell.fixed {
  background-color: #f0f0f0;
}

.cell-input {
  width: 100%;
  height: 100%;
  text-align: center;
  border: none;
  outline: none;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>