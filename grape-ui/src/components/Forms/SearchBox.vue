<template>
  <form class="d-flex">
    <input
      class="form-control bg-dark me-1 text-white"
      type="search"
      :placeholder="defaultText"
      v-model="keyword"
      @change="onChange()"
      :aria-label="defaultText"
    />
    <button
      class="btn bg-dark btn-outline-light"
      @click="onButtonClick()"
      type="submit"
    >
      <BIconSearch />
    </button>
  </form>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { BIconSearch } from "bootstrap-icons-vue";
export default defineComponent({
  name: "SearchBox",
  components: {
    BIconSearch,
  },
  data() {
    return {
      keyword: "",
    };
  },
  props: {
    defaultText: { type: String, required: true },
  },
  methods: {
    onChange(): void {
      this.$emit("updated", this.keyword);
    },
    onButtonClick(): void {
      this.$emit("updated", this.keyword);
    },
  },
});
</script>

<style lang="css" scoped>
.btn-outline-light:hover,
.btn-outline-light:focus,
.btn-outline-light:active,
.btn-outline-light.active,
.open > .dropdown-toggle.btn-outline-light {
  color: #b4b4b4;
  border-color: #b4b4b4; /*hack to change button overlay color*/
}
</style>
