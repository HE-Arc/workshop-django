<script setup>
// TODO-9-0 Ajouter une props nommée errors et remplacer les TODOerrors par les éléments correspondants
</script>

<template>
  <q-banner v-if="TODOerrors" inline-actions class="q-mb-lg text-white bg-red">
    <div class="text-h6">
      <q-icon left size="md" name="mdi-alert" />
      Input errors
    </div>

    <q-separator dark class="q-my-md" inset />

    <div class="self-center" v-for="(item, key) in TODOerrors" :key="key">
      {{ key }}
      <ul>
        <li v-for="(err, index) in item" :key="index">{{ err }}</li>
      </ul>
    </div>
  </q-banner>
</template>
