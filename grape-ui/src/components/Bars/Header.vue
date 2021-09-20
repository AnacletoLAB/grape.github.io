<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark" id="header">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand px-2" href="#">
        <img :src="iconUrl" class="d-inline-block" /> Grape
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="navbarDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Dropdown
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><hr class="dropdown-divider" /></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link disabled">Disabled</a>
          </li>
        </ul>
        <div class="mb-2 mb-lg-0 px-2">
          <VersionSelect :defaultValue="latestVersion()" />
        </div>
        <div class="mb-2 mb-lg-0 px-2">
          <SearchBox defaultText="Search..." />
        </div>
      </div>
    </div>
  </nav>
</template>
<script lang="ts">
import "../../../main.scss";
import { defineComponent } from "vue";
import SearchBox from "../Forms/SearchBox.vue";
import VersionSelect from "../Forms/VersionSelect.vue";

export default defineComponent({
  name: "Header",
  components: {
    SearchBox,
    VersionSelect,
  },
  data() {
    return {};
  },
  methods: {
    async latestVersion() {
      const versions = this.$store.state.versions;
      if (versions.length > 0) {
        return versions[0];
      }
      console.error("No latest version stored");
      return "";
    },
  },
  computed: {
    iconUrl() {
      return require("../../assets/logo.png");
    },
  },
});
</script>
<style scoped>
select {
  color: white;
  background: #222222;
  outline: none;
  border: 0;
  padding: 4px;
}

a {
  font-weight: bold;
  color: #f1f1f1;
  text-decoration: none;
}
.router-link-exact-active {
  color: #f1f1f1;
  text-decoration: none;
}
</style>
