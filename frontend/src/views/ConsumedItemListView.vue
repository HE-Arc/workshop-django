<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const users = ref([]);

const fetchUsers = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/users/");

  users.value = res;
};

onMounted(() => {
  fetchUsers();
});
</script>

<template>
  <q-page padding>{{ users }} </q-page>
</template>
