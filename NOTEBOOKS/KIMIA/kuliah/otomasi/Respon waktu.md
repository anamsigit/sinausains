respon keluaran (output) dari sistem merupakan jumlahan dari 2 respon:
1. Respon paksa (steady-state)
2. Respon alami

## Kasus sistem orde pertama

Respon sistem terhadap input step
![f5ccf0dec41ba861db2dc145657cc359.png](../../../../_resources/f5ccf0dec41ba861db2dc145657cc359.png)

fungsi step adalah ketika secara spontan (tiba-tiba) ada singal umumnya bernilai antara 0 (tidak ada singal) dan 1 (ada singal). 

![12bd2966f2050227551f47d091171527.png](../../../../_resources/12bd2966f2050227551f47d091171527.png)

misalnya menentukan output dari sistem transfer apabila inputnya adalah fungsi step, maka penyusun outputnya adalah respon paksa + respon alami. 


contoh
![1651e262ed5f2079daf22153388900c5.png](../../../../_resources/1651e262ed5f2079daf22153388900c5.png)
variabel **A merupakan respon paksa** sedangkan variabel **B, C, D, E adalah respon alami** dimana nilai eksponensial ditentukan dari s + 1, s + 7, s + 8, s + 10. 

## Kasus sistem orde satu tanpa *zero*

diagram blok
![e0808d27a72bfea194e157b2d0f8b8a6.png](../../../../_resources/e0808d27a72bfea194e157b2d0f8b8a6.png)
contoh
![6c3029ea865cb28c3c2953ccfb30d698.png](../../../../_resources/6c3029ea865cb28c3c2953ccfb30d698.png)
respon paksa adalah cf(t) yaitu 1. sedangkan respon alami adalah cn(t) yaitu e^-at

respon output juga dapat diperoleh secara kualitatif lewat **konsep pole** dan **konsep nol(zero)**

1. misal untuk konsep pole:
![4f0cfc75be2aeaa43641e1e6ca8485ef.png](../../../../_resources/4f0cfc75be2aeaa43641e1e6ca8485ef.png)
apabila fungsi seperti diatas, ia bernilai -1 atau -2 ( disubstitusikan untuk s pada (s+1)(s+2)) yang membuat penyebut (bawah) bernilai nol sehingga persamaan tadi menjadi tak terhingga.

2. misal untuk konsep nol(zero):
ketika yang bagian atas (pembilang) bernilai nol, sehingga menyebabkan persamaan diatas menjadi bernilai nol (karena pembilang 0 dibagi berapapun akan menghasilkan nol)


grafik
![df6cc46aeecd0eaee47663104cde51f9.png](../../../../_resources/df6cc46aeecd0eaee47663104cde51f9.png)

glosarium terkait grafik diatas:
1. **waktu naik (*rise time*)** didefinisikan sebagai waktu yang dibutuhkan kurva respon dari 0,1 ke 0,9 dari nilai akhir. 
2. **waktu penyelesaian (setting time)** didefinisikan sebagai waktu yang dibutuhkan kurva untuk mencapai dan bertahan pada 2% dari nilai akhir

anda pasti penasaran, jika ada orde satu pasti ada orde dua? yap betul dan untuk setiap orde fungsi transfernya akan berbeda.
![7066ace3a6e8dcc83760578030e36a0b.png](../../../../_resources/7066ace3a6e8dcc83760578030e36a0b.png)
![5700d21c9e8c8d7c45ee9dea1dc1e0ac.png](../../../../_resources/5700d21c9e8c8d7c45ee9dea1dc1e0ac.png)