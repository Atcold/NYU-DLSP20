<span dir="rtl" align="right"> 
 
<!-- Deep Learning (with PyTorch)
-->
# التعلم العميق (باستعمال PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)

<!-- This notebook repository now has a [companion website](https://atcold.github.io/pytorch-Deep-Learning/), where all the course material can be found in video and textual format.
-->
يحتوي دفتر الملاحظات هذا الآن على [موقع ويب مصاحب](https://atcold.github.io/pytorch-Deep-Learning/es/)، حيث يمكن العثور على جميع مواد الدورة في شكل فيديو ونص.


<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - French -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md) &nbsp; [🇫🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fr/README-FR.md)

<!-- Getting started
-->
# البداية

<!-- To be able to follow the exercises, you are going to need a laptop with Miniconda (a minimal version of Anaconda) and several Python packages installed.
The following instruction would work as is for Mac or Ubuntu Linux users, Windows users would need to install and work in the [Git BASH](https://gitforwindows.org/) terminal.
-->
لتتمكن من متابعة التدريبات، ستحتاج إلى جهاز كمبيوتر محمول مع Miniconda (إصدار بسيط من Anaconda) والعديد من حزم Python المثبتة.
ستعمل التعليمات التالية كما هو الحال مع مستخدمي Mac أو Ubuntu Linux، وسيحتاج مستخدمو Windows إلى التثبيت والعمل في ملف [Git BASH](https://gitforwindows.org/).

<!-- Download and install Miniconda
-->
## تنزيل وتثبيت Miniconda

<!-- Please go to the [Anaconda website](https://conda.io/miniconda.html).
Download and install *the latest* Miniconda version for *Python* 3.7 for your operating system.
-->
إذهب إلى [موقع Anaconda](https://conda.io/miniconda.html).
قم بتنزيل وتثبيت *أحدث* إصدار من Miniconda لـ *Python* 3.7 لنظام التشغيل الخاص بك.

<!-- Once Miniconda is ready, checkout the course repository and proceed with setting up the environment:
-->
بمجرد أن يصبح Miniconda جاهزًا، راجع مستودع الدورة التدريبية وتابع إعداد البيئة:

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```

<!-- Create isolated Miniconda environment
-->
## خلق بيئة Miniconda معزولة

<!-- Change directory (`cd`) into the course folder, then type:
-->
قم بتغيير الدليل (`cd`) إلى مجلد الدورة التدريبية، ثم اكتب:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```

<!-- Start Jupyter Notebook or JupyterLab
-->
## ابدأ Jupyter Notebook أو JupyterLab

<!-- Start from terminal as usual:
-->
ابدأ من Terminal كالمعتاد:

```bash
jupyter lab
```

<!-- Or, for the classic interface:
-->
أو للواجهة الكلاسيكية:

```bash
jupyter notebook
```

<!-- Notebooks visualisation
-->
## عرض Jupyter Notebooks

<!-- *Jupyter Notebooks* are used throughout these lectures for interactive data exploration and visualisation.
-->
يتم استخدام *Jupyter Notebooks* في جميع هذه الدروس لاستكشاف البيانات التفاعلية والتصور.

<!-- We use dark styles for both *GitHub* and *Jupyter Notebook*.
You should try to do the same, or they will look ugly.
JupyterLab has a built-in selectable dark theme, so you only need to install something if you want to use the classic notebook interface.
To see the content appropriately in the classic interface install the following:
-->
نستخدم أنماطًا داكنة لـ *GitHub* و *Jupyter Notebook*.
يجب أن تحاول أن تفعل الشيء نفسه، أو سيبدو قبيحًا.
يحتوي JupyterLab على سمة داكنة قابلة للتحديد مضمنة، لذلك ستحتاج فقط إلى تثبيت بعض الأشياء الإضافية إذا كنت تريد استخدام واجهة الكمبيوتر المحمول الكلاسيكية.
لعرض المحتوى بشكل صحيح في الواجهة الكلاسيكية، قم بتثبيت ما يلي:

<!--  - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) and comment out the `invert #fff to #181818` code block.
-->
 - [النمط الداكن *Jupyter Notebook*](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [النمط الداكن *GitHub*](https://userstyles.org/styles/37035/github-dark) وقم بالتعليق خارج كتلة الكود `عكس #fff إلى # 181818`.


</span>
