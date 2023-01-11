<script setup>
// TODO-4-1 Importer axios, ref et onMounted
// TODO-4-2 Récupérer tous les caffeine items de l'API (ref var, async func, axios, onMounted)
// TODO-4-5 Récupérer tous les users de l'API (ref var, async func, axios, onMounted)

// TODO-7-0 Permettre d'enregistrer des consumed items (axios post, form fields, date.now, url vs id)
// TODO-7-2 Créer une variable nommée errors permettant de récupérer les erreurs de l'appel (init à null)

// TODO-9-1 importer le composant ErrorBanner, l'utiliser dans le DOM et tester le résultat
</script>

<template>
  <!-- TODO-4-3 Afficher les caffeine items reçus de l'API -->
  <!-- TODO-4-4 Remplacer les TODOcaffeine par les bons éléments correspondants -->
  <!-- TODO-4-6 Remplacer les TODOuser par les bons éléments correspondants -->

  <!-- TODO-5-0 Remplacer les TODOcreatebeverage par les bons éléments correspondants (beverages.create) -->

  <!-- TODO-7-1 Remplacer les TODOconsumed par les bons éléments correspondants -->
  <!-- TODO-7-3 Afficher le contenu de la var errors ici pour l'instant -->
  <q-page padding>
    <q-select
      v-model="TODOuser"
      option-value="TODOuser"
      option-label="TODOuser"
      :options="TODOuser"
      label="User"
      outlined
    />

    <div class="text-left q-my-md">
      <q-btn color="primary" TODOcreatebeverage>
        <q-icon left size="xl" name="mdi-plus-box" />
        <div>Create a new beverage</div>
      </q-btn>
    </div>

    <div class="row">
      <div
        class="text-center col-12 col-sm-6 col-md-4 col-lg-3 q-pa-sm"
        v-for="(item, index) in TODOcaffeine"
        :key="index"
      >
        <q-card class="my-card">
          <q-card-section>
            <div class="text-h4">TODOcaffeine</div>
            <div class="text-subtitle2">TODOcaffeine</div>
          </q-card-section>

          <q-separator inset />

          <q-card-section>
            <div>Serving size</div>
            <q-badge class="text-h6 q-pa-xs" color="purple">
              TODOcaffeine ml
            </q-badge>
            <div class="q-mt-md">Caffeine amount</div>
            <q-badge class="text-h6 q-pa-xs" color="teal">
              TODOcaffeine mg
            </q-badge>
          </q-card-section>

          <q-separator inset />

          <q-card-actions vertical>
            <q-btn
              push
              @click="TODOconsumed"
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
