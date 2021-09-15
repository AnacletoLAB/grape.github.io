<template>
  <sidebar-menu style="top: 60px" :menu="menu" />
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
        // item
        {
          href: "/",

          title: "Ensmallen",

          // icon class
          icon: {
            element: "img",
            attributes: { src: require("../../assets/logo.png") },
            // text: ''
          },
        },
        {
          href: "/",

          title: "Enbiggen",

          // icon class
          icon: {
            element: "img",
            attributes: { src: require("../../assets/logo.png") },
            // text: ''
          },
        },
        // header item
        {
          header: true,
          title: "Main Navigation",
          // hidden: false
          // hiddenOnCollapse: true
          // class: ''
          // attributes: {}
        },
        /*
    // component item
    {
        component: componentName
        // props: componentProps
        // hidden: false
        // hiddenOnCollapse: true
    }*/
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
<style lang="scss">
.v-sidebar-menu {
}
</style>
