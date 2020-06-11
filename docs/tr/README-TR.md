# Derin Öğrenme (PyTorch ile) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)

Bu kurs deposunun materyallerini yazılı ve video halinde bulabileceğiniz [ilgili site](https://atcold.github.io/pytorch-Deep-Learning/).

<!-- English - Mandarin - Korean - Spanish - Italian - Turkish -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md)

# Başlarken

Alıştırmaları takip edebilmek için Miniconda (Anaconda'nın asgari versiyonu) ve birkaç Python paketi kurulu bir bilgisayara ihtiyacınız olacak.
Aşağıdaki yönergeler Mac veya Ubuntu Linux kullancıları için geçerlidir. Windows kullanıcılarının [Git BASH](https://gitforwindows.org/) kullanması gerekli.


## Miniconda'nın indirilmesi ve yüklenmesi

[Anaconda](https://conda.io/miniconda.html)'nın sitesine giderek işletim sisteminiz için uygun olan *en güncel* *Python* 3.7 Miniconda versiyonunu indirip kurun.


```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```


## Alıştırma içeren git deposuna göz atın

Miniconda hazır olduğunda kurs deposuna göz atın ve ortamın kurulması ile devam edin.

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```

## İzole bir Miniconda ortamı oluşturun 

Kurs dizinine gelin (`cd`) daha sonra aşağıdakini yazın:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```

## Jupyter Notebook'u veya JupyerLab'ı başlatın 

Her zamanki gibi terminalden başlatın:

```bash
jupyter lab
```

Ya da klasik arayüzden:

```bash
jupyter notebook
```


## Defterlerin görüntülenmesi

*Jupyter Notebooks* dersler boyunca interaktif bir biçimde verilerin incelenmesinde ve görselleştirilmesinde kullanıldı. 

*GitHub* ve *Jupyter Notebook* için koyu tema kullanıyoruz.
Eğer çirkin görünmelerini istemiyorsan sen de öyle kullanmalısın.
JupyterLab'ın seçilebilir hazır bir koyu teması bulunuyor eğer klasik defter arayüzü kullanmak istiyorsan bir şey yüklemen gerekiyor.

İçeriği klasik arayüzde düzgün bir şekilde görüntülemek istiyorsan aşağıdakileri yükle:

 - [*Jupyter Notebook* koyu tema](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* koyu tema](https://userstyles.org/styles/37035/github-dark) `invert #fff to #181818`ve bu kod bloğunu yorum satırından çıkar.



