# Configuration du workshop

La documentation de configuration du workshop se trouve dans le README sur la branche `main`.

Ce README sera utile durant la réalisation du workshop.

# Réponses

**ATTENTION**  
Ce README a été conçu pour être visualisé en mode "preview", depuis GitHub ou depuis n'importe quel autre interpréteur MarkDown.  
Si vous ouvrez et suivez les instructions de ce fichier dans votre IDE, vous pourriez avoir quelques soucis avec le copier-coller, etc.

**AVERTISSEMENT**  
Lire les réponses uniquement en cas de besoins, essayez d'abord par vous-même, vous apprendrez mieux ;)

TODO-0-0

```
cd api

source path_to_venv/Scripts/activate
# Or
. path_to_venv/Scripts/activate

python manage.py runserver
```

TODO-0-1

```
python manage.py migrate

python manage.py createsuperuser --email admin@example.com --username admin
```

TODO-0-2

```
INSTALLED_APPS = [
    ...
    "caffeinecalculatorapp",
    ...
]
```

TODO-0-3

Lire les parties dédiées aux extensions et aux formatters dans le README sur la branche `main`

TODO-0-4

```
pipenv install --dev

pip freeze
```

TODO-1-0

```
class CaffeineItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, blank=True)
    serving_size_in_ml = models.FloatField()
    caffeine_amount_in_mg = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
```

TODO-1-1

```
python manage.py makemigrations caffeinecalculatorapp

python manage.py migrate
```

TODO-1-2

```
from caffeinecalculatorapp.models import CaffeineItem

admin.site.register(CaffeineItem)
```

TODO-1-3

Actions à réaliser dans l'interface admin de Django

TODO-1-4

Actions à réaliser dans l'interface admin de Django

TODO-1-5

```
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "url",
            "id",
            "username",
        ]
```

TODO-1-6

```
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
```

TODO-1-7

```
from . import views

urlpatterns = [
    ...
    path("users/", views.UserList.as_view(), name="user-list"),
    path(
        "users/<int:pk>/",
        views.UserDetail.as_view(),
        name="user-detail",
    ),
    ...
]
```

TODO-1-8

```
from django.urls import include

urlpatterns = [
    ...
    path("api/", include("caffeinecalculatorapp.urls")),
    ...
]
```

TODO-1-9

```
INSTALLED_APPS = [
    ...
    "rest_framework",
    ...
]
```

TODO-1-10

Accéder à /api/users/

TODO-2-0

```
cd frontend

npm install

npm run dev
```

TODO-2-1

```
<script setup></script>
```

TODO-2-2

```
import axios from "axios";
```

TODO-2-3

```
import { ref, onMounted } from "vue";

const users = ref([]);

const fetchUsers = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/users/");

  users.value = res.data;
};
```

TODO-2-4

```
<template>
    {{ users }}
    ...
</template>
```

Tester l'application en accédant à la page d'accueil

TODO-2-5

```
INSTALLED_APPS = [
    ...
    "corsheaders",
    ...
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    ...
]

# Replace URLs by yours
CORS_ALLOWED_ORIGINS = ["http://localhost:5173", "http://127.0.0.1:5173"]
```

TODO-2-6

Tester l'application en accédant à la page d'accueil

TODO-2-7

```
import NavBar from "./components/NavBar.vue";

...

<NavBar></NavBar>
```

TODO-3-0

```
from .models import CaffeineItem


class CaffeineItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(required=False, max_length=2000)
    serving_size_in_ml = serializers.FloatField()
    caffeine_amount_in_mg = serializers.FloatField()

    def create(self, validated_data):
        return CaffeineItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.serving_size_in_ml = validated_data.get(
            "serving_size_in_ml", instance.serving_size_in_ml
        )
        instance.caffeine_amount_in_mg = validated_data.get(
            "caffeine_amount_in_mg", instance.caffeine_amount_in_mg
        )
        instance.save()
        return instance
```

TODO-3-1

```
class CaffeineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaffeineItem
        fields = [
            "url",
            "id",
            "name",
            "description",
            "serving_size_in_ml",
            "caffeine_amount_in_mg",
        ]
```

TODO-3-2

