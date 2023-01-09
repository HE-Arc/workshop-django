<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { date } from "quasar";

const rows = ref([]);

const fetchItems = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/consumed-items/");

  res.data.forEach((element) => {
    rows.value.push({
      created: element.created,
      user: element.user.username,
      caffeine_item: element.caffeine_item_obj.name,
      consumed_number: element.consumed_number,
    });
  });
};

onMounted(() => {
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
    name: "consumednumber",
    label: "Nnumber",
    align: "left",
    field: (row) => row.consumed_number,
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
];
</script>

<template>
  <q-page padding>
    <q-table :rows="rows" :columns="columns" row-key="name">
      <!-- <template v-slot:body="props">
        <q-tr :props="props">
          <q-td key="name" :props="props">
            {{ props.row.name }}
          </q-td>
          <q-td key="calories" :props="props">
            <q-badge color="green">
              {{ props.row.calories }}
            </q-badge>
          </q-td>
          <q-td key="fat" :props="props">
            <q-badge color="purple">
              {{ props.row.fat }}
            </q-badge>
          </q-td>
          <q-td key="carbs" :props="props">
            <q-badge color="orange">
              {{ props.row.carbs }}
            </q-badge>
          </q-td>
          <q-td key="protein" :props="props">
            <q-badge color="primary">
              {{ props.row.protein }}
            </q-badge>
          </q-td>
          <q-td key="sodium" :props="props">
            <q-badge color="teal">
              {{ props.row.sodium }}
            </q-badge>
          </q-td>
          <q-td key="calcium" :props="props">
            <q-badge color="accent">
              {{ props.row.calcium }}
            </q-badge>
          </q-td>
          <q-td key="iron" :props="props">
            <q-badge color="amber">
              {{ props.row.iron }}
            </q-badge>
          </q-td>
        </q-tr>
      </template> -->
    </q-table>
  </q-page>
</template>
