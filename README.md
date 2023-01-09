# Introduction

Ce Workshop Django est donné aux étudiants de 3ème année à la HE-Arc dans le cadre du cours de développement web.

L'objectif de ce workshop est de transmettre aux étudiants les bases et les bonnes pratiques de la création d'un projet web avec le Framework Django et Vuejs. Ce workshop a également pour but de fournir un point de départ aux étudiants afin de leur permettre de créer leur projet de semestre.

Les prochaines étapes permettent de mettre en place l'environnement de développement et de suivre le workshop dans son intégralité.

# Explication des branches

Branches générales

- main : la branche contenant la version du README le plus à jour
- start : la branche contenant le code de départ du workshop Django
- end : la branche contenant le code solution du workshop Django

Branches par années

- xxxx-start : la branche contenant le code de départ du workshop Django, réalisé avec les étudiants de l'année xxxx
- xxxx-end : la branche contenant le code solution du workshop Django, réalisé avec les étudiants de l'année xxxx

# Prérequis

Dans ce workshop nous utiliserons la version 4.1.5 de Django et la version 3.2.45 de Vue.js.

La première étape est d'installer les différents prérequis listés ci-dessous.

## IMPORTANT si vous travaillez sur linux

Vous concerne si vous utilisez Linux :

Sur Linux toutes les commandes python doivent commencée par `python3`, donc `python --version` sur Windows, devra s'écrire `python3 --version` sur Linux.

Les commande pip doivent également commencée par `pip3`, donc `pip --version` sur Windows, devra s'écrire `pip3 --version` sur Linux.

C'est une source d'erreur très fréquente, il faut s'y faire au début, cela devient un automatisme par la suite...

## Python

Pour le workshop vous aurez besoin de la version de Python >= 3.8

https://www.python.org/downloads/

> Le workshop a été testé avec la version 3.11.1 de Python

> Dépendance provenant du site officiel de Django pour la version utilisé dans ce workshop https://docs.djangoproject.com/en/4.1/faq/install/#faq-python-version-support  
> Documentation Django officielle pour la version utilisée de Django https://docs.djangoproject.com/en/4.1/

```
python --version
```

## pip

pip est le "package manager" qui vient par défaut avec Python, assurez-vous simplement d'avoir une version compatible.

> Le workshop a été testé avec la version 22.3.1 de pip

```
pip --version
```

Si nécessaire, pip peut être mit à niveau avec la commande suivante.

```
python -m pip install --upgrade pip
```

## Nodejs

Pour le workshop vous aurez besoin de la version de Node.js >= 16.0

https://nodejs.org/en/

> Le workshop a été testé avec la version 18.13.0 de Node.js

> Dépendant provenant du site officiel de Vue.js https://vuejs.org/guide/quick-start.html

```
node --version
```

## npm

npm est le "package manager" qui vient par défaut avec Node.js, assurez-vous simplement d'avoir une version compatible.

> Le workshop a été testé avec la version 8.19.3 de npm

```
npm --version
```

# Installation et configuration

Vous trouverez ci-dessous les quelques commandes qui vous permettront de commencer à travailler sur le workshop.

## 1. Cloner le répo Github du workshop, vous connaissez c'est easy ;)

> SSH recommandé

(TODO): check les liens et commandes
```
git clone git@github.com:HE-Arc/workshop-django.git
cd workshop-django
git checkout start
```

## 2. Créer un environnement virtuel, c'est très important... vraiment !

**Commandes**

Créer un nouvel env virtuel

```
python -m venv .venv
```

Activer l'env virtuel

```
source .venv/Scripts/activate
# Or
. .venv/Scripts/activate
```

> Si la commande ne fonctionne pas, c'est peut être un problème de permission, essayez d'exécuter en mode admin.

**Détails et explications**

> Virtual environment en anglais, souvent abbrégé venv

Le gestionnaire de paquet en Python s'appelle pip. La technique de base consiste à créer un fichier nommé requirement.txt dans lequel nous allons pouvoir lister toutes les bibliothèques (dépendances) dont notre projet a besoin pour fonctionner correctement.

Par défaut pip installe toutes les bibliothèques globalement sur l'ordinateur, ce qui pourrait paraitre comme une bonne idée à la base car si nous avons un autre projet qui nécessite toutes ou certaines mêmes bibliothèques, les bibliothèques en question seront déjà installées... MAIS...

Mais en réfléchissement un peu on s'aperçoit très vite que c'est une très mauvaise idée. Certaines bibliothèques pourraient ne pas être compatibles ce qui pourrait rapidement devenir difficile à gérer.

Le mieux est donc de séparer toutes les bibliothèques de tous les projets quitte à devoir réinstaller dans certain cas la même version de certaines d'entre elles.

