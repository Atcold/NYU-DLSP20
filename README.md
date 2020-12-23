# Deep Learning (with PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)

This notebook repository now has a [companion website](https://atcold.github.io/pytorch-Deep-Learning/), where all the course material can be found in video and textual format.

<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - French - Farsi - Russian - Vietnamese - Serbian - Portuguese -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md) &nbsp; [🇫🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fr/README-FR.md) &nbsp; [🇮🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fa/README-FA.md) &nbsp; [🇷🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ru/README-RU.md) &nbsp; [🇻🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/vi/README-VI.md) &nbsp; [🇷🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/sr/README-SR.md) &nbsp; [🇵🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/pt/README-PT.md)



## COMPLETE TUTORIAL

# Installing Miniconda3

### Download it

To Install simply type this command in terminal:

```bash
 curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

   
or you can download the suitable version through website:


```bash
 https://docs.conda.io/en/latest/miniconda.html
```
   

### Install

Using Terminal navigate to the directory and Install the miniconda3 bash Miniconda3-latest-Linux-x86_64.sh (Verify the name of .sh file)

You do not want to automatically activate the conda environment, so apply this command:

```bash
conda config --set auto_activate_base false
```

   

### Source it

```bash
source ~/.bashrc
```
   

# Download Course from github

Download with git clone and Open New Terminal and apply the following command:

```bash
   git clone https://github.com/Atcold/pytorch-Deep-Learning

   cd pytorch-Deep-Learning
```



# Install Pytorch using conda

Pytorch is installed inside Conda Environment 


### Give path to the conda

 
```bash
 export PATH="parent_path/miniconda3/bin:$PATH"

```

If you dont give this command you may encounter Error “ conda: command not found”

### Create Conda Environment
 
```bash
 conda env create -f environment.yml

```

   
### Check available environment

```bash
 conda env list
```

   
### Activate the environment

```bash
  conda activate
```
  

You will notice that in terminal user@machine will become (environment)
user@machine

### Install Pytorch in this environment

   conda install pytorch torchvision cpuonly -c pytorch

# Install Jupyter Notebook using conda

```bash
 conda install jupyter
```
  

### Check what features are installed in coda

```bash
conda list
```
   
you will find the jupyter, pytorch, ipython  etc in the list shown

### Run Jupyter Notebook

With in the same terminal where environment is activated run the following command:

```bash
   jupyter notebook

```

### Close Jupyter Notebook

```bash
    Ctrl+C
```
  

### Deactivate Conda Environment


```bash
   conda deactivate 
```








