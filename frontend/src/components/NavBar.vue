<script setup></script>

<template>
  <q-header reveal elevated class="bg-primary text-white" height-hint="98">
    <q-toolbar>
      <q-icon name="coffee" size="xl"></q-icon>
      <q-toolbar-title> Caffeine Calculator </q-toolbar-title>
    </q-toolbar>

    <q-tabs align="left">
      <q-route-tab :to="{ name: 'home' }" label="Home" />
      <q-route-tab :to="{ name: 'consumedItems' }" label="Consumed items" />
      <q-route-tab :to="{ name: 'caffeineItems' }" label="Caffeine items" />
    </q-tabs>
  </q-header>
</template>

<style scoped></style>
