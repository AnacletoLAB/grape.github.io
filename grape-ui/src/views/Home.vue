<template>
  <div class="display-6">Welcome to Grape documentation</div>
  <p>Latest version: {{ latestVersion }}</p>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "Home",
  components: {},
  data() {
    return {
      activeVersion: "",
    };
  },
  methods: {},
  computed: {
    latestVersion() {
      const versions = this.$store.state.versions;
      if (versions.length > 0) {
        return versions[0];
      }
      console.error("No latest version stored");
      return "";
    },
  },
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
