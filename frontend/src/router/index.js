import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/details-and-stats",
      name: "detailsAndStats",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/DetailsAndStatsView.vue"),
    },
    {
      path: "/beverages",
      name: "beverages",
      component: () => import("../views/BeverageView.vue"),
    },
    {
      path: "/beverages/create",
      name: "beverages.create",
      component: () => import("../views/CreateBeverageView.vue"),
    },
  ],
});

export default router;
