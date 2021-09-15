<template>
  <Header />
  <div class="container-fluid px-0 mx-0 flex">
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

<script>
import Header from "./components/Bars/Header.vue";
import Sidebar from "./components/Bars/Sidebar.vue";
import "../main.scss";
export default {
  name: "App",
  components: {
    Header,
    Sidebar,
  },
};
</script>

<style>
@import "~bootstrap/dist/css/bootstrap.css";
</style>
