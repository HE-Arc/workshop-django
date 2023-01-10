<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const errors = ref({});

const consumedNumber = ref(1);

const users = ref([]);
const user = ref(null);

const caffeineItems = ref([]);
const caffeineItem = ref(null);

const fetchUsers = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/users/");

  users.value = res.data;
};

const fetchCaffeineItems = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/caffeine-items/");

  caffeineItems.value = res.data;
};

const submit = async () => {
  try {
    const res = await axios.post("http://127.0.0.1:8000/api/consumed-items/", {
      user: user.value?.url,
      caffeine_item: caffeineItem.value?.url,
      consumed_number: consumedNumber.value,
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
  <q-page padding>
    <q-form class="q-gutter-md" @submit="submit">
      <div class="row self-center justify-evenly">
        <div class="col-8 col-md-6 q-mt-md">
          <q-card class="q-pa-lg">
            <q-card-section class="">
              <q-btn
                color="primary"
                :to="{
                  name: 'consumedItems',
                }"
              >
                <q-icon left name="mdi-arrow-left-top-bold" />
                <div>Back</div>
              </q-btn>
            </q-card-section>
            <q-card-section class="text-center">
              <div class="text-h5">
                Who, Which and How many caffeinated beverage did you just drank?
              </div>
            </q-card-section>
            <q-card-section>
              <q-select
                v-model="user"
                class="q-mb-lg"
                option-value="id"
                option-label="username"
                :options="users"
                label="User"
                outlined
              />
              <q-select
                v-model="caffeineItem"
                class="q-mb-lg"
                option-value="id"
                option-label="name"
                :options="caffeineItems"
                label="Caffeine item"
                outlined
              />
              <q-input
                v-model.number="consumedNumber"
                type="number"
                label="Quantity"
                outlined
              />
            </q-card-section>
            <q-card-section class="q-gutter-y-sm">
              <div class="text-center">
                <q-btn type="submit" color="primary" label="Submit" />
              </div>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </q-form>
  </q-page>
</template>
