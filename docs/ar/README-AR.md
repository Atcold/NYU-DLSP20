<!-- Deep Learning (with PyTorch)
-->
<div dir="rtl">
 
# التعلم العميق (باستعمال PyTorch) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)
</div>

<!-- This notebook repository now has a [companion website](https://atcold.github.io/pytorch-Deep-Learning/), where all the course material can be found in video and textual format.
-->
<div dir="rtl">
 
يحتوي دفتر الملاحظات هذا الآن على [موقع ويب مصاحب](https://atcold.github.io/pytorch-Deep-Learning/ar/), حيث يمكن العثور على جميع مواد الدورة في شكل فيديو ونص.
</div>

<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md)
<!-- Getting started
-->
<div dir="rtl">
 
# البداية
</div>

<!-- To be able to follow the exercises, you are going to need a laptop with Miniconda (a minimal version of Anaconda) and several Python packages installed.
The following instruction would work as is for Mac or Ubuntu Linux users, Windows users would need to install and work in the [Git BASH](https://gitforwindows.org/) terminal.
-->
<div dir="rtl">
 
لتتمكن من متابعة التدريبات ، ستحتاج إلى جهاز كمبيوتر محمول مع Miniconda (إصدار بسيط من Anaconda) والعديد من حزم Python المثبتة.
ستعمل التعليمات التالية كما هو الحال مع مستخدمي Mac أو Ubuntu Linux ، وسيحتاج مستخدمو Windows إلى التثبيت والعمل في ملف [Git BASH](https://gitforwindows.org/).
</div>

<!-- Download and install Miniconda
-->
<div dir="rtl">

## تنزيل وتثبيت Miniconda
</div>

<!-- Please go to the [Anaconda website](https://conda.io/miniconda.html).
Download and install *the latest* Miniconda version for *Python* 3.7 for your operating system.
-->
<div dir="rtl">
 
إذهب إلى [موقع Anaconda](https://conda.io/miniconda.html).
قم بتنزيل وتثبيت * أحدث * إصدار من Miniconda لـ * Python * 3.7 لنظام التشغيل الخاص بك.
</div>

<!-- Once Miniconda is ready, checkout the course repository and proceed with setting up the environment:
-->
<div dir="rtl">
 
بمجرد أن يصبح Miniconda جاهزًا ، راجع مستودع الدورة التدريبية وتابع إعداد البيئة:
</div>

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```

<!-- Create isolated Miniconda environment
-->
<div dir="rtl">
 
## خلق بيئة Miniconda معزولة
</div>

<!-- Change directory (`cd`) into the course folder, then type:
-->
<div dir="rtl">
 
قم بتغيير الدليل (`cd`) إلى مجلد الدورة التدريبية ، ثم اكتب:
</div>

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```

<!-- Start Jupyter Notebook or JupyterLab
-->
<div dir="rtl">
 
## ابدأ Jupyter Notebook أو JupyterLab
</div>

<!-- Start from terminal as usual:
-->
<div dir="rtl">
 
ابدأ من Terminal كالمعتاد:
</div>

```bash
jupyter lab
```

<!-- Or, for the classic interface:
-->
<div dir="rtl">
 
أو للواجهة الكلاسيكية:
</div>

```bash
jupyter notebook
```

<!-- Notebooks visualisation
-->
<div dir="rtl">
 
## عرض Jupyter Notebooks
</div>

<!-- *Jupyter Notebooks* are used throughout these lectures for interactive data exploration and visualisation.
-->
<div dir="rtl">
 
يتم استخدام * Jupyter Notebooks * في جميع هذه الدروس لاستكشاف البيانات التفاعلية والتصور.
</div>

<!-- We use dark styles for both *GitHub* and *Jupyter Notebook*.
You should try to do the same, or they will look ugly.
JupyterLab has a built-in selectable dark theme, so you only need to install something if you want to use the classic notebook interface.
To see the content appropriately in the classic interface install the following:
-->
<div dir="rtl">
 
نستخدم أنماطًا داكنة لـ * GitHub * و * Jupyter Notebook *.
يجب أن تحاول أن تفعل الشيء نفسه ، أو سيبدو قبيحًا.
يحتوي JupyterLab على سمة داكنة قابلة للتحديد مضمنة ، لذلك ستحتاج فقط إلى تثبيت بعض الأشياء الإضافية إذا كنت تريد استخدام واجهة الكمبيوتر المحمول الكلاسيكية.
لعرض المحتوى بشكل صحيح في الواجهة الكلاسيكية ، قم بتثبيت ما يلي:
</div>

<!--  - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) and comment out the `invert #fff to #181818` code block.
-->
<div dir="rtl">
 
 - [النمط الداكن *Jupyter Notebook*](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [النمط الداكن *GitHub*](https://userstyles.org/styles/37035/github-dark) وقم بالتعليق خارج كتلة الكود  <span dir="ltr">`عكس #fff إلى # 181818`</span>.
</div>
