# Duboko učenje (u PyTorch-u) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)

Ovaj repozitorijum ima [prateći sajt](https://atcold.github.io/pytorch-Deep-Learning/) gde se svi materijali kursa mogu naći u video i tekstualnom formatu.

<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - French - Farsi - Russian - Vietnamese - Serbian - Portuguese - Bengali - Hungarian -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md) &nbsp; [🇫🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fr/README-FR.md) &nbsp; [🇮🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fa/README-FA.md) &nbsp; [🇷🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ru/README-RU.md) &nbsp; [🇻🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/vi/README-VI.md) &nbsp; [🇷🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/sr/README-SR.md) &nbsp; [🇵🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/pt/README-PT.md) &nbsp; [🇧🇩](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/bn/README-BN.md) &nbsp; [🇭🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/hu/README-HU.md)


# Podešavanja

Da bi bilo moguće pratiti vežbe, potreban je laptop sa instaliranom Miniconda-om (minimalnom verzijom Anaconda-e) i nekoliko paketa jezika Python.
Naredne instrukcije rade za Mac i Ubuntu Linux, a za Windows je potrebno da se instalira i radi u [Git BASH](https://gitforwindows.org/) terminalu.


## Podešavanje radnog okruženja

Potrebno je otići na [sajt Anaconda](https://conda.io/miniconda.html).
Skinuti i instalirati *najnoviju* Miniconda verziju za *Python* 3.7 za vaš operativni sistem.

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```


## Preuzimanje git repozitorijuma sa vežbama

Kada je Miniconda spremna, potrebno je preuzeti repozitorijum kursa i nastaviti sa podešavanjem okruženja:

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```


## Kreirati izolovano Miniconda okruženje

Promeniti direktorijum (`cd`) na folder kursa, pa ukucati:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```


## Startovati Jupyter Notebook ili JupyterLab

Startovati iz terminala:

```bash
jupyter lab
```

Ili, za klasični interfejs:

```bash
jupyter notebook
```


## Vizuelizacija Notebook-a

*Jupyter Notebooks* se koriste kroz lekcije za interaktivnu analizu podataka i vizualizaciju.

Koristimo tamni stil i za *GitHub* i *Jupyter Notebook*.
Trebalo bi podesiti isto jer inače neće izgledati lepo.
JupyterLab ima ugrađenu tamnu temu koju je moguće odabrati, pa je potrebno izvršiti dodatne instalacije samo ukoliko želite da koristite klasičan interfejs notebook-a.
Da bi se sadržaj video kako treba u klasičnom interfejsu potrebno je instalirati sledeće:

 - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) i zakomentarisati `invert #fff to #181818` blok koda.
