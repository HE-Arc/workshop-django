# Introduction

Ce Workshop Django est donné aux étudiants de 3ème année à la HE-Arc dans le cadre du cours de développement web.

L'objectif de ce workshop est de transmettre aux étudiants les bases et les bonnes pratiques de la création d'un projet web avec le Framework Django et Vuejs. Ce workshop a également pour but de fournir un point de départ aux étudiants afin de leur permettre de créer leur projet de semestre.

Les prochaines étapes permettent de mettre en place l'environnement de développement et de suivre le workshop dans son intégralité.

# Explication des branches

Branches générales

- main : la branche contenant la version du README le plus à jour
- start : la branche contenant le code de départ du workshop Django
- end : la branche contenant le code solution du workshop Django

Branches par année

- xxxx-start : la branche contenant le code de départ du workshop Django, réalisé avec les étudiants de l'année xxxx
- xxxx-end : la branche contenant le code solution du workshop Django, réalisé avec les étudiants de l'année xxxx

# Prérequis

Dans ce workshop nous utiliserons la version 5.0 de Django et la version 3.3.4 de Vue.js.

La première étape est d'installer les différents prérequis listés ci-dessous.

## IMPORTANT si vous travaillez sur linux

Vous concerne si vous utilisez Linux :

Sur Linux toutes les commandes python doivent commencer par `python3`, donc `python --version` sur Windows, devra s'écrire `python3 --version` sur Linux.

Les commande pip doivent également commencée par `pip3`, donc `pip --version` sur Windows, devra s'écrire `pip3 --version` sur Linux.

C'est une source d'erreur très fréquente, il faut s'y faire au début, cela devient un automatisme par la suite...

## Python

Pour le workshop vous aurez besoin de la version de Python >= 3.10.

https://www.python.org/downloads/

> Le workshop a été testé avec la version 3.12.1 de Python

> Dépendance provenant du site officiel de Django pour la version utilisée dans ce workshop https://docs.djangoproject.com/en/5.0/faq/install/#what-python-version-can-i-use-with-django  
> Documentation Django officielle pour la version utilisée de Django https://docs.djangoproject.com/en/5.0/

```
python --version
```

## pip

pip est le "package manager" qui vient par défaut avec Python, assurez-vous simplement d'avoir une version compatible.

> Le workshop a été testé avec la version 23.3.2 de pip

```
pip --version
```

Si nécessaire, pip peut être mis à niveau avec la commande suivante.

```
python -m pip install --upgrade pip
```

## Nodejs

Pour le workshop vous aurez besoin de la version de Node.js >= 18.0

https://nodejs.org/en/

> Le workshop a été testé avec la version 20.10.0 de Node.js

> Dépendance provenant du site officiel de Vue.js https://vuejs.org/guide/quick-start.html

```
node --version
```

## npm

npm est le "package manager" qui vient par défaut avec Node.js, assurez-vous simplement d'avoir une version compatible.

> Le workshop a été testé avec la version 10.2.3 de npm

```
npm --version
```

# Installation et configuration

Vous trouverez ci-dessous les quelques commandes qui vous permettront de commencer à travailler sur le workshop.

## 1. Cloner le répo Github du workshop, vous connaissez c'est easy ;)

**Commandes**

> SSH recommandé

```
git clone git@github.com:HE-Arc/workshop-django.git
cd workshop-django
git checkout check
```

## 2. Installer les dépendances de l'app Django dans un venv, c'est très important... vraiment !

**Commandes**

Installer `pipenv` qui s'occupera de gérer nos bibliothèques Python via pip.

> Testé avec la version `pipenv==2023.11.15`

```
pip install pipenv
```

Installer les bibliothèques du projet.

```
cd api
pipenv install
```

> Cette commande crée un environnement virtuel et y installe toutes les bibliothèques nécessaires.

> **ATTENTION** ! Pour installer une bibliothèque dans notre projet il faudra utiliser pipenv directement et non plus pip.  
> ```
> pipenv install package==x.y.z
> ```

Lancer des commandes depuis l'environnement virtuel

```
pipenv run python ...
```

Ou activer l'env virtuel

> REMARQUE : Il se peut que sur Windows, l'environnement virtuel est créé dans le dossier personnel de l'utilisateurs. Afin de savoir son emplacement à tout moment, vous pouvez utiliser la commande `pipenv --venv` dans le dossier contenant les dépendances installés.

```
source path_to_venv/Scripts/activate
# Or
. path_to_venv/Scripts/activate
```

> Si la commande ne fonctionne pas, c'est peut être un problème de permission, essayez d'exécuter en mode admin.

**Détails et explications**

> Virtual environment en anglais, souvent abrégé venv

