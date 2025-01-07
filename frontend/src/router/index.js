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
    // TODO-4-0 Remplacer les TODObeverage par les bons éléments correspondants (beverages)
    {
      path: "/beverages",
      name: "beverages",
      // NOTE: route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/BeverageView.vue"),
    },
    // TODO-5-0 Remplacer les TODOcreatebeverage par les bons éléments correspondants (beverages.create)
    {
      path: "/beverates/create",
      name: "beverages.create",
      component: () => import("../views/CreateBeverageView.vue"),
    },
    // TODO-8-0 Remplacer les TODOdetailsandstats par les bons éléments correspondants (detailsAndStats) -->
    {
      path: "/details-and-stats",
      name: "detailsAndStats",
      component: () => import("../views/DetailsAndStatsView.vue"),
    },
  ],
});

export default router;
