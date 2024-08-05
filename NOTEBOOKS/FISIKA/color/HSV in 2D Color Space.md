Hue Saturation Value (HSV). in CIE Color Space 2D. 
Value disebut juga dengan luminisence

Saturation disebut dengan kromatisiti, adalah jarak dari tengah grafik color space 2D, seperti diampilkan pada ilustrasi dibawah
![34a11738aa6b71eed19a1aaccfc340b3.png](../../../_resources/34a11738aa6b71eed19a1aaccfc340b3.png)
sedangkan value merepresentasikan sudut kromatisiti
![d3f7ce166f8b8f814bb4c901ef79402d.png](../../../_resources/d3f7ce166f8b8f814bb4c901ef79402d.png)
rentang dapat berkisar
![b2277a153dfbbcd7fd65fbb963215255.png](../../../_resources/b2277a153dfbbcd7fd65fbb963215255.png)

HSV diperoleh dari diagram kromatisasi
![2921b142f7eb0e1b00edba31a39113cf.png](../../../_resources/2921b142f7eb0e1b00edba31a39113cf.png)

komputer umumnya menggunakan RGB untuk merepresentasikan gambar dalam monitor. untuk mengkonversi RGB ke HSV dapat dilakukan sebagai berikut. membagi setiap parameter dengan 255, sehingga didapatkan skala 0 sampai 1. kemudian mencari nilai max dan min dari ketiga parameter, dan delta merupakan selisih dari keduanya
![e7adaeec01e421b5049fda6b7299d30b.png](../../../_resources/e7adaeec01e421b5049fda6b7299d30b.png)

v (value) didefinisikan sebagai m2*100

ref[*](https://youtu.be/gnUYoQ1pwes)