```
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import CaffeineItem
from .serializers import UserSerializer


@api_view(["GET", "POST"])
def caffeine_item_list(request):
    if request.method == "GET":
        caffeine_items = CaffeineItem.objects.all()
        serializer = CaffeineItemSerializer(caffeine_items, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = CaffeineItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

TODO-3-3

```
from rest_framework.views import APIView


class CaffeineItemList(APIView):
    def get(self, request, format=None):
        caffeine_items = CaffeineItem.objects.all()
        serializer = CaffeineItemSerializer(caffeine_items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CaffeineItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

TODO-3-4

```
from rest_framework import mixins


class CaffeineItemList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = CaffeineItem.objects.all()
    serializer_class = CaffeineItemSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

TODO-3-5

```
from rest_framework import generics


class CaffeineItemList(generics.ListCreateAPIView):
    queryset = CaffeineItem.objects.all()
    serializer_class = CaffeineItemSerializer
```

TODO-3-6

```
from rest_framework import viewsets


class CaffeineItemViewSet(viewsets.ModelViewSet):
    queryset = CaffeineItem.objects.all()
    serializer_class = CaffeineItemSerializer
```

TODO-3-7

```
from rest_framework.routers import DefaultRouter
from django.urls import include


router = DefaultRouter()
router.register(r"caffeine-items", views.CaffeineItemViewSet, basename="caffeineitem")

urlpatterns = [
    ...
    path("", include(router.urls)),
]
```

TODO-4-0

```
{
  path: "/beverages",
  name: "beverages",
  component: () => import("../views/BeverageView.vue"),
},
```

```
<q-route-tab :to="{ name: 'beverages' }" label="Add beverage" />
```

TODO-4-1

```
import axios from "axios";
import { ref, onMounted } from "vue";
```

TODO-4-2

```
const caffeineItems = ref([]);

const fetchCaffeineItems = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/caffeine-items/");

  caffeineItems.value = res.data;
};

onMounted(() => {
  fetchCaffeineItems();
});
```

TODO-4-3

```
{{ caffeineItems }}
```

TODO-4-4

```
v-for="(item, index) in caffeineItems"

<div class="text-h4">{{ item.name }}</div>
<div class="text-subtitle2">{{ item.description }}</div>

<q-badge class="text-h6 q-pa-xs" color="purple">
  {{ item.serving_size_in_ml }} ml
</q-badge>
<q-badge class="text-h6 q-pa-xs" color="teal">
  {{ item.caffeine_amount_in_mg }} mg
</q-badge>
```

TODO-4-5

```
const users = ref([]);
const user = ref(null);

const fetchUsers = async () => {
  const res = await axios.get("http://127.0.0.1:8000/api/users/");

  users.value = res.data;
};

onMounted(() => {
  fetchUsers();
});
```

TODO-4-6

```
<q-select
  v-model="user"
  option-value="id"
  option-label="username"
  :options="users"
  label="User"
  outlined
/>
```

TODO-5-0

```
{
  path: "/TODOcreatebeverage",
  name: "TODOcreatebeverage",
  component: () => import("../views/CreateBeverageView.vue"),
},
```

```
<q-btn
  color="primary"
  :to="{
    name: 'beverages.create',
  }"
>
```

TODO-5-1

```
import axios from "axios";
import { ref } from "vue";
```

TODO-5-2

```
const name = ref("");
const description = ref("");
const servingSize = ref("");
const caffeineAmount = ref("");
```

TODO-5-3

```
const submit = async () => {
  try {
    await axios.post("http://127.0.0.1:8000/api/caffeine-items/", {
      name: name.value,
      description: description.value,
      serving_size_in_ml: servingSize.value,
      caffeine_amount_in_mg: caffeineAmount.value,
    });
  } catch (error) {
    console.log(error.response.data);
  }
};
```

TODO-5-4

```
const success = ref(false);
```

TODO-5-5

```
const errors = ref(null);

const submit = async () => {
  try {
    errors.value = null;
    success.value = false;
    ...
    (await axios here)
    ...
    success.value = true;
  } catch (error) {
    ...
    errors.value = error.response.data;
  }
};
```

TODO-5-6

```
{{ errors }}
```

TODO-5-7

```
<q-form class="q-gutter-md" @submit="submit">

<q-btn
  color="primary"
  :to="{
    name: 'beverages',
  }"
>

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

<q-banner
  v-if="success"
  inline-actions
  class="q-mb-lg text-white bg-green"
>

