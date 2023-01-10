<script setup>
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
  <q-page padding>
    <p>
      If your user is displayed in the array bellow, you're ready for the
      Workshop! :)
    </p>

    <div class="q-mb-md">{{ users }}</div>

    <div>
      <img src="@/assets/images/coffee_dev_meme_bruce_almighty.gif" />
    </div>
  </q-page>
</template>
