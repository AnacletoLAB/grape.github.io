import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { store } from "./store";
//import { OpenAPI } from "../gen";
import "bootstrap";
import * as Configs from "../config";
/*
if (process.env.NODE_ENV === "production") {
  OpenAPI.BASE = Configs.ApiBaseAddress;
}*/

createApp(App).use(router).use(store).mount("#app");