Le gestionnaire de paquet en Python s'appelle pip. La technique de base consiste à créer un fichier nommé requirement.txt dans lequel nous allons pouvoir lister toutes les bibliothèques (dépendances) dont notre projet a besoin pour fonctionner correctement. Dans ce workshop nous utilisons une technique un peu plus avancée en utilisant pipenv qui permet d'organiser un peu mieux nos bibliothèques (un peu à l'image de composer ou de npm).

Par défaut pip installe toutes les bibliothèques globalement sur l'ordinateur, ce qui pourrait paraître comme une bonne idée à la base, car si nous avons un autre projet qui nécessite toutes ou certaines mêmes bibliothèques, les bibliothèques en question seront déjà installées... MAIS...

Mais en réfléchissant un peu on s'aperçoit très vite que c'est une très mauvaise idée. Certaines bibliothèques pourraient ne pas être compatibles ce qui pourrait rapidement devenir difficile à gérer.

Le mieux est donc de séparer toutes les bibliothèques de tous les projets quitte à devoir réinstaller dans certains cas la même version de certaines d'entre elles.

Pour ce faire nous allons utiliser les environnements virtuels qui nous permettent d'isoler un environnement afin de le séparer de celui de base et des autres que nous allons créer pour d'autres projets.

Il existe plusieurs bibliothèques qui permettent toutes de créer des environnements virtuels. Dans notre cas et comme nous utilisons pipenv, nous utiliserons celle proposée par défaut par pipenv.

Vous devez le créer une fois au début et/ou à chaque fois que vous clonez le projet. Ensuite une fois qu'il est créé pour la première fois vous n'aurez plus qu'à l'activer. Attention il ne faut pas oublier de le réactiver.

**IMPORTANT** : les dossiers et fichiers de l'environnement virtuel ne doivent JAMAIS être push (en utilisant pipenv, c'est le comportement par défaut, car les env virtuels ne sont pas créés dans le dossier du projet. En principe vous n'avez donc rien à faire) !  

## 3. Migrer et créer un utilisateur admin

**Commandes**

Migrez

```
pipenv run python manage.py migrate
```

Créez un nouvel utilisateur admin et donnez-lui un mot de passe dont vous pourrez vous rappeler.

```
pipenv run python manage.py createsuperuser --email admin@example.com --username admin
```

> Si vous êtes sur Windows et que vous avez des erreurs avec ces commandes, vous pouvez essayer de préfixé les commandes python par `winpty`
> Exemple : `winpty python manage.py migrate`
> https://stackoverflow.com/questions/32532900/not-able-to-create-super-user-with-django-manage-py

## 4. Démarrer le serveur de dev

**Commandes**

```
pipenv run python manage.py runserver
```

## 5. Tester l'app Django

En allant à l'URL proposée dans la console, après avoir démarré le serveur de dev, aller sur `/admin` et tenter de vous connecter avec l'utilisateur créé précédemment.

S’il n'y a pas d'erreur et que vous arrivez sur une interface sur laquelle il est écrit "Django Administration", c'est tout bon et vous pouvez passer à la suite.

## 6. Installer les dépendances de l'app Vue.js

**Commandes**

Dans un nouveau bash, se rendre dans le dossier `frontend` et exécutez

```
npm install
```

## 7. Démarrer le serveur de dev de l'app Vue.js

**Commandes**

```
npm run dev
```


## 8. Tester l'app Vue.js

**Prérequis**

Vous devriez maintenant avoir 2 bash ouvert, le premier bash avec le serveur Django et l'autre bash avec le serveur Vue.js.  
Si ce n'est pas le cas, assurez-vous d'avoir les 2 serveurs allumés avant de continuer.

Une fois les 2 serveurs allumés...

**Test**

En allant à l'URL proposée dans la console, après avoir démarré le serveur de dev, vous devriez voir une application avec du texte et un GIF.

Lisez le texte et vérifiez que ce qui est indiqué fonctionne correctement pour vous, si c'est le cas... C'est que vous êtes prêt pour le workshop !

---

**Prêt pour le workshop !**

Si vous êtes arrivés jusqu'ici sans problème, vous êtes prêt pour le workshop.  
La suite vous sera utile lorsque vous devrez créer votre propre projet pour le semestre.

---

# Méthodologie - Comment va se dérouler le workshop ?

L'app est préexistante. Il faudra remplir les trous (TODOs) pour la rendre fonctionnelle (eeeasy!).

On part de TODO-0-0 jusqu'à TODO-X-Y, avec à chaque étape quelques lignes à taper.

On fait une recherche dans l'arborescence (Ctrl+Shift+F avec VSCode p.ex) et on recherche les TODOs un à un.

Les réponses se trouvent dans le README sur la branche `start` mais **c'est de la triche de regarder**. C'est seulement en cas d'urgence (je vous vois).

# Initialiser un nouveau projet de zéro

Durant le workshop nous avons démarré d'un projet existant, en réalité c'est juste pour nous faire gagner du temps, mais c'est simple à reproduire.

Voici quelques explications vous permettant de créer un projet Django et Vue.js comme dans le workshop. Le résultat se rapproche de celui du workshop, mais il faudra le compléter avec ce qui a été vu durant le workshop.

## Prérequis

Avant de réaliser les étapes suivantes, assurez-vous d'avoir correctement installé Python et Node.js comme demandé pour le workshop.

## Django

Installez pipenv si ce n'est pas déjà fait.

Vous trouverez des explications sur les commandes principales à connaitre afin d'utiliser pipenv correctement : https://pipenv.pypa.io/en/latest/

A la racine de votre projet, créez un dossier pour le backend (p.ex. api).

Ouvrez un bash/terminal/autre dans ce dossier que vous venez de créer et exécutez-y la commande suivante afin de créer un venv.

```sh
pipenv install
```

Installez la dernière version de Django et de Django REST Framework. Vous pouvez trouver les versions des package à l'aide de `pip index versions package_name`.

```sh
pipenv install django==version_number
pipenv install djangorestframework==version_number

django-admin startproject tutorial . # ATTENTION le "." en fin de commande est important ici
django-admin startapp tutorialapp

pipenv run python manage.py migrate

pipenv run python manage.py createsuperuser --email admin@example.com --username admin
```

Ajoutez 'rest_framework' aux INSTALLED_APPS se trouvant dans le fichier `tutorial/settings.py`.

```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

Le projet backend devrait déjà pouvoir fonctionner.

```
pipenv run python manage.py runserver
```

Vous devriez voir une page Django à l'URL : http://127.0.0.1:8000/

Maintenant, il faut créer un model, un serializer, une view et des urls pour pouvoir commencer à afficher des données provenant de la base de données.

Une fois fait et si tout a bien été configuré, vous devriez pouvoir avoir accès à la "browsable API" de Django REST Framework.

## Vue.js

A la racine de votre projet, créez un dossier pour le frontend (p.ex. frontend).

Ouvrez un bash/terminal/autre dans ce dossier que vous venez de créer et exécutez-y la commande suivante afin de créer un projet vue.js.

```sh
npm init vue@latest . # ATTENTION le "." en fin de commande est important ici
``` 

Vous devrez répondre à une série de questions, voici ce que je vous recommande de sélectionner :

![image](https://user-images.githubusercontent.com/39899628/213749904-d7598ea1-f13d-4b2e-8545-68c18f9c4892.png)

Vous pouvez ensuite installer les dépendances et `axios` pour vous permettre de réaliser des requêtes asynchrones.

```sh
npm install

npm install axios
```

Démarrez le serveur de développement.

```sh
npm run dev
```

Vous devriez voir une page Vue.js à l'URL : http://localhost:5173/

Maintenant, il faut créer une nouvelle view et afficher des données provenant de votre API à l'aide d'appels asynchrones en utilisant axios.

Durant le workshop nous avons utilisé un framework de styles et composants pour Vue 3 qui se nomme Quasar, vous êtes libre d'utiliser le même (je vous le recommande) ou d'en utiliser un autre.  
Si vous partez sur Quasar, vous pouvez l'installer et le configurer en suivant ce lien (vous pouvez sauter la section "Creating a Vite project", c'est déjà fait dans notre cas) : https://quasar.dev/start/vite-plugin

> NOTE : Attention, si vous choisissez d'utiliser Vuetify (qui est normalement l'option par défaut), soyez au courant que la version actuellement compatible avec Vue 3 est incomplète. Renseignez-vous un peu avant de choisir entre Vuetify/Quasar/autre.

---

# Tips

## Installer des extensions VSCode pour aider au développement

Si vous utilisez Visual Studio Code, je vous recommande fortement d'installer et d'utiliser les packs d'extensions suivants.

- `Python Extension Pack` : Django
- `Vue Volar extension Pack` : Vue.js

Ces extensions VSCode facilitent grandement le développement ! Je ne peux que vous recommander très très fortement de les installer et de les utiliser. Certaines sont plus utiles que d'autres.  
Même si cela est recommandé, il n'est pas obligatoire de les installer, vous êtes également libre de sélectionner dans ces packs, les extensions que vous souhaitez utiliser.

Ces extensions sont pour la plupart configurables, voici quelques configurations que je vous recommande d'ajouter.

Pour Django, il est également possible d'activer l'importation automatique dans les paramètres de Pylance https://code.visualstudio.com/docs/python/editing#_enable-auto-imports

## Installer un formatter pour Python

Il en existe plusieurs, voici celui que j'utilise :

https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0

## Supprimer toutes les bibliothèques d'un environnement

```
pip freeze | xargs pip uninstall -y
```

https://stackoverflow.com/questions/11248073/what-is-the-easiest-way-to-remove-all-packages-installed-by-pip

## Supprimer une bibliothèque et toutes ces dépendances en utilisant pipenv

```
pipenv uninstall package && pipenv clean
```

> Replace "package" by the name of the package you're interested in

https://stackoverflow.com/questions/62632664/how-to-autoremove-dependent-python-packages-within-a-pipenv-when-uninstalling-a

## Lister toutes les versions d'une bibliothèque Python disponible avec pip

```
pip index versions package
```

> Replace "package" by the name of the package you're interested in

https://stackoverflow.com/questions/4888027/python-and-pip-list-all-versions-of-a-package-thats-available

## Rollback une ou plusieurs migrations

https://stackoverflow.com/questions/32123477/how-to-revert-the-last-migration

# Erreurs courantes

...
