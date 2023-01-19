<script setup>
// TODO-4-1 Importer axios, ref et onMounted
import axios from "axios";
import { ref, onMounted } from "vue";

// TODO-9-1 importer le composant ErrorBanner, l'utiliser dans le DOM et tester le résultat
import ErrorBanner from "../components/ErrorBanner.vue";

// TODO-4-2 Récupérer tous les caffeine items de l'API (ref var, async func, axios, onMounted)
const caffeineItems = ref([]);

const fetchCaffeineItems = async () => {
  const result = await axios.get("http://127.0.0.1:8000/api/caffeine-items/");

  caffeineItems.value = result.data;
};

// TODO-4-5 Récupérer tous les users de l'API (ref var, async func, axios, onMounted)
const users = ref([]);
const currentUser = ref(null);

const fetchUsers = async () => {
  users.value = (await axios.get("http://127.0.0.1:8000/api/users/")).data;
};

// TODO-7-2 Créer une variable nommée errors permettant de récupérer les erreurs de l'appel (init à null)
const errors = ref(null);

// TODO-7-0 Permettre d'enregistrer des consumed items (axios post, form fields, date.now, url vs id)
const submit = async (caffeine_item) => {
  try {
    errors.value = null;

    const res = await axios.post("http://127.0.0.1:8000/api/consumed-items/", {
      user: currentUser.value?.url,
      caffeine_item: caffeine_item.url,
      consumed_number: 1,
      consumption_date: new Date(),
    });

    console.log(res);
  } catch (error) {
    errors.value = error.response.data;
    console.log(error.response.data);
  }
};

// Execute le code quand le composant démarre
onMounted(() => {
  fetchCaffeineItems();
  fetchUsers();
});
</script>

<template>
  <!-- TODO-4-3 Afficher les caffeine items reçus de l'API -->
  <!-- {{ caffeineItems }} -->

  <!-- TODO-4-4 Remplacer les TODOcaffeine par les bons éléments correspondants -->
  <!-- TODO-4-6 Remplacer les TODOuser par les bons éléments correspondants -->

  <!-- TODO-5-0 Remplacer les TODOcreatebeverage par les bons éléments correspondants (beverages.create) -->

  <!-- TODO-7-1 Remplacer les TODOconsumed par les bons éléments correspondants -->
  <!-- TODO-7-3 Afficher le contenu de la var errors ici pour l'instant -->
  <q-page padding>
    <ErrorBanner :errors="errors" />

    <q-select
      v-model="currentUser"
      option-value="id"
      option-label="username"
      :options="users"
      label="User"
      outlined
    />

    <div class="text-left q-my-md">
      <q-btn color="primary" :to="{ name: 'beverages.create' }">
        <q-icon left size="xl" name="mdi-plus-box" />
        <div>Create a new beverage</div>
      </q-btn>
    </div>

    <div class="row">
      <div
        class="text-center col-12 col-sm-6 col-md-4 col-lg-3 q-pa-sm"
        v-for="(item, index) in caffeineItems"
        :key="index"
      >
        <q-card class="my-card">
          <q-card-section>
            <div class="text-h4">{{ item.name }}</div>
            <div class="text-subtitle2">{{ item.description }}</div>
          </q-card-section>

          <q-separator inset />

          <q-card-section>
            <div>Serving size</div>
            <q-badge class="text-h6 q-pa-xs" color="purple">
              {{ item.serving_size_in_ml }} ml
            </q-badge>
            <div class="q-mt-md">Caffeine amount</div>
            <q-badge class="text-h6 q-pa-xs" color="teal">
              {{ item.caffeine_amount_in_mg }} mg
            </q-badge>
          </q-card-section>

          <q-separator inset />

          <q-card-actions vertical>
            <q-btn
              push
              @click="submit(item)"
              class="q-ma-xs"
              color="primary"
              dense
            >
              <q-icon left size="xl" name="mdi-numeric-positive-1" />
              <div>I drank this one today</div>
            </q-btn>
          </q-card-actions>
        </q-card>
      </div>
    </div>

    <div class="text-right q-my-md">
      <!-- NOTE: What's "_blank"? source https://www.freecodecamp.org/news/how-to-use-html-to-open-link-in-new-tab/ -->
      <q-btn
        color="grey-9"
        target="_blank"
        href="https://www.caffeineinformer.com/the-caffeine-database"
      >
        The values are comming from: caffeineinformer.com
        <q-icon right size="xs" name="mdi-arrow-top-right-bold-box-outline" />
      </q-btn>
    </div>
  </q-page>
</template>

<style scoped></style>
