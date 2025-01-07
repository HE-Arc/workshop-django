<script setup>
// TODO-8-1 Importer axios, ref et onMounted, data
import axios from "axios";
import { ref, onMounted } from "vue";
import { date } from "quasar";
// TODO-8-2 Récupérer tous les consumed items et users de l'API (ref var, async func, axios, onMounted)
const users = ref([]);


const fetchUsers = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/users/");

  users.value = res.data;
};

const rows = ref([]);

const fetchConsumedItems = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/consumed-items/");

  rows.value = [];

  res.data.forEach((element) => {
    rows.value.push({
      id: element.id,
      consumption_date: element.consumption_date,
      user: element.user_obj.username,
      caffeine_item: element.caffeine_item_obj.name,
      serving_size_in_ml: element.caffeine_item_obj.serving_size_in_ml,
      caffeine_amount_in_mg: element.caffeine_item_obj.caffeine_amount_in_mg,
    });
  });
};

onMounted(() => {
  fetchUsers();
  fetchConsumedItems();
});

// TODO-8-5 Ajouter les var suivantes : currentRows (Array), user (null)
const user = ref(null);
    
const currentRows = ref([]);

// TODO-8-6 Créer une fonction permettant de mettre à jour le tableau afin de n'afficher uniquement
// les éléments de l'utilisateur sélectionné
const updateVal = () => {
  const res = [];
  servingSizeTotal.value = 0;
  caffeineAmountTotal.value = 0;
  servingSizeToday.value = 0;
  caffeineAmountToday.value = 0;

  rows.value.forEach((row) => {
    if (row.user == user.value.username) {
      res.push(row);
      servingSizeTotal.value += row.serving_size_in_ml;
      caffeineAmountTotal.value += row.caffeine_amount_in_mg;

      const rowDate = new Date(row.consumption_date);
      const currentDate = new Date();
      if (
        rowDate.getFullYear() === currentDate.getFullYear() &&
        rowDate.getMonth() === currentDate.getMonth() &&
        rowDate.getDate() === currentDate.getDate()
      ) {
        servingSizeToday.value += row.serving_size_in_ml;
        caffeineAmountToday.value += row.caffeine_amount_in_mg;
      }
    }
  });

  currentRows.value = res;
};
// TODO-8-8 Ajouter les var suivantes : servingSizeTotal (null), caffeineAmountTotal (null),
// servingSizeToday(null), caffeineAmountToday(null)
const servingSizeTotal = ref(null);
const caffeineAmountTotal = ref(null);
const servingSizeToday = ref(null);
const caffeineAmountToday = ref(null);
// TODO-8-9 Calculer la valeur des nouvelles variables dans la fonction de mise à jour des éléments du tableau

// TODO-8-11 Créer une fonction permettant de supprimer un élément dans le tableau
const remove = async (id) => {
  await axios.delete(`http://127.0.0.1:8000/api/consumed-items/${id}/`);

  await fetchConsumedItems();

  updateVal();
};
const initialPagination = {
  sortBy: "id",
  descending: true,
};

const columns = [
  {
    name: "user",
    label: "User",
    align: "left",
    field: (row) => row.user,
    sortable: true,
  },
  {
    name: "caffeineitem",
    label: "Item",
    align: "left",
    field: (row) => row.caffeine_item,
    sortable: true,
  },
  {
    name: "caffeineservingsize",
    label: "Service size",
    align: "left",
    field: (row) => row.serving_size_in_ml,
    sortable: true,
  },
  {
    name: "caffeineamount",
    label: "Caffeine amount",
    align: "left",
    field: (row) => row.caffeine_amount_in_mg,
    sortable: true,
  },
  {
    name: "consumptiondate",
    label: "Date",
    align: "left",
    field: (row) =>
      date.formatDate(new Date(row.consumption_date), "HH:mm:ss DD.MM.YYYY"),
    format: (val) => `${val}`,
    required: true,
    sortable: true,
  },
  {
    name: "id",
    label: "Actions",
    align: "left",
    field: (row) => row.id,
    sortable: false,
  },
];
</script>

<template>
  <!-- TODO-8-3 Afficher les consumed items reçus de l'API -->
  {{ rows }}
  <!-- TODO-8-4 Remplacer les TODOconsumed par les bons éléments correspondants -->

  <!-- TODO-8-7 Remplacer les TODOuser par les bons éléments correspondants et remplacer rows
  par currentRows dans la table en dessous afin de n'afficher que les éléments de l'utilisateur actuel -->

  <!-- TODO-8-10 Remplacer les TODOToday par les bons éléments correspondants -->
  <!-- TODO-8-12 Remplacer les TODOremove par les bons éléments correspondants -->
  <q-page padding>
    <q-select
      v-model="user"
      @update:model-value="updateVal"
      class="q-mb-lg"
      option-value="id"
      option-label="username"
      :options="users"
      label="User"
      filter="1"
      outlined
    />
    <div class="row">
      <div class="col-12 offset-md-2 col-md-8">
        <q-card class="q-mb-lg">
          <q-card-section class="text-center">
            <div class="text-h4">Consumption stats</div>
          </q-card-section>

          <q-separator inset />

          <div v-if="users">
            <q-card-section class="text-center">
              <div class="text-h6">Today</div>
              <div>Serving size</div>
              <q-badge class="text-h6 q-pa-xs" color="purple">
               {{ servingSizeToday }} ml
              </q-badge>
              <div class="q-mt-md">Caffeine amount</div>
              <q-badge class="text-h6 q-pa-xs" color="teal">
                {{ caffeineAmountToday }} mg
              </q-badge>
            </q-card-section>

            <q-card-section class="text-center">
              <q-banner inline-actions class="text-white bg-primary">
                <div>
                  [5] The U.S. Food and Drug Administration considers 400
                  milligrams (about 4 cups brewed coffee) a safe amount of
                  caffeine for healthy adults to consume daily.
                </div>

                <div class="text-right">
                  <!-- NOTE: What's "_blank"? source https://www.freecodecamp.org/news/how-to-use-html-to-open-link-in-new-tab/ -->
                  <q-btn
                    color="grey-9"
                    target="_blank"
                    href="https://www.hsph.harvard.edu/nutritionsource/caffeine/"
                  >
                    More details
                    <q-icon
                      right
                      size="xs"
                      name="mdi-arrow-top-right-bold-box-outline"
                    />
                  </q-btn>
                </div>
              </q-banner>
            </q-card-section>

            <q-separator inset />

            <q-card-section class="text-center">
              <div class="text-h6">Total</div>
              <div>Serving size</div>
              <q-badge class="text-h6 q-pa-xs" color="purple">
                {{ servingSizeToday }} ml
              </q-badge>
              <div class="q-mt-md">Caffeine amount</div>
              <q-badge class="text-h6 q-pa-xs" color="teal">
                {{ caffeineAmountToday }} mg
              </q-badge>
            </q-card-section>
          </div>

          <q-card-section v-else class="text-center">
            <q-banner inline-actions class="text-white bg-orange">
              <div class="text-h4">Select a user to display his stats</div>
            </q-banner>
          </q-card-section>

          <q-separator inset />
        </q-card>

        <q-table
          :pagination="initialPagination"
          :rows="rows"
          :columns="columns"
          row-key="name"
        >
          <template #body-cell-id="props">
            <q-td key="id" :props="props">
              <q-btn
                @click="remove(props.row.id)"
                class="q-ma-xs"
                color="negative"
                icon="mdi-delete"
                dense
              />
            </q-td>
          </template>
        </q-table>
      </div>
    </div>
  </q-page>
</template>
