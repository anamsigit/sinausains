Spektrum yang dapat dibaca oleh spektrometer berada pada jangkauan mikrodetik. Mirkodetik adalah satu per satujuta detik. Gambaran dari Localized Surface Plasmon Resonance
![6d2d68e5f7465fc9a701b8768cd462c0.png](../../../../_resources/6d2d68e5f7465fc9a701b8768cd462c0.png)

Sumber sinar menggunakan halogen, kedalam kuvet dimasukkan air, nanopartikel emas, dan sampel. dibalik kuvet dideteksi spetrometer untuk mengukur intensitas setiap panjang gelombang serapan. 

## Kalibrasi
Kalibrasi menimbang dua variabel yaitu ref bright dan ref dark. Ketika kuvet dalam keadaan kosong, ref bright adalah ketika sumber sinar (halogen) diberikan sedangkan ref dark adalah ketika sumber sinar (halogen) dimatikan (karena anda tahu akan ada yang bocor). sehingga serapan sampel adalah hasil dari eliminasi kedua variabel tersebut dengan rumus sebagai berikut
![c4aaf106416ccfa7bbc527e0d8fe11a4.png](../../../../_resources/c4aaf106416ccfa7bbc527e0d8fe11a4.png)

Tranmisi Au adalah adalah spektrum asli dikurangi ref dark kemudian dinormalisasi dengan ref bright dikurangi ref dark dikali 100%.

> dalam software bawaan ocean optics sudah ada tombol untuk kalibrasi termasuk ref dark dan ref bright. Tetapi tidak ada fitur fitting dan lainya masih basic, oleh sebab itu kembangkan antarmuka untuk visualisasi data.

![0a98d758b9226a853f8e13e43bc36f89.png](../../../../_resources/0a98d758b9226a853f8e13e43bc36f89.png)

> pertama kali pakai skype

Seperti informasi posisi titik inflasi, pergantian model fitting(Lorentzian, Gaussian, Polinomial), posisi pada suatu titik panjang gelombang tetap (misal pada 655 nm), plotting posisi y titik inflasi terhadap waktu, plotting posisi x titik inflasi terhadap waktu, saving data.

***
## Temporary note:
estension posisi = y
ektensi pada panjang gelombang tertentu, misal pada 655 nm
diberi input. (apakah hanya satu?)
tombol
spektrum yang dibaca dan tiga variabel, 
spektrum, hasil peak fitting, extension, extensioat at 655 nm. ( di step berikutnya bisa lebih banyak multiple).

fitting itu distep berikutnya 

fitur fitting
gaussian, polinomial, loretzian
MB ada dua peak maka perlu polinomial. 
deconvolusi (terdiri lebih dari satu puncak)

deadline kapan. urgent: dalam bulan ini. 

data virtual. 