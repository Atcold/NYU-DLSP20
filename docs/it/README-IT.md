# Apprendimento Profondo (con PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)


Questo repositorio di *notebook* ha un [sito che lo
accompagna](https://atcold.github.io/pytorch-Deep-Learning/it/), dove tutto il
materiale del corso puo essere trovato in formati video e testuali.

<!-- English - Mandarin - Korean - Spanish - Italian -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md)

# Iniziare

Per poter seguire gli esercizi, si avrà bisogno di un computer con Miniconda
(una version minimalista di Anaconda) e di diversi pacchetti Python installati.
Le seguenti istruzioni dovrebbero funzionare sia per utenti Mac che per quelli
che usano Ubuntu Linux, mentre utenti Windows dovrebbere installare e usare il
terminale fornito con [Git Bash](https://gitforwindows.org/).


## Scaricare e installare Miniconda

Vai al [sito di Anaconda](https://conda.io/miniconda.html). Scarica e installa
*l'ultima* version di Miniconda per *Python* 3.7 per il tuo sistema operativo.


```bash
wget <http:// url di miniconda>
sh <miniconda*.sh>
```


## Scarica il repositorio di git con gli esercizi

Una volta che Miniconda è pronto, scarica il repositorio del corso e procedi a
configurare il tuo ambiente di lavoro:

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```


## Crea un ambiente di lavoro isolato di Miniconda

Cambia cartella (`cd` -- "change directory") e vai in quella del corso, poi
scrivi:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```


## Attiva Jupter notebook o JupyterLab

Attiva dal terminale come al solito:

```bash
jupyter lab
```

Altrimenti, usa l'interfaccia classica:

```bash
jupyter notebook
```


## Visualizzazione dei notebook

I *Jupyter Notebook* sono usati durante tutte queste lezioni per l'esplorazione
e la visualizzazione interattiva di dati.

Usiamo uno stile scuro sia per *GitHub* che per *Jupyter Notebook*. Dovresti
provare a configurare entrambi nello stesso modo, o altrimenti potrebbero non
essere belli da vedere. JupyterLab ha già un tema scuro che puo' essere
selezionato, quindi devi solo installare qualche libreria se vuoi usare
l'interfaccia classica di notebook.

Per vedere il contenuto in modo appropriato usando l'interfaccia classica,
installa:

 - [Tema scuro di *Jupyter
   Notebook*](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [Tema scuro di *GitHub*](https://userstyles.org/styles/37035/github-dark) e
   commenta il blocco di codice `invert #fff to #181818`.
