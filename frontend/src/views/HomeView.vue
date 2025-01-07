<script setup>
// TODO-2-1 Ajouter le mot clé setup dans la balise script, cela permettra de
// travailler avec la composition API de Vue.js
// TODO-2-2 Importer axios, ref et onMounted
// TODO-2-3 Récupérer tous les users de l'API (ref var, async func, axios, onMounted)

import axios from "axios";
import { ref, onMounted } from "vue";

const users = ref([]);

const fetchUsers = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/users/");

  users.value = res.data;
};

onMounted(() => {
  fetchUsers();
});
</script>

<template>
  <!-- TODO-2-0 Installer les dépendances du projet et exécuter le serveur de dev -->
  <!-- TODO-2-4 Essayer d'afficher les users reçus, voir qu'une erreur CORS apparaît...
  ...la résoudre avec le prochain point -->
  {{ users }}
  <!-- TODO-2-6 Essayer à nouveau d'afficher les users reçus, voir que cette fois cela fonctionne -->
  <q-page padding>
    <img
      class="fixed-center"
      src="@/assets/images/coffee_dev_meme_bruce_almighty.gif"
    />
  </q-page>
</template>
