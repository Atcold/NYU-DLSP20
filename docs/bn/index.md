---
layout: default
title: ডীপ লার্নিং
author: Alfredo Canziani
lang-ref: home
lang: bn
translation-date: 17 October 2020
translator: Taniya Seth
---

**DS-GA 1008 · বসন্ত ২০২০ · [ডাটা সাইন্স-এর (তথ্য বিজ্ঞানের) জন্য এন-হোয়াই-ইউ কেন্দ্র](http://cds.nyu.edu/)**

| প্রশিক্ষক | Yann LeCun ও Alfredo Canziani |
| লেকচার    | প্রতি সোমবার ১৬:৫৫-১৮:৩৫, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| প্র্যাক্টিক্যাল    | প্রতি মঙ্গলবার ১৯:১০-২০:০০, [GCASL C95](http://library.nyu.edu/services/campus-media/classrooms/gcasl-c95/) |
| ফোরাম       | [r/NYU_DeepLearning](https://www.reddit.com/r/NYU_DeepLearning/) |
| শিক্ষাসামগ্রী    | [Google Drive](https://bitly.com/DLSP20), [Notebooks](https://github.com/Atcold/pytorch-Deep-Learning) |

## বর্ণনা

এই কোর্সটি ডীপ লার্নিং এবং রিপ্রেজেন্টেশন লার্নিং-এর সর্বশেষতম কৌশলগুলিকে শেখায়। কোর্সটি নিম্নলিখিত কৌশলগুলিকে প্রাধান্য দেয়- সুপারভাইজ্ড ও আনসুপারভাইজ্ড ডীপ লার্নিং, এমবেডিং মেথডস, মেট্রিক লার্নিং, কনভলিউশনাল ও রেকার্রেন্ট নেটওয়ার্কস, এইগুলির কম্পিউটার ভিশন, ন্যাচারাল ল্যাংগুয়েজ আন্ডারস্টেন্ডিং এবং স্পীচ রিকগ্নিশন-এর এপ্লিকেশন সহ। কোর্সটির পূর্বশর্ত হলো-[DS-GA 1001 ডাটা সাইন্স-এর (তথ্য বিজ্ঞানের) ভূমিকা](https://cds.nyu.edu/academics/ms-curriculum/) অথবা একটি গ্রাজুয়েট লেভেলের মেশিন লার্নিং কোর্স।

## লেকচার

**লেজেন্ড**: 🖥 স্লাইড, 📓 জুপিটার নোটবুক, 🎥 ইউটিউব ভিডিও।

<table>
<!-- =============================== HEADER ================================ -->
  <thead>
    <tr>
      <th>সপ্তাহ</th>
      <th align="left">বিন্যাস</th>
      <th align="left">শিরোনাম</th>
      <th align="left">শিক্ষাসামগ্রী</th>
    </tr>
  </thead>
  <tbody>
<!-- =============================== WEEK 1 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week01/01">①</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week01/01-1">ইতিহাস এবং অনুপ্রেরণা</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Q7LtZyIS1f3TfeTGll3aDtWygh3GAfCb">🖥️</a>
        <a href="https://www.youtube.com/watch?v=0bMe_vCZo30">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week01/01-2">বিবর্তন এবং ডীপ লার্নিং</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week01/01-3">নিউরাল নেটওয়ার্ক্স</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/01-tensor_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/02-space_stretching.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=5_qrxVq1kvc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 2 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week02/02">②</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week02/02-1">স্টোকাস্টিক গ্রেডিয়েন্ট ডিসেন্ট ও ব্যাক-প্রোপাগেশন</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1w2jV_BT2hWzfOKBR02x_rB4-dfVUI6SR">🖥️</a>
        <a href="https://www.youtube.com/watch?v=d9vdh3b787Y">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week02/02-2">অনুশীলনে ব্যাক-প্রোপাগেশন</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week02/02-3">নিউরাল নেটওয়ার্ক্স-এর ট্রেনিং</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/01%20-%20Spiral%20classification.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/04-spiral_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/05-regression.ipynb">📓</a>
        <a href="https://www.youtube.com/watch?v=WAn6lip5oWk">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 3 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week03/03">③</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week03/03-1">প্যারামিটার-এর রূপান্তর</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=18UFaOGNKKKO5TYnSxr2b8dryI-PgZQmC">🖥️</a>
        <a href="https://youtu.be/FW5gFiJb-ig">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week03/03-2">CNN</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week03/03-3">ন্যাচারাল সিগনালগুলির বৈশিষ্ট্য</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/02%20-%20CNN.pdf">🖥</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/06-convnet.ipynb">📓</a>
        <a href="https://youtu.be/kwPWpVverkw">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 4 ================================ -->
    <tr>
      <td rowspan="1" align="center"><a href="en/week04/04">④</a></td>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week04/04-1">1D কনভলিউশন</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/07-listening_to_kernels.ipynb">📓</a>
        <a href="https://youtu.be/OrBEon3VlQg">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 5 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week05/05">⑤</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week05/05-1">
অপ্টিমাইজেশন-প্রথম</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1pwlGN6hDFfEYQqBqcMjWbe4yfBDTxsab">🖥️</a>
        <a href="https://youtu.be/--NZb480zlg">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week05/05-2">
অপ্টিমাইজেশন-দ্বিতীয়</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week05/05-3">CNN, অটোগ্র্যাড</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/03-autograd_tutorial.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/extra/b-custom_grads.ipynb">📓</a>
        <a href="https://youtu.be/eEzCZnOFU1w">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 6 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week06/06">⑥</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week06/06-1">CNN-এর এপ্লিকেশন</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1opT7lV0IRYJegtZjuHsKhlsM5L7GpGL1">🖥️</a>
        <a href="https://drive.google.com/open?id=1sdeVBC3nuh5Zkm2sqzdScEicRvLc_v-F">🖥️</a>
        <a href="https://youtu.be/ycbMGyCPzvE">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week06/06-2">RNNs ও আটেনশন</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week06/06-3">RNNs গুলিকে ট্রেন করা</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/08-seq_classification.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/09-echo_data.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/04%20-%20RNN.pdf">🖥️</a>
        <a href="https://youtu.be/8cAffg2jaT0">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 7 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week07/07">⑦</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week07/07-1">এনার্জি-বেসড মডেল</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1z8Dz1YtkOEJpU-gh5RIjORs3GGqkYJQa">🖥️</a>
        <a href="https://youtu.be/tVwV14YkbYs">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week07/07-2">সেল্ফ সুপারভাইজ্ড লার্নিং, এনার্জি-বেসড মডেল</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week07/07-3">অটো-এনকোডার</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/10-autoencoder.ipynb">📓</a>
        <a href="https://youtu.be/bggWQ14DD9M">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 8 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week08/08">⑧</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week08/08-1">কন্ট্রাস্টিভ মেথড</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1Zo_PyBEO6aNt0GV74kj8MQL7kfHdIHYO">🖥️</a>
        <a href="https://youtu.be/ZaVP2SY23nc">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week08/08-2">রেগুলারাইজ্ড ল্যাটেন্ট</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week08/08-3">ভেরিয়েশনাল অটো-এনকোডার গুলিকে ট্রেন করা</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/11-VAE.ipynb">📓</a>
        <a href="https://youtu.be/7Rb4s9wNOmc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 9 ================================ -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week09/09">⑨</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week09/09-1">স্প্যার্সিটি</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=1wJRzhjSqlrSqEpX4Omagb_gdIkQ5f-6K">🖥️</a>
        <a href="https://youtu.be/Pgct8PKV7iw">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week09/09-2">ওয়ার্ল্ড মডেল, জেনারেটিভ এডভারসিরিয়াল নেটওয়ার্ক</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week09/09-3">জেনারেটিভ এডভারসিরিয়াল নেটওয়ার্ক গুলিকে ট্রেন করা</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/05%20-%20Generative%20models.pdf">🖥️</a>
        <a href="https://github.com/pytorch/examples/tree/master/dcgan">📓</a>
        <a href="https://youtu.be/xYc11zyZ26M">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 10 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week10/10">⑩</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week10/10-1">কম্পিউটার ভিশন সেল্ফ সুপারভাইজ্ড লার্নিং-প্রথম</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/open?id=16lsnDN2HIBTcRucbVKY5B_U16c0tNQhR">🖥️</a>
        <a href="https://youtu.be/0KeR6i1_56g">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week10/10-2">কম্পিউটার ভিশন সেল্ফ সুপারভাইজ্ড লার্নিং-দ্বিতীয়</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week10/10-3">প্রেডিক্টিভ কন্ট্রোল</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/09%20-%20Controller%20learning.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/14-truck_backer-upper.ipynb">📓</a>
        <a href="https://youtu.be/A3klBqEWR-I">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 11 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week11/11">⑪</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week11/11-1">একটিভেশন</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1AzFVLG7D4NK6ugh60f0cJQGYF5OL2sUB">🖥️</a>
        <a href="https://drive.google.com/file/d/1rkiZy0vjZqE2w7baVWvxwfAGae0Eh1Wm">🖥️</a>
        <a href="https://drive.google.com/file/d/1tryOlVAFmazLLZusD2-UfReFMkPk5hPk">🖥️</a>
        <a href="https://youtu.be/bj1fh3BvqSU">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week11/11-2">লস</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week11/11-3">অনিশ্চয়তার অধীনে প্রেডিকশন ও পলিসি লার্নিং</a></td>
      <td>
        <a href="http://bit.ly/PPUU-slides">🖥️</a>
        <a href="http://bit.ly/PPUU-code">📓</a>
        <a href="https://youtu.be/VcrCr-KNBHc">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 12 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week12/12">⑫</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week12/12-1">ন্যাচারাল ল্যাংগুয়েজ প্রোসেসিং-এর  জন্য দীপ লার্নিং-প্রথম</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/149m3wRavTp4DQZ6RJTej8KP8gv4jnkPW/">🖥️</a>
        <a href="https://youtu.be/6D4EWKJgNn0">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week12/12-2">ন্যাচারাল ল্যাংগুয়েজ প্রোসেসিং-এর  জন্য দীপ লার্নিং-দ্বিতীয়</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week12/12-3">আটেনশন ও ট্রান্সফরমার</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/10%20-%20Attention%20%26%20transformer.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/15-transformer.ipynb">📓</a>
        <a href="https://youtu.be/f01J0Dri-6k">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 13 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week13/13">⑬</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week13/13-1">গ্রাফ কনভলিউশনাল নেটওয়ার্ক-প্রথম</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1oq-nZE2bEiQjqBlmk5_N_rFC8LQY0jQr/">🖥️</a>
        <a href="https://youtu.be/Iiv9R6BjxHM">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week13/13-2">গ্রাফ কনভলিউশনাল নেটওয়ার্ক-দ্বিতীয়</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week13/13-3">গ্রাফ কনভলিউশনাল নেটওয়ার্ক-তৃতীয়</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/11%20-%20GCN.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/16-gated_GCN.ipynb">📓</a>
        <a href="https://youtu.be/2aKXWqkbpWg">🎥</a>
      </td>
    </tr>
<!-- =============================== WEEK 14 =============================== -->
    <tr>
      <td rowspan="3" align="center"><a href="en/week14/14">⑭</a></td>
      <td rowspan="2">লেকচার</td>
      <td><a href="en/week14/14-1">স্ট্রাকচার্ড প্রেডিকশন</a></td>
      <td rowspan="2">
        <a href="https://drive.google.com/file/d/1qBu-2hYWaGYEXeX7kAU8O4S2RZ1hMjsk/">🖥️</a>
        <a href="https://youtu.be/gYayCG6YyO8">🎥</a>
      </td>
    </tr>
    <tr><td><a href="en/week14/14-2">গ্রাফিকাল মেথড</a></td></tr>
    <tr>
      <td rowspan="1">ব্যবহারিক পাঠ্যক্রম</td>
      <td><a href="en/week14/14-3">রেগুলারাইজেশন ও বয়েসিয়ান</a></td>
      <td>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/07%20-%20Regularisation.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/12-regularization.ipynb">📓</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/slides/08%20-%20Bayesian%20NN.pdf">🖥️</a>
        <a href="https://github.com/Atcold/pytorch-Deep-Learning/blob/master/13-bayesian_nn.ipynb">📓</a>
        <a href="https://youtu.be/DL7iew823c0">🎥</a>
      </td>
    </tr>
  </tbody>
</table>


## কোর্সটির  সাথে  যুক্ত মানুষ

| ভূমিকা | ছবি | যোগাযোগ | এই মানুষদের সম্পর্কে তথ্য |
|:-----|:-----:|:--------|:------|
|প্রশিক্ষক|<img src="../images/Yann.png" width="100" height="100">|<a href="https://twitter.com/ylecun">Yann LeCun</a><br>yann@cs.nyu.edu|নিউ ইয়র্ক ইউনিভার্সিটি-তে কম্পিউটার সায়েন্সের সিলভের প্রফেসর<br>ও Turing পুরস্কার বিজয়ী|
|প্রশিক্ষক|<img src="https://avatars1.githubusercontent.com/u/2119355" width="100" height="100">|<a href="https://twitter.com/alfcnz">Alfredo Canziani</a><br>canziani@nyu.edu|নিউ ইয়র্ক ইউনিভার্সিটি-তে কম্পিউটার সায়েন্সের অ্যাসিস্ট্যান্ট প্রফেসর|
|সহকারী|<img src="https://pbs.twimg.com/profile_images/1186879808845860864/czRv3g1G_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/marikgoldstein">Mark Goldstein</a><br>goldstein@nyu.edu|নিউ ইয়র্ক ইউনিভার্সিটি-তে কম্পিউটার সায়েন্সের পি-এচ-ডি স্টুডেন্ট|
|ওয়েবমাস্টার|<img src="https://pbs.twimg.com/profile_images/673997980370927616/vMXf545j_400x400.jpg" width="100" height="100">|<a href="https://twitter.com/ebetica">Zeming Lin</a><br>zl2799@nyu.edu|নিউ ইয়র্ক ইউনিভার্সিটি-তে কম্পিউটার সায়েন্সের পি-এচ-ডি স্টুডেন্ট|

## ডিসক্লেইমার

এই সাইটে পাওয়া অন্যান্য সমস্ত আর্টিকেলগুলি ইয়্যান লে কুন, আলফ্রেদো কানজিয়ানি, ইশান মিশ্রা, মাইক লুইস এবং হাভিয়ার ব্র্রেসন প্রদত্ত লেকচারের সময় নিউইয়র্ক বিশ্ববিদ্যালয়ের শিক্ষার্থীদের নেওয়া লেকচার নোট।
সুতরাং এই সবগুলো লেখা প্রায় ১৩০ জনের দ্বারা লিখিত হয়েছে , যা স্বাভাবিক ভাবেই এর একাত্বতার উপর প্রভাব ফেলে (কেউ অতীত কাল এ লেখে, কেউ আবার বর্তমানে; যেসব সংক্ষিপ্তরূপ ব্যবহৃত হয়েছে সেগুলোর মধ্যেও সবসময় মিল নাও থাকতে পারে; কেউ সংক্ষিপ্ত বাক্য লেখেন, কেউ কেউ আবার 5 বা 6 লাইন পর্যন্ত বাক্য লেখেন ইত্যাদি)।
সাধারণভাবেই এখানে কিছু ভুল থাকতে পারে: লেখার ভুল, বানানের ভুল, ইত্যাদি। তুমি যদি এরকম কিছু লক্ষ্য করে থাকো তাহলে আমরা তোমাকে স্বাগত জানাই [আমাদের সাইট এর গিটহাব রিপোসিটোরি](https://github.com/Atcold/pytorch-Deep-Learning/pulls) তে `[EN]` উল্লেখিত একটি PR
সাবমিট করার জন্য যা বুঝায় এটা ইংরেজি অনুবাদ সম্পর্কিত।

তোমার ডীপ রিডিং এর জন্য শুভকামনা!