Pour ce faire nous allons utiliser les environnements virtuels qui nous permettent d'isoler un environnement afin de le séparer de celui de base et des autres que nous allons créer pour d'autres projets.

Il existe plusieurs bibliothèques qui permettent toutes de créer des environnements virtuels, vous pouvez utiliser celui que vous souhaitez. Personnellement j'utilise celui disponible directement avec Python.

Vous devez le créer une fois au début et/ou à chaque fois que vous clonez le projet. Ensuite une fois qu'il est créé pour la première fois vous n'aurez plus qu'à l'activer. Attention il ne faut pas oublier de le réactiver. Vous pouvez checker que vous avez bien l'extension VSCode "Python" (sinon installez là, elle nous sera utile par la suite).

**IMPORTANT** : les dossiers et fichiers de l'environnement virtuel ne doivent JAMAIS être push !  
**IMPORTANT 2** : l'environnement virtuel peut être construit de manière légèrement différente en fonction de l'OS, de l'environnement virtuel utilisé, ou pour d'autre raisons. Contrôlez l'architecture des dossiers de votre venv si vous avez des soucis à exécuter l'une ou l'autre des commandes suivantes et adaptez les commandes suivantes en fonction.

## 3. Installer les dépendances dans le venv

**Commandes**

> **IMPORTANT** Assurez-vous d'être dans le venv avant de lancer les commandes suivantes !

```
pip install -r requirements.txt
```

**Détails et explications**

Il existe des débats sur le net au sujet d'une meilleure utilisation de ce fichier.

Dans ce workshop et dans le projet que vous réaliserez lors de ce cours (projet de petite taille), le fichier requirements.txt est tout à fait adapté.

Mais si vous souhaitez creuser un peu, des techniques plus avancées existent et vous pouvez checker pipenv (https://pipenv-fork.readthedocs.io/en/latest/basics.html) ou encore poetry qui est encore plus avancé (https://python-poetry.org/)

## 4. Migrer et créer un utilisateur admin

```
python manage.py migrate
```

Créer un nouvel utilisateur admin et donnez-lui un mot de passe dont vous pourrez vous rappeler.

```
python manage.py createsuperuser --email admin@example.com --username admin
```

## 5. Démarrer le serveur de dev

**Commandes**

```
python manage.py runserver
```

**Détails et explications**

Il est possible de structurer son projet différemment, la structure que nous allons utilisez est basé sur celle proposée par le site de la bibliothèque Django REST Framework. Une fois que vous aurez compris et que vous serez à l'aise n'hésitez pas à chercher comment l'améliorer et l'adapter au mieux pour votre projet.

## 6. Prêt pour le workshop ?

TODO: Si vous voyez une image d'espace en atteignant `localhost:8000`... C'est que c'est tout bon !

---

**Prêt pour le workshop !**

Si vous êtes arrivés jusqu'ici sans problème, vous êtes prêt pour le workshop.  
La suite vous sera utile lorsque vous devrez créer votre propre projet pour le semestre.

---

# (TODO) Méthodologie - Comment va se dérouler le workshop ?

L'app est pré-existante. Il faudra remplir les trous (TODOs) pour la rendre fonctionnelle (eeeasy!).

On part de TODO-0-0 jusqu'à TODO-X-Y, avec à chaque étape quelques lignes à taper.

On fait une recherche dans l'arborescence (Ctrl+Shift+F avec VSCode p.ex) et on recherche les TODOs un à un.

Les réponses se trouvent dans le README sur la branche `start` mais **c'est de la triche de regarder**. C'est seulement en cas d'urgence (je vous vois).

# Initialiser un nouveau projet Django de zéro

Durant le workshop nous avons démarrés d'un projet existant, en réalité c'est juste pour nous faire gagner un peu de temps, mais c'est extrêmement simple à reproduire.

Le chapitre "setup project" de ce tuto permettent de réaliser les premières étapes du workshop (les chapitres suivants ont été vu ensemble durant le workshop) : https://www.django-rest-framework.org/tutorial/quickstart/

---

# Tips

## Installer des extensions VSCode pour aider au développement

Si vous utilisez Visual Studio Code, je vous recommande fortement d'installer et d'utiliser le pack d'extensions `Python Extension Pack`.  
Cela n'est pas obligatoire pour le workshop et vous êtes également libre d'installer ou de désinstaller des extensions proposées dans ce pack.

Il est également possible d'activer l'importation automatique dans les paramètres de Pylance :
https://code.visualstudio.com/docs/python/editing#_enable-auto-imports

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

## Installer un formatter pour Python

Il en existe plusieurs, voici celui que j'utilise :

https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0

## Rollback une ou plusieurs migrations

https://stackoverflow.com/questions/32123477/how-to-revert-the-last-migration

# Erreurs courantes

...
