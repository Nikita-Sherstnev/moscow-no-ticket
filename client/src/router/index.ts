import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Home from "../views/Home.vue";
import Schema from "../views/Schema.vue";
import Warning from "@/views/Warning.vue";

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
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
