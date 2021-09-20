import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { store } from "./store";
import { OpenAPI } from "../gen";
import "bootstrap";
import VueSidebarMenu from "vue-sidebar-menu";
import "vue-sidebar-menu/dist/vue-sidebar-menu.css";
import * as Configs from "../config";
import { addMocks } from "./mocks/mock";

if (process.env.NODE_ENV === "production") {
  OpenAPI.BASE = Configs.ApiBaseAddress;
} else {
  addMocks();
}

createApp(App).use(router).use(store).use(VueSidebarMenu).mount("#app");
