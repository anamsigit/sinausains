- F(0) is the DC component. 
- F(1) is the fundamental frequency (Sampling frequency) component. 
- F(2) is the second harmonic (twice the sampling frequency)
- and so on.

DFT works by measuring the Correlation with an integer multiple of frequencies. Fourier transform of the original signal f(t) will be
![0e74024891acb0d0b61fdeeec751dea6.png](../../../../_resources/0e74024891acb0d0b61fdeeec751dea6.png)
![5817c67a2098078478d47277f913cf84.png](../../../../_resources/5817c67a2098078478d47277f913cf84.png)

Hal yang perlu dipahami pada DFT adalah sinyal kontinyu atau sinyal analog pada domain waktu perlu diubah terlebih dahulu menjadi sinyal diskrit pada domain waktu dimana diambil nilainya pada titik tertentu pada suatu sinyal sepanjang waktu tertentu yang umumnya sering disebut sebagai sampel.

> DFT mampu mengetahui magnitude frekuensi-frekuensi pengganggu pada sebuah sinyal, atau mampu mengetahui magnitude banyak frekuensi pada suatu sinyal dimana hal ini sulit dilakukan pada domain waktu.

![1a5a5d5236621717b869afd5dc4b7738.png](../../../../_resources/1a5a5d5236621717b869afd5dc4b7738.png)

beberapa variabel sinyal pada domain frekuensi adalah magnitude, sudut (fasa) dan frekuensi. 

# Deret Fourier
![04650d3a8f3b343d42bcfef15de819f9.png](../../../../_resources/04650d3a8f3b343d42bcfef15de819f9.png)
apabila dijabarkan bisa dalam bentuk seperti ini
![65affbcfcda55c7b02ad0f7535ca6bf9.png](../../../../_resources/65affbcfcda55c7b02ad0f7535ca6bf9.png).

secara teoritis, nilai N bernilai tak terhingga. tetapi pada kehidupan nyata perlu membatasi hingga nilai N tertentu. A0 dapat dikatan sebagai DC

setiap nilai magnitude pada fungsi sin (Bn) dan cos (An) pada frekuensi tertentu dijumlahkan. Untuk menjumlahkan semua magnitude di atas tidak dapat dilakukan dengan penjumlahan biasa, akan tetapi dengan menjumlahkan masing-masing  magnitude secara vector pada fungsi sin dan cos yang umumnya ditulis dalam bentuk bilangan kompleks lalu dicari resultan-nya.

![38eced67fbd009f74323817fdbae4bd2.png](../../../../_resources/38eced67fbd009f74323817fdbae4bd2.png)
dapat ditulis sebagai berikut
![2c9fa5ad4ca508691cb96d661ecfe791.png](../../../../_resources/2c9fa5ad4ca508691cb96d661ecfe791.png)
f(t) merupakan magnitude dari fungsi sin dengan satu periode putaran 2π dengan frekuensi f pada nilai t tertentu dengan magnitude maksimum adalah A.

## Bilangan kompleks
terdiri dari komponen real dan imaginary.  Dengan nilai real dan imaginary dapat dicari nilai Magnitude
![f57d559a4392fe112c49ddea446156fc.png](../../../../_resources/f57d559a4392fe112c49ddea446156fc.png)
*fungsi sinyal dalam bentuk kompleks*
f(t) = A sin (2π 1/T t) dapat diasumsikan merupakan penjumlahan fungsi sin dan cos pada sinyal berwarna biru. 
![ec6511e0dc5759b4726c84d614ed6493.png](../../../../_resources/ec6511e0dc5759b4726c84d614ed6493.png)

diagram fasor yang menyatakan bahwa As merupakan vector komponen imaginary dengan nilai maksimum 1j atau sering ditulis j saja. Sedangkan Ac merupakan vector komponen real dimana magnitude maksimumnya adalah sama seperti nilai maksimum fungsi cos yaitu 1 sehingga fungsi sinyal dalam bilangan kompleks
![5dcbeafc8d8a16fae2bc24e30ac925e4.png](../../../../_resources/5dcbeafc8d8a16fae2bc24e30ac925e4.png)

diatas merupakan awal dari representasi persamaan euler
![785444ba85e4aa5e38be5da6cf752987.png](../../../../_resources/785444ba85e4aa5e38be5da6cf752987.png)

# DFT
merupakan penerapan dari deret fourier. hanya saja magnitude sinyal diambil pada waktu tertentu saja dan cukup singkat (diskrit).

Dalam satu periode terdapat total sampel yang diambil dimana total sampel tersebut lebih dikenal dengan notasi N. Kecepatan yang dibutuhkan untuk mengambil maksimum jumlah sampel pada rentang waktu tertentu disebut sebagai frekuensi sampling rate atau sample rate.

rumus DFT
![e27a1283e67e1bc32d180e955b56941c.png](../../../../_resources/e27a1283e67e1bc32d180e955b56941c.png)
atau dapat ditulis sebagai 
![17b00ec0ca0ef317641fd49f6ef4a7c2.png](../../../../_resources/17b00ec0ca0ef317641fd49f6ef4a7c2.png)

memilih salah satu metode
![26dd9f1502ace0c073fc8afcc6f28422.png](../../../../_resources/26dd9f1502ace0c073fc8afcc6f28422.png)

![85d67312648f9b476ba200084520faa9.png](../../../../_resources/85d67312648f9b476ba200084520faa9.png)

![9da3d54c838c1fe81cdbc060f8cd7362.png](../../../../_resources/9da3d54c838c1fe81cdbc060f8cd7362.png)

reference [*](https://www.belajarelektro.com/2021/06/dft.html)