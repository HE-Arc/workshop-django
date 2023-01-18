import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

// TODO-4-0 Remplacer les TODObeverage par les bons éléments correspondants (beverages)

// TODO-5-0 Remplacer les TODOcreatebeverage par les bons éléments correspondants (beverages.create)

// TODO-8-0 Remplacer les TODOdetailsandstats par les bons éléments correspondants (detailsAndStats) -->

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/beverages",
      name: "beverages",
      // NOTE: route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/BeverageView.vue"),
    },
    {
      path: "/TODOcreatebeverage",
      name: "TODOcreatebeverage",
      component: () => import("../views/CreateBeverageView.vue"),
    },
    {
      path: "/TODOdetailsandstats",
      name: "TODOdetailsandstats",
      component: () => import("../views/DetailsAndStatsView.vue"),
    },
  ],
});

export default router;
