<script setup>
// TODO-5-1 Importer axios, ref
import axios from "axios";
import { ref } from "vue";
// TODO-5-2 Créer des variables string pour chaque tous les éléments de coffeine item :
//name, description, servingSize et caffeineAmount (ref var)

const name = ref("");
const description = ref("");
const servingSize = ref("");
const caffeineAmount = ref("");
const errors = ref(null);

// TODO-5-3 Créer une fonction nommée submit permettant d'envoyer les données du form à l'API

const submit = async () => {
  try {
    errors.value = null;
    success.value = false;

    await axios.post("http://127.0.0.1:8000/api/caffeine-items/", {
      name: name.value,
      description: description.value,
      serving_size_in_ml: servingSize.value,
      caffeine_amount_in_mg: caffeineAmount.value,
    });
    success.value = true;
  } catch (error) {
    console.log(error.response.data);
    errors.value = error.response.data;
  }
};

// TODO-5-4 Créer une variable bool nommée success permettant d'afficher un message de succès (utile plus tard)

const success = ref(false);

// TODO-5-5 Créer une variable nommée errors permettant de récupérer les erreurs de l'appel (init à null)


// TODO-9-1 importer le composant ErrorBanner, l'utiliser dans le DOM et tester le résultat
import ErrorBanner from "../components/ErrorBanner.vue";
</script>

<template>
  <ErrorBanner :errors="errors" />
  <!-- TODO-5-6 Afficher le contenu de la var errors ici pour l'instant -->
  {{ errors }}
  <!-- TODO-5-7 Remplacer les TODOform par les bons éléments correspondants -->

  <!-- TODO-5-8 Essayer d'enregistrer des éléments sur le site et voir si ces éléments sont correctement
  ajoutés à la BDD et affichés sur la page /beverages -->
  <q-page padding>
    <q-form class="q-gutter-md" @submit="submit">
      <div class="row self-center justify-evenly">
        <div class="col-8 col-md-6 q-mt-md">
          <q-card class="q-pa-lg">
            <q-card-section class="">
              <q-btn color="primary" :to="{ name: 'beverages' }">
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
