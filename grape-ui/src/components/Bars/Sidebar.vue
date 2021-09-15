<template>
  <sidebar-menu relative="true" :menu="menu" />
</template>
<script lang="ts">
import "../../../main.scss";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Sidebar",
  data() {
    return {
      menu: [
        {
          header: "Grape",
          hiddenOnCollapse: true,
          href: { path: "/" },
        },
        {
          title: "Overview",
          hiddenOnCollapse: true,
          href: { path: "/" },
        },
        {
          header: "Modules",
          hiddenOnCollapse: true,
        },
        {
          href: "/",

          title: "Ensmallen",
          hiddenOnCollapse: true,
          // icon class
          icon: {
            element: "img",
            attributes: { src: require("../../assets/logo.png") },
          },
        },
        {
          href: "/",

          title: "Enbiggen",
          hiddenOnCollapse: true,
          icon: {
            element: "img",
            attributes: { src: require("../../assets/logo.png") },
          },
        },
      ],
    };
  },

  computed: {
    iconUrl() {
      return require("../../assets/logo.png");
    },
  },
});
</script>
<style lang="scss"></style>
