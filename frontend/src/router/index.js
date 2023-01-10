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
      path: "/consumed-items",
      name: "consumedItems",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/ConsumedItemListView.vue"),
    },
    {
      path: "/consumed-items/create",
      name: "consumedItems.create",
      component: () => import("../views/ConsumedItemCreateView.vue"),
    },
    {
      path: "/caffeine-items",
      name: "caffeineItems",
      component: () => import("../views/CaffeineItemListView.vue"),
    },
  ],
});

export default router;
