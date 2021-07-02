# Deep Learning (PyTorch könyvtárral) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)

Ennek a tárhelynek (*repository*) van egy [társoldala](https://atcold.github.io/pytorch-Deep-Learning/), ahol a teljes tananyag elérhető videós és írott formátumban.

<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - French - Farsi - Russian - Vietnamese - Serbian - Portuguese - Bengali - Hungarian -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md) &nbsp; [🇫🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fr/README-FR.md) &nbsp; [🇮🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fa/README-FA.md) &nbsp; [🇷🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ru/README-RU.md) &nbsp; [🇻🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/vi/README-VI.md) &nbsp; [🇷🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/sr/README-SR.md) &nbsp; [🇵🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/pt/README-PT.md) &nbsp; [🇧🇩](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/bn/README-BN.md) &nbsp; [🇭🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/hu/README-HU.md)


# Első lépések

A kurzus elvégzéséhez szükséged lesz egy laptopra, melyen telepítve van a Minicoda (az Anaconda egyszerűsített verziója) illetve néhány Python könyvtár (*package*). Az alábbi lépéseket Mac illetve Ubuntu Linux felhasználók a *terminal* ablakban tudják végrehajtani. Windows felhasználóknak szüksége lesz a [Git BASH](https://gitforwindows.org/) telepítésére.

## A Miniconda letöltése és telepítése

Kérlek menj az [Anaconda weboldalára](https://conda.io/miniconda.html).
Tölts le és telepítsd a Miniconda *legújabb Python 3.7* verzióját az operációs rendszerednek megfelelően.

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```


## Git tárhely klónozása

A Miniconda telepítése után klónozd a kurzus tárhelyét és folytatsd a programozási környezet konfigurálásával.

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```


## Hozz létre egy különalló Miniconda környezetet

Navigálj (`cd`) a kurzus könyvtárába, majd gépeld a következőt:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```


## Indítsd el a Jupyter Notebook vagy a JupyterLab alkalmazást

JupterLab:

```bash
jupyter lab
```

Jupyter Notebook:

```bash
jupyter notebook
```


## Vizualizáció

A kurzus folyamán a *Jupyter Notebook-ot* használjuk interaktív adatfeltárásra és vizualizációra.

Sötét témát használunk mindkét felületen: *GitHub* és *Jupyter Notebook*. Javasoljuk, hogy te is ezt használd a megfelelő megjelenítés érdekében.
A JupyterLab-nek van beépített sötét témája, így csak akkor kell valamit telepítened, ha a klasszikus (Jupyter Notebook) interfészt használod.
Amennyiben a Jupyter Notebook-ot használod, a tartalom megfelelő megjelenítése érdekében telepíts az alábbiakat:

 - [*Jupyter Notebook* sötét téma](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* sötét téma](https://userstyles.org/styles/37035/github-dark) és kommenteld ki az `invert #fff to #181818` kódrészletet.
