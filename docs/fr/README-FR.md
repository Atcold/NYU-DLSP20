<!--
Deep Learning (with PyTorch)
-->

# Apprentissage profond (avec PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)



<!--
This notebook repository now has a [companion website](https://atcold.github.io/pytorch-Deep-Learning/), where all the course material can be found in video and textual format.
-->

Ce répertoire a maintenant un [site web associé](https://atcold.github.io/pytorch-Deep-Learning/fr/), où tout le matériel de cours peut être trouvé au format vidéo et textuel.


<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - French - Farsi - Russian - Vietnamese - Serbian - Portuguese - Bengali - Hungarian -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md) &nbsp; [🇫🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fr/README-FR.md) &nbsp; [🇮🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fa/README-FA.md) &nbsp; [🇷🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ru/README-RU.md) &nbsp; [🇻🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/vi/README-VI.md) &nbsp; [🇷🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/sr/README-SR.md) &nbsp; [🇵🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/pt/README-PT.md) &nbsp; [🇧🇩](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/bn/README-BN.md) &nbsp; [🇭🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/hu/README-HU.md)

<!--
# Getting started

To be able to follow the exercises, you are going to need a laptop with Miniconda (a minimal version of Anaconda) and several Python packages installed.
The following instruction would work as is for Mac or Ubuntu Linux users, Windows users would need to install and work in the [Git BASH](https://gitforwindows.org/) terminal.
-->

# Pour commencer

Pour pouvoir suivre les exercices, vous aurez besoin d'un ordinateur portable avec Miniconda (une version minimale d'Anaconda) et plusieurs packages Python installés.
Les instructions suivantes fonctionneront telles quelles pour les utilisateurs de Mac ou Ubuntu Linux, les utilisateurs de Windows devront installer et travailler dans le terminal [Git BASH](https://gitforwindows.org/).


<!--
## Download and install Miniconda

Please go to the [Anaconda website](https://conda.io/miniconda.html).
Download and install *the latest* Miniconda version for *Python* 3.7 for your operating system.

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```
-->

## Télécharger et installer Miniconda

Veuillez-vous rendre sur le [site web d'Anaconda](https://conda.io/miniconda.html).
Téléchargez et installez la *dernière* version de Miniconda pour *Python* 3.7 pour votre système d'exploitation.

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```

<!--
## Check-out the git repository with the exercise

Once Miniconda is ready, checkout the course repository and proceed with setting up the environment:

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```
-->

## Vérifiez le dépôt git avec l'exercice

Une fois que Miniconda est prêt, consultez le répertoire des cours et procédez à la mise en place de l'environnement :

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```


<!--
## Create isolated Miniconda environment

Change directory (`cd`) into the course folder, then type:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```
-->

## Créer un environnement Miniconda isolé

Changez le répertoire (`cd`) dans le dossier du cours, puis tapez :
```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```

<!--
## Start Jupyter Notebook or JupyterLab

Start from terminal as usual:

```bash
jupyter lab
```

Or, for the classic interface:

```bash
jupyter notebook
```
-->


## Démarrer Jupyter Notebook ou JupyterLab

Dans le terminal lancez :

```bash
jupyter lab
```

Ou bien pour l'interface classique :

```bash
jupyter notebook
```


<!--
## Notebooks visualisation

*Jupyter Notebooks* are used throughout these lectures for interactive data exploration and visualisation.

We use dark styles for both *GitHub* and *Jupyter Notebook*.
You should try to do the same, or they will look ugly.
JupyterLab has a built-in selectable dark theme, so you only need to install something if you want to use the classic notebook interface.
To see the content appropriately in the classic interface install the following:

 - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) and comment out the `invert #fff to #181818` code block.
-->

## Visualisation des notebooks

Les *Notebooks Jupyter * sont utilisés tout au long de ces conférences pour l'exploration et la visualisation des données.
Nous utilisons des styles sombres pour *GitHub* et *Jupyter Notebook*.
Nous vous conseillons de faire de même sinon les rendus risques d’être moches.
JupyterLab a un thème sombre intégré sélectionnable, il vous suffit donc d'installer quelque chose si vous voulez utiliser l'interface classique.
Pour voir le contenu de manière appropriée dans l'interface classique, installez ce qui suit :

 - [*Notebooks Jupyter* thème sombre](https://userstyles.org/styles/153443/jupyter-notebook-dark) ;
 - [*GitHub* thème sombre](https://userstyles.org/styles/37035/github-dark) et commentez le bloc de code `invert #fff to #181818`.

