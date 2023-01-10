<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { date } from "quasar";

const rows = ref([]);
const currentRows = ref([]);

const servingSizeTotal = ref(null);
const caffeineAmountTotal = ref(null);

const users = ref([]);
const user = ref(null);

const fetchUsers = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/users/");

  users.value = res.data;
};

const fetchItems = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/consumed-items/");

  res.data.forEach((element) => {
    rows.value.push({
      id: element.id,
      created: element.created,
      user: element.user_obj.username,
      caffeine_item: element.caffeine_item_obj.name,
      serving_size_in_ml: element.caffeine_item_obj.serving_size_in_ml,
      caffeine_amount_in_mg: element.caffeine_item_obj.caffeine_amount_in_mg,
    });
  });
};

const updateVal = () => {
  const res = [];
  servingSizeTotal.value = 0;
  caffeineAmountTotal.value = 0;

  rows.value.forEach((row) => {
    if (row.user == user.value.username) {
      res.push(row);
      servingSizeTotal.value += row.serving_size_in_ml;
      caffeineAmountTotal.value += row.caffeine_amount_in_mg;
    }
  });

  currentRows.value = res;
};

onMounted(() => {
  fetchUsers();
  fetchItems();
});

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
    name: "created",
    label: "Date",
    align: "left",
    field: (row) =>
      date.formatDate(new Date(row.created), "hh:mm:ss DD.MM.YYYY"),
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
    <div class="row q-mb-lg">
      <div class="col-12 text-center">
        <q-btn
          color="primary"
          :to="{
            name: 'consumedItems.create',
          }"
        >
          <q-icon left size="3em" name="mdi-coffee-to-go" />
          <div>I drank a caffeinated beverage</div>
        </q-btn>
      </div>
    </div>

    <div class="row">
      <div class="col-12 offset-md-2 col-md-8">
        <q-card class="q-mb-lg">
          <q-card-section v-if="user" class="text-center">
            <div class="text-h4">Consumption stats</div>

            <div class="text-h6">Today</div>

            <div class="text-h6">Total</div>
            <div>Serving size</div>
            <q-badge class="text-h6 q-pa-xs" color="purple">
              {{ servingSizeTotal }} ml
            </q-badge>
            <div class="q-mt-md">Caffeine amount</div>
            <q-badge class="text-h6 q-pa-xs" color="teal">
              {{ caffeineAmountTotal }} mg
            </q-badge>
          </q-card-section>
          <q-card-section v-else class="text-center">
            <div class="text-h4 text-accent">
              Select a user to display his stats
            </div>
          </q-card-section>
        </q-card>

        <q-table :rows="currentRows" :columns="columns" row-key="name">
          <template #body-cell-id="props">
            <q-td key="id" :props="props">
              <q-btn
                class="q-ma-xs"
                color="primary"
                icon="mdi-arrow-right-bold"
                dense
                :to="{
                  name: 'consumedItems.show',
                  params: { id: props.row.id },
                }"
              />
              <q-btn
                class="q-ma-xs"
                color="primary"
                icon="mdi-pencil"
                dense
                :to="{
                  name: 'consumedItems.edit',
                  params: { id: props.row.id },
                }"
              />
              <q-btn class="q-ma-xs" color="negative" icon="mdi-delete" dense />
            </q-td>
          </template>
        </q-table>
      </div>
    </div>
  </q-page>
</template>
