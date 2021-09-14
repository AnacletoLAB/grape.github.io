import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
/*
export enum Routes {
  Home = "Home",
  Search = "Search",
  FlowDetails = "FlowDetails",
  PageNotFound = "PageNotFound",
  EditFingerprint = "EditFingerprint",
}

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: Routes.Home,
    component: () => import("../views/Home.vue"),
  },
  {
    path: "/flows/:flow_id",
    name: Routes.FlowDetails,
    component: () => import("../views/FlowDetails.vue"),
  },
  {
    path: "/fingerprint/:fingerprintid",
    name: Routes.EditFingerprint,
    component: () => import("../views/EditFingerprint.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    name: Routes.PageNotFound,
    component: () => import("../views/PageNotFound.vue"),
  },
];
*/
const routes: Array<RouteRecordRaw> = [];
const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
