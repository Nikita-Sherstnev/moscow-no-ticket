import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";
import Schema from "../views/Schema.vue";
import Warning from "@/views/Warning.vue";
import Debug from "@/views/Debug.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/schema",
    name: "Schema",
    component: Schema,
  },
  {
    path: "/warning",
    name: "Warning",
    component: Warning,
  },
  {
    path: "/debug",
    name: "Debug",
    component: Debug,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
