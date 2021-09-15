<template>
  <Header />
  <div class="container-fluid flex">
    <Sidebar />
    <router-view />
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
html,
body {
  height: 100%;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  padding-right: 0;
  padding-left: 0;
  height: 100vh;
}
.container-fluid {
  position: relative; /* needed for footer positioning*/
  padding-right: 0;
  padding-left: 0;
  height: calc(100% - 60px);
}
.flex {
  display: flex;
}
@import "~bootstrap/dist/css/bootstrap.css";
</style>
