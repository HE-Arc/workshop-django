<script setup>
// TODO-2-7 Importer le composant NavBar et l'utiliser dans le DOM
import NavBar from "./components/NavBar.vue";
</script>

<template>
  <q-layout view="hHh Lpr fFf">
    <!-- navbar -->
    <NavBar />

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<style scoped></style>