<q-btn type="submit" color="primary" label="Submit" />
```

TODO-6-0

```
class ConsumedItem(models.Model):
    user = models.ForeignKey(
        User, related_name="consumed_items", on_delete=models.CASCADE
    )
    caffeine_item = models.ForeignKey(
        CaffeineItem,
        related_name="consumed_items",
        on_delete=models.SET_NULL,
        null=True,
    )
    consumed_number = models.PositiveIntegerField()
    consumption_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
```

TODO-6-1

``
python manage.py makemigrations caffeinecalculatorapp

python manage.py migrate

```

TODO-6-2

```

from .models import ConsumedItem

class ConsumedItemSerializer(serializers.HyperlinkedModelSerializer):
class Meta:
model = ConsumedItem
fields = [
"url",
"id",
"user",
"caffeine_item",
"consumed_number",
"consumption_date",
]

```

TODO-6-3

```

from .models import ConsumedItem
from .serializers import ConsumedItemSerializer
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404

class ConsumedItemViewSet(viewsets.ModelViewSet):
queryset = ConsumedItem.objects.all()
serializer_class = ConsumedItemSerializer

    @action(detail=True, methods=["POST"], url_path="increase-by-one")
    def increase_by_one(self, request, pk):
        consumed_item = get_object_or_404(ConsumedItem, pk=pk)

        data = {"consumed_number": consumed_item.consumed_number + 1}
        serializer = self.get_serializer(
            consumed_item,
            data=data,
            partial=True,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

```

TODO-6-4

```

router.register(r"consumed-items", views.ConsumedItemViewSet, basename="consumeditem")

```

TODO-6-5

Actions à réaliser sur la browsable API de DRF directement, en utilisant le POST form /api/consumed-items/

TODO-6-6

```

class UserViewSet(viewsets.ReadOnlyModelViewSet):
queryset = User.objects.all()
serializer_class = UserSerializer

```

TODO-6-7

```

router.register(r"users", views.UserViewSet, basename="user")

```

TODO-6-8

Accéder aux 3 ressources via la browsable API de DRF directement et vérifier que toutes les routes fonctionnent toujours

TODO-6-9

```

class ComplexeUserSerializer(UserSerializer):
consumed_items = serializers.HyperlinkedRelatedField(
many=True, view_name="consumeditem-detail", read_only=True
)

    class Meta:
        model = User
        fields = UserSerializer.Meta.fields + [
            "consumed_items",
        ]

```

> NOTE: More complexe serializer for users including additionnal fields
> Keeping a "default" serializer with the default fields representation
> also avoids circular calls
> e.g.: UserSerializer fetches the consumed_items using the ConsumedItemSerializer
> which fetches the user using the UserSerializer, etc. (it never ends until it crashes)


TODO-6-10

```

from .serializers import ComplexeUserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
queryset = User.objects.all()
serializer_class = ComplexeUserSerializer

```

TODO-6-11

```

class ComplexeConsumedItemSerializer(ConsumedItemSerializer):
user_obj = UserSerializer(source="user", read_only=True)
caffeine_item_obj = CaffeineItemSerializer(source="caffeine_item", read_only=True)

    class Meta:
        model = ConsumedItem
        fields = ConsumedItemSerializer.Meta.fields + [
            "user_obj",
            "caffeine_item_obj",
        ]

```

TODO-6-12

```

from .serializers import ComplexeConsumedItemSerializer

class ConsumedItemViewSet(viewsets.ModelViewSet):
queryset = ConsumedItem.objects.all()
serializer_class = ComplexeConsumedItemSerializer

```

Et actions à réaliser sur la browsable API de DRF directement, en accédant à /api/consumed-items/

TODO-7-0

```

const submit = async (caffeine_item) => {
try {
const res = await axios.post("http://127.0.0.1:8000/api/consumed-items/", {
user: user.value?.url,
caffeine_item: caffeine_item.url,
consumed_number: 1,
consumption_date: new Date(),
});

    console.log(res);

} catch (error) {
console.log(error.response.data);
}
};

```

TODO-7-1

```

<q-btn
push
@click="submit(item)"
class="q-ma-xs"
color="primary"
dense

>

```


TODO-7-2

```

const errors = ref(null);

const submit = async () => {
try {
errors.value = null;
...
(await axios here)
...
} catch (error) {
...
errors.value = error.response.data;
}
};

```

