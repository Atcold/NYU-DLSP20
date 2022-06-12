# ডীপ লার্নিং (PyTorch সহ) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Atcold/pytorch-Deep-Learning/master)

এই নোটবুকটির রিপোজিটরি (সংগ্রহস্থল) সহ একটি [সহযোগী ওয়েবসাইট](https://atcold.github.io/pytorch-Deep-Learning/) আছে, যেইখানে এই কোর্সটির সমস্ত শিক্ষাসামগ্রী গুলি ভিডিও ও লেখা তে উপলব্ধ আছে।

<!-- English - Mandarin - Korean - Spanish - Italian - Turkish - Japanese - Arabic - French - Farsi - Russian - Vietnamese - Serbian - Portuguese - Bengali - Hungarian -->
[🇬🇧](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/README.md) &nbsp; [🇨🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/zh/README-ZH.md) &nbsp; [🇰🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ko/README-KO.md) &nbsp; [🇪🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/es/README-ES.md) &nbsp; [🇮🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/it/README-IT.md) &nbsp; [🇹🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/tr/README-TR.md) &nbsp; [🇯🇵](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ja/README-JA.md) &nbsp; [🇸🇦](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ar/README-AR.md) &nbsp; [🇫🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fr/README-FR.md) &nbsp; [🇮🇷](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/fa/README-FA.md) &nbsp; [🇷🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/ru/README-RU.md) &nbsp; [🇻🇳](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/vi/README-VI.md) &nbsp; [🇷🇸](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/sr/README-SR.md) &nbsp; [🇵🇹](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/pt/README-PT.md) &nbsp; [🇧🇩](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/bn/README-BN.md) &nbsp; [🇭🇺](https://github.com/Atcold/pytorch-Deep-Learning/blob/master/docs/hu/README-HU.md)

# সূচনা

এই কোর্সটির বিষয়বস্তুগুলিকে অনুসরণ করার জন্য আপনার Miniconda (Anaconda-র একটি সর্বনিম্ন সংস্করণ) এবং কিছু Python প্যাকেজ সহ একটি ল্যাপটপের প্রয়োজন হবে। নিম্নলিখিত নির্দেশ গুলি Mac ও Ubuntu Linux এর ব্যবহারকারীরা সরাসরি ব্যবহার করতে পারেন। Windows ব্যবহারকারীদের [Git BASH](https://gitforwindows.org/) টার্মিনাল ইনস্টল করে তাতে কাজ করতে হবে।

## Miniconda ডাউনলোড করে ইনস্টল করুন

[Anaconda ওয়েবসাইটে](https://conda.io/miniconda.html) গিয়ে আপনার অপারেটিং সিস্টেমে *Python* 3.7-এর জন্য Miniconda-র *সর্বশেষ* সংস্করণটি ডাউনলোড ও ইনস্টল করুন।

```bash
wget <http:// link to miniconda>
sh <miniconda*.sh>
```

## বিষয়বস্তু সহ Git রিপোজিটরিটি কে অনুসরণ করুন

Miniconda তৈরী হয়ে যাওয়ার পর, কোর্সের রিপোজিটরিটি কে  অনুসরণ করে এনভায়রনমেন্ট সেট-আপ করুন। :

```bash
git clone https://github.com/Atcold/pytorch-Deep-Learning
```
## একটি পৃথক Miniconda এনভায়রনমেন্ট তৈরী করুন

ডাইরেক্টরি পরিবর্তন করে (`cd`) কোর্স ফোল্ডারে আসুন। এর পর নিম্নলিখিত কমান্ডটি কে লিখুন:

```bash
# cd pytorch-Deep-Learning
conda env create -f environment.yml
source activate pDL
```

## Jupyter Notebook অথবা JupyterLab কে চালু করুন

টার্মিনাল থেকে চালু করার জন্য এটি লিখুন:

```bash
jupyter lab
```

অথবা, ক্লাসিক ইন্টারফেসের জন্য এটি লিখুন:

```bash
jupyter notebook
```

## Notebook দৃশ্যায়ন

 ডাটা এক্সপ্লোরেশন ও দৃশ্যায়ন করার জন্য এই কোর্সটির প্রত্যেকটি লেকচারে *Jupyter Notebooks*-এর ব্যবহার করা হয়েছে।

আমরা *GitHub* এবং *Jupyter Notebooks*, দুটির জন্যই ডার্ক স্টাইলের ব্যবহার করি। আপনার ও এটি করা উচিত, অন্যথা এইগুলিকে দেখতে অসুবিধা  হতে পারে। JupyterLab-এ একটি নিজস্ব ডার্ক থীম রয়েছে তাই আপনি যদি ক্লাসিক notebook ইন্টারফেসটি কে ব্যবহার করতে চান নিচের অংশটি দেখুন।

ক্লাসিক ইন্টারফেসে যথাযথভাবে সামগ্রীটি দেখতে নিম্নলিখিত গুলিকে ইনস্টল করুন:

 - [*Jupyter Notebook* ডার্ক থীম](https://userstyles.org/styles/153443/jupyter-notebook-dark);
 - [*GitHub* ডার্ক থীম](https://userstyles.org/styles/37035/github-dark) `invert #fff to #181818` কোড ব্লকটি কে কমেন্ট করুন।
