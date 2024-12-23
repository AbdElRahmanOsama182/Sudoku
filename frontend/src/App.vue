<template>
    <div class="app">
        <router-view></router-view>
    </div>
</template>
<script>
export default {
    name: "App",
    created() {
        const initialRoute = sessionStorage.getItem("initialRoute");
        if (initialRoute) {
            this.$router.push(initialRoute);
        }
    },
    beforeDestroy() {
        sessionStorage.removeItem("initialRoute");
    },
};
</script>
<style>
.app {
    font-family: Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
}
</style>
