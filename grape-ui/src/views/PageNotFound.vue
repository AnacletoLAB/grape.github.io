<template>
  <h1>404 Page not found</h1>
  <h2><router-link to="/">Back to Home</router-link></h2>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "PageNotFound",
  components: {},
  computed: {},
});
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
