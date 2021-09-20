<template>
  <select v-on:change="setActiveVersion" v-model="activeVersion">
    <option v-for="v in versions" v-bind:key="v.key" v-bind:value="v.key">
      {{ v.value }}
    </option>
  </select>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "VersionSelect",
  data() {
    return { activeVersion: 0 };
  },
  methods: {
    setActiveVersion() {
      this.$store.commit(
        "setActiveVersion",
        this.$store.state.versions[this.activeVersion]
      );
    },
  },

  computed: {
    versions() {
      return this.$store.state.versions.map((v, i) => {
        return {
          key: i,
          value: v,
        };
      });
    },
  },
});
</script>
