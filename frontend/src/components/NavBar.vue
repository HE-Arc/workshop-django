<script setup></script>

<template>
  <!-- TODO-4-0 Remplacer les TODObeverage par les bons éléments correspondants (beverages) -->

  <!-- TODO-8-0 Remplacer les TODOdetailsandstats par les bons éléments correspondants (detailsAndStats) -->
  <q-header reveal elevated class="bg-grey-10 text-white" height-hint="98">
    <q-toolbar>
      <q-icon name="coffee" size="xl"></q-icon>
      <q-toolbar-title> Caffeine Calculator </q-toolbar-title>
    </q-toolbar>

    <q-tabs align="left">
      <q-route-tab :to="{ name: 'home' }" label="Home" />
      <q-route-tab :to="{ name: 'beverages' }" label="Add beverage" />
      <q-route-tab
        :to="{ name: 'detailsAndStats' }"
        label="Details and stats"
      />
    </q-tabs>
  </q-header>
</template>

<style scoped></style>
