# 딥러닝 (with PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)

[웹사이트](https://atcold.github.io/pytorch-Deep-Learning/)를 방문해보세요! 비디오와 텍스트 형식의 모든 강의 자료를 확인하실 수 있습니다!

# 시작하기

이 강의를 위해, 미니콘다(아나콘다의 경량화 버전)과 몇 가지 파이썬 패키지가 설치된 컴퓨터가 필요합니다.
아래 과정은 Mac 또는 Ubuntu Linux 사용자를 위한 것입니다. 윈도우 유저는 [Git BASH](https://gitforwindows.org/) 터미널을 사용하여 실행할 수 있습니다.


## 미니콘다 다운로드 & 설치하기

[아나콘다 웹사이트](https://conda.io/miniconda.html)에 방문하세요.
본인의 운영체제에 맞는 파이썬 3.7을 지원하는 *최신 버전* 미니콘다를 다운로드하여 설치해주세요.

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```


## Git Repository 다운로드

미니콘다가 설치되면, 이 강의 repository를 다운로드하세요.

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```


## 독립된 미니콘다 가상환경 생성하기

`cd`명령어로 다운받은 repository 경로로 이동한 후, 아래 코드를 실행하세요.

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```


## 주피터 노트북 혹은 주피터 랩을 실행하기

아래 명령어로 주피터 랩을 실행하거나:

```bash
jupyter lab
```

주피터 노트북을 실행하세요:

```bash
jupyter notebook
```


## 주피터 노트북 시각화

*주피터 노트북*은 이 강의에서 동적인 데이터 탐색과 시각화를 위해 사용됩니다.

이 강의에서는 *Github*와 *주피터 노트북*의 다크 테마를 사용합니다.
한번 사용해보세요! 훨씬 이뻐진답니다.
주피터랩은 기본 다크 테마가 내장되어 있으므로, 주피터 노트북을 사용하는 경우에만 다크 테마를 다운받으면 됩니다.
다크 테마 다운로드는 아래를 참조하세요.

 - [*주피터 노트북* 다크 테마](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* 다크 테마](https://userstyles.org/styles/37035/github-dark) 이후 `invert #fff to #181818`를 입력하세요.