TODO-7-3

```

{{ errors }}

```

TODO-8-0

```

<q-route-tab
  :to="{ name: 'detailsAndStats' }"
  label="Details and stats"
/>

```

```

{
path: "/details-and-stats",
name: "detailsAndStats",
component: () => import("../views/DetailsAndStatsView.vue"),
},

```

TODO-8-1

```

import axios from "axios";
import { ref, onMounted } from "vue";
import { date } from "quasar";

```

TODO-8-2

```

const users = ref([]);

const fetchUsers = async () => {
const res = await axios.get("http://127.0.0.1:8000/api/users/");

users.value = res.data;
};

const rows = ref([]);

const fetchItems = async () => {
const res = await axios.get("http://127.0.0.1:8000/api/consumed-items/");

rows.value = [];

res.data.forEach((element) => {
rows.value.push({
id: element.id,
consumption_date: element.consumption_date,
user: element.user_obj.username,
caffeine_item: element.caffeine_item_obj.name,
serving_size_in_ml: element.caffeine_item_obj.serving_size_in_ml,
caffeine_amount_in_mg: element.caffeine_item_obj.caffeine_amount_in_mg,
});
});
};

onMounted(() => {
fetchUsers();
fetchItems();
});

```

TODO-8-3

```

{{ rows }}

```

TODO-8-4

```

<q-table
:pagination="initialPagination"
:rows="rows"
:columns="columns"
row-key="name"

>

```

TODO-8-5

```

const user = ref(null);

const currentRows = ref([]);

```

TODO-8-6

```

const updateVal = () => {
const res = [];

rows.value.forEach((row) => {
if (row.user == user.value.username) {
res.push(row);
}
});

currentRows.value = res;
};

```

TODO-8-7

```

q-select
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

...

<q-table
:pagination="initialPagination"
:rows="currentRows"
:columns="columns"
row-key="name"

>

```

TODO-8-8

```

const servingSizeTotal = ref(null);
const caffeineAmountTotal = ref(null);
const servingSizeToday = ref(null);
const caffeineAmountToday = ref(null);

```

TODO-8-9

```

const updateVal = () => {
...
servingSizeTotal.value = 0;
caffeineAmountTotal.value = 0;
servingSizeToday.value = 0;
caffeineAmountToday.value = 0;

rows.value.forEach((row) => {
if (row.user == user.value.username) {
...

      servingSizeTotal.value += row.serving_size_in_ml;
      caffeineAmountTotal.value += row.caffeine_amount_in_mg;

      const rowDate = new Date(row.consumption_date);
      const currentDate = new Date();
      if (
        rowDate.getFullYear() === currentDate.getFullYear() &&
        rowDate.getMonth() === currentDate.getMonth() &&
        rowDate.getDate() === currentDate.getDate()
      ) {
        servingSizeToday.value += row.serving_size_in_ml;
        caffeineAmountToday.value += row.caffeine_amount_in_mg;
      }
    }

});

...
};

```

TODO-8-10

```

<div class="text-h6">Today</div>
<div>Serving size</div>
<q-badge class="text-h6 q-pa-xs" color="purple">
  {{ servingSizeToday }} ml
</q-badge>
<div class="q-mt-md">Caffeine amount</div>
<q-badge class="text-h6 q-pa-xs" color="teal">
  {{ caffeineAmountToday }} mg
</q-badge>
```

TODO-8-11

```
const remove = async (id) => {
  await axios.delete(`http://127.0.0.1:8000/api/consumed-items/${id}/`);

  await fetchItems();

  updateVal();
};
```

TODO-8-12

```
<q-btn
  @click="remove(props.row.id)"
  class="q-ma-xs"
  color="negative"
  icon="mdi-delete"
  dense
/>
```

TODO-9-0

```
const props = defineProps({
  errors: Array,
});

...

<q-banner
  v-if="props.errors"
  inline-actions
  class="q-mb-lg text-white bg-red"
>

...

<div class="self-center" v-for="(item, key) in props.errors" :key="key">
  {{ key }}
  <ul>
    <li v-for="(err, index) in item" :key="index">{{ err }}</li>
  </ul>
</div>
```

TODO-9-1

```
import ErrorBanner from "../components/ErrorBanner.vue";

...

<ErrorBanner :errors="errors" />
```
