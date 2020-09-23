# (یادگیری عمیق(با پایتورچ [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)
&#x202b;
این مخزن یک [وبسایت](https://atcold.github.io/pytorch-Deep-Learning/) به همراه خود دارد که تمام محتویات دوره در قالب متن و ویدیو در دسترس است.



<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - Farsi -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md)&nbsp; [🇫🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fa/README-FA.md)


# شروع
&#x202b;
برای اینکه بتوانید تمرین ها را دنبال کنید به یک لپ تاپ با Miniconda (نسخه حداقلی Anaconda) نیاز دارید. راهنمایی که در ادامه می آید برای کاربران مک و اوبونتو کار می کند. کاربران ویندوز نیاز به نصب و اجرای دستورات در ترمینال [Git BASH](https://gitforwindows.org/)  دارند.


## Miniconda دانلود و نصب
&#x202b;
لطفا به وبسایت [Anaconda](https://conda.io/miniconda.html) بروید و آخرین نسخه Miniconda برای پایتون 3.7 مخصوص سیستم عامل خود را دانلود و سپس نصب کنید.

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```


## :بررسی مخزن گیت حاوی تمرین ها
&#x202b;
وقتی Miniconda آماده شد، مخزن این دوره را بررسی کنید و محیط کار را تنظیم کنید:

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```


## Miniconda ساخت محیط ایزوله 
&#x202b;
مسیر جاری را به پوشه این دوره تغییر دهید و سپس تایپ کنید:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```


## جوپیتر نوت بوک یا جوپیترلب را اجرا کنید
&#x202b;
به طور معمول از ترمینال اجرا کنید:

```bash
jupyter lab
```
&#x202b;
یا برای رابط کلاسیک:

```bash
jupyter notebook
```


## مصور سازی نوت بوک ها
&#x202b;
جوپیتر نوت بوک ها در طول ارائه ها برای اکتشاف و مصور سازی داده ها به صورت تعاملی استفاده می شوند.

&#x202b;
ما از استایل تیره برای گیت هاب و جوپیتر نوت بوک استفاده می کنیم. پیشنهاد می شود شما نیز همین کار را انجام دهید تا ظاهر مناسبی را تجربه کنید. جوپیترلب همراه خود تم تیره دارد، بنابراین تنها در صورتی که مایل هستید از رابط نوت بوک کلاسیک استفاده کنید باید چیز دیگری نصب کنید. برای مشاهده مناسب محتویات در رابط کلاسیک موارد زیر را نصب کنید:


 - [*Jupyter Notebook* dark theme](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* dark theme](https://userstyles.org/styles/37035/github-dark) را کامنت کنید `invert #fff to #181818` کد.
