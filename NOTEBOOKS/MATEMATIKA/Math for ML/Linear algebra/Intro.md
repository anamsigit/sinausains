Linear Algebra is to get a handle on vectors, which will turn out to be really useful for us in solving those linear algebra problems.

![bacce6a81088374c47ff197837c69f6d.png](../../../../_resources/bacce6a81088374c47ff197837c69f6d.png)

diatas adalah distribusi tinggi orang, dari 1,5 meter sampai 2 meter. kurva diatas hanya memiliki 2 parameter yaitu ```mu```  dan  ```sigma```. dimana ```mu```  merupakan representasi dari tingginya kurva distribusi dan ```sigma``` merukan lebarnya kurva distribusi.

dan fungsi (x) direpresentasikan seperti pada gambar. dari distribusi gaussian, luas area adalah sama dengan 1 karena itu merupakan suatu probabulitas (100%). 

ketika memiliki grafik gaussian yang berbeda
![f3890d142d4b4679dbdbc9ac420ec598.png](../../../../_resources/f3890d142d4b4679dbdbc9ac420ec598.png)
kita dapat melihat bahwa besarnya ```sigma``` akan berbeda, dengan nilai  ````mu```` sama (tetap di tengah). perbedaan grafik pertama dan kedua akan memiliki fungsi (x) yang berbeda karena parameter yang berbeda, itu akan berhubungan dengan vektor dan kalkulus. 

dapat dituliskan sebagai vektor antara ```sigma``` dan ```mu```

![07ce1c5b58a424d5a3d817202501ef7e.png](../../../../_resources/07ce1c5b58a424d5a3d817202501ef7e.png)

vectors don't have to be just geometric objects in the physical order of space. They can describe directions along any sorts of axes. So we can think of vectors as just being lists.

kalkulus dapat digunakan untuk menyeselaikan beberapa permasalahan terlepas bentuk geografis, misalnya kita dapat menuliskan kinerja emisinya dalam gram CO2 per 100KM untuk fungsi membunuh berapa orang, dan pencemaran lain sebagainya. 

> vectors can be viewed as a list of numbers which describes some optimisation problem. A list of number. and position on three dimension of space in one dimension of time. 
****
dibawah ini merupakan histogram yang merepresentasikan sebaran tinggi orang dengan interval 2,5 cm

![e1885609e365a7eb1c0890fce07c033c.png](../../../../_resources/e1885609e365a7eb1c0890fce07c033c.png)

> misalnya tinggi orang dari 160 - 162,5 memiliki frekuensi 0,012 and so on

This histogram can also be represented by a vector, i.e. a list of numbers

![8c2087086e8333f7cde7f69fd492c787.png](../../../../_resources/8c2087086e8333f7cde7f69fd492c787.png)

****
![a550871ca990f8f3186749a83c3cd67c.png](../../../../_resources/a550871ca990f8f3186749a83c3cd67c.png)

contoh tabel distribusi normal. dan memenuhi persamaan : 
![be709be9d2fd2a96ab29ae9f5b01ec3d.png](../../../../_resources/be709be9d2fd2a96ab29ae9f5b01ec3d.png)
dari persamaan diatas dua parameter yang penting yaitu mu dan sigma, dua parameter tersebut dapat dimasukkan dalam vektor 
![8ee516e2890d2359833b455956748db3.png](../../../../_resources/8ee516e2890d2359833b455956748db3.png)
sehingga
![651a71100413d9c893c0de3ec39a7b87.png](../../../../_resources/651a71100413d9c893c0de3ec39a7b87.png)

sigma juga dapat dinamakan dengan standard deviation atau lebar puncak.

***
A model is only considered good if it fits the measured data well. We need a way fit a model's parameters to data and quantify how good that fit is. salah satu model itu adalah dengan menghitung **residuals** yang merupakan perbedaan nilai lapangan dengan model prediksi

![70003c48ddcde4e006623591c376b2c8.png](../../../../_resources/70003c48ddcde4e006623591c376b2c8.png)
(model prediksi bewarna pink, kesamaan bewarna hijau). kesamaan yang besar menunjukkan model semakin baik. 

beberapa cara untuk memperbaiki model adalah 
1. Increase the mean, μ.
2. Keep the standard deviation, σ, approximately the same.

The performance of a model can be quantified in a single number. One measure we can use is the Sum of Squared Residuals (SSR). 

dalam bahasa vektor kita dapat menuliskan 
![d6df4aa23d8627982a77db3715b64fb1.png](../../../../_resources/d6df4aa23d8627982a77db3715b64fb1.png)

![302d53205a79bd409cc7ffedb15dadcf.png](../../../../_resources/302d53205a79bd409cc7ffedb15dadcf.png)
***
![bc451f2f5bc2e64937416380ebacf5d0.png](../../../../_resources/bc451f2f5bc2e64937416380ebacf5d0.png)
jika anda menemui persamaan diatas, anda bisa menyelesaikanya dengan mensubstitusi (3x -2y) agar tersisa z ketemu. bahkan saya menyelesaikanya tanpa melibat x + y + z =2
