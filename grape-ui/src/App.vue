<template>
  <Header />
  <div class="container-fluid px-0 mx-0 flex" id="sidebar-container">
    <Sidebar />
    <div class="container-fluid px-0 mx-0">
      <div class="container px-0 py-0">
        <div class="row px-0 py-3">
          <div
            class="col border border-secondary-50 bg-light rounded-3 px-0 py-0"
          >
            <router-view />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import Header from "./components/Bars/Header.vue";
import Sidebar from "./components/Bars/Sidebar.vue";
import "../main.scss";
import { defineComponent } from "vue";

import { EntityService } from "../gen";

export default defineComponent({
  name: "App",
  components: {
    Header,
    Sidebar,
  },
  methods: {
    async getVersions() {
      try {
        const versions = await (
          (await EntityService.getMethodController1()) as string[]
        ).sort((a, b) => (a < b ? 1 : -1));
        this.$store.commit("setVersions", versions);
        this.$store.commit("setActiveVersion", versions[0]);
      } catch (err) {
        if (err instanceof Error) {
          console.error("Error while saving versions!\n" + err.toString());
        } else {
          console.error("Error while saving versions! Unknown type error");
        }
      }
    },
  },

  created() {
    this.getVersions();
  },
});
</script>

<style>
@import "~bootstrap/dist/css/bootstrap.css";
</style>
