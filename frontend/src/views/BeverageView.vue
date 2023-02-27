<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import ErrorBanner from "../components/ErrorBanner.vue";

const errors = ref(null);

const caffeineItems = ref([]);

const users = ref([]);
const user = ref(null);

const fetchUsers = async () => {
  const res = await axios.get(`${import.meta.env.VITE_HOST}/api/users/`);

  users.value = res.data;
};

const fetchCaffeineItems = async () => {
  const res = await axios.get(
    `${import.meta.env.VITE_HOST}/api/caffeine-items/`
  );

  caffeineItems.value = res.data;
};

const readCookie = (name) => {
  const nameEQ = name.concat("=");
  const ca = document.cookie.split(";");
  for (let i = 0; i < ca.length; i += 1) {
    let c = ca[i];
    while (c.charAt(0) === " ") c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
};
const submit = async (caffeine_item) => {
  try {
    errors.value = null;

    const res = await axios.post(
      `${import.meta.env.VITE_HOST}/api/consumed-items/`,
      {
        user: user.value?.url,
        caffeine_item: caffeine_item.url,
        consumed_number: 1,
        consumption_date: new Date(),
      },
      {
        headers: {
          "x-csrftoken": readCookie("csrftoken"),
        },
        withCredentials: true,
      }
    );

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
  <q-page padding>
    <ErrorBanner :errors="errors" />

    <q-select
      v-model="user"
      option-value="id"
      option-label="username"
      :options="users"
      label="User"
      outlined
    />

    <div class="text-left q-my-md">
      <q-btn
        color="primary"
        :to="{
          name: 'beverages.create',
        }"
      >
        <q-icon left size="3em" name="mdi-plus-box" />
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
