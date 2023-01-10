<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const errors = ref({});

const caffeineItems = ref([]);

const users = ref([]);
const user = ref(null);

const fetchUsers = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/users/");

  users.value = res.data;
};

const fetchCaffeineItems = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/caffeine-items/");

  caffeineItems.value = res.data;
};

const submit = async (caffeine_item) => {
  try {
    const res = await axios.post("http://127.0.0.1:8000/api/consumed-items/", {
      user: user.value?.url,
      caffeine_item: caffeine_item.url,
      consumed_number: 1,
    });

    console.log(res);
  } catch (error) {
    console.log(error.response.data);
    errors.value = error.response.data;
  }
};

onMounted(() => {
  fetchUsers();
  fetchCaffeineItems();
});
</script>

<template>
  {{ errors }}
  <q-page padding>
    <q-select
      v-model="user"
      class="q-mb-lg"
      option-value="id"
      option-label="username"
      :options="users"
      label="User"
      outlined
    />

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
              <q-icon left size="3em" name="mdi-numeric-positive-1" />
              <div>I drank this one today</div>
            </q-btn>
          </q-card-actions>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<style scoped></style>
