import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";

export enum Routes {
  Home = "Home",
  Method = "Method",
  PageNotFound = "PageNotFound",
}

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: Routes.Home,
    component: () => import("../views/Home.vue"),
  },
  {
    path: "/method/:method_id",
    name: Routes.Method,
    component: () => import("../views/Method.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    name: Routes.PageNotFound,
    component: () => import("../views/PageNotFound.vue"),
  },
];
const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
