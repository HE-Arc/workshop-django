<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import ErrorBanner from "../components/ErrorBanner.vue";

const errors = ref(null);

const success = ref(false);

const name = ref("");
const description = ref("");
const servingSize = ref("");
const caffeineAmount = ref("");

const submit = async () => {
  try {
    errors.value = null;
    success.value = false;

    await axios.post("http://localhost:8000/api/caffeine-items/", {
      name: name.value,
      description: description.value,
      serving_size_in_ml: servingSize.value,
      caffeine_amount_in_mg: caffeineAmount.value,
    });

    success.value = true;
  } catch (error) {
    errors.value = error.response.data;
  }
};

onMounted(() => {});
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
                  name: 'beverages',
                }"
              >
                <q-icon left name="mdi-arrow-left-top-bold" />
                <div>Back</div>
              </q-btn>
            </q-card-section>

            <q-card-section class="text-center">
              <div class="text-h5">Create a new beverage</div>
            </q-card-section>

            <q-card-section>
              <div class="text-center q-my-md">
                <!-- NOTE: What's "_blank"? source https://www.freecodecamp.org/news/how-to-use-html-to-open-link-in-new-tab/ -->
                <q-btn
                  color="grey-9"
                  target="_blank"
                  href="https://www.caffeineinformer.com/the-caffeine-database"
                >
                  Help with the values: caffeineinformer.com
                  <q-icon
                    right
                    size="xs"
                    name="mdi-arrow-top-right-bold-box-outline"
                  />
                </q-btn></div
            ></q-card-section>

            <q-card-section>
              <q-input v-model="name" label="*Name" class="q-mb-md" outlined />
              <q-input
                v-model="description"
                label="Description"
                class="q-mb-md"
                outlined
              />
              <q-input
                v-model.number="servingSize"
                type="number"
                label="*Serving size in [ml]"
                class="q-mb-md"
                outlined
              />
              <q-input
                v-model.number="caffeineAmount"
                type="number"
                label="*Caffeine amount in [mg]"
                class="q-mb-md"
                outlined
              />
            </q-card-section>

            <ErrorBanner :errors="errors" />

            <q-banner
              v-if="success"
              inline-actions
              class="q-mb-lg text-white bg-green"
            >
              <div class="text-h6">
                <q-icon left size="md" name="mdi-check-circle-outline" />
                New caffeinated beverage successfully created!
              </div>
            </q-banner>

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
