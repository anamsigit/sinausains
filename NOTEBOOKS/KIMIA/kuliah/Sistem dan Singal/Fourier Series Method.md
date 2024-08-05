subject ini pertama kali diasumsikan oleh Newton pada pengamatan bahwa cahaya putih tersusun atas beberapa spectrum. 
![478ab018e0278f0ce2db24303118e2b6.png](../../../../_resources/478ab018e0278f0ce2db24303118e2b6.png)

Fourier’s theory states that any periodic function can be synthesized using these sinusoidal waves. konsep penjumlahan sinusoidal disebut dengan Fourier series. 


# Deret Fourier
Deret Fourier adalah metode yang memperkirakan fungsi periodik sembarang (f(x)) sebagai jumlah tak hingga dari sinus dan kosinus dengan frekuensi semakin tinggi yang memberikan basis ortogonal untuk ruang fungsi solusi. Fungsi sinus dan kosinus hadir sebagai fungsi eigen

Dalam analisis Fourier, komponen dasar utama berasal dari sekumpulan sinusoid harmonik yang disebut sebagai set dasar. Set ini terdiri dari sejumlah tak terbatas sinusoid periodik dengan frekuensi yang berbeda-beda yang disebut sebagai harmonik. Setiap gelombang individu dalam set dasar disebut sebagai elemen dasar. Proses memecah sinyal periodik menjadi sejumlah gelombang dasar disebut Analisis. Sinyal periodik dapat dibangun kembali dengan menggabungkan (menambahkan) beberapa gelombang dari set dasar ini, yang disebut sebagai Proses Sintesis.

![7e532e82fee2da9ced0dfa0ee68c46bc.png](../../../../_resources/7e532e82fee2da9ced0dfa0ee68c46bc.png)
frekuensi fundamental (*1st harmonic*)

![f4515b92fc1864900d7d8c504aa56985.png](../../../../_resources/f4515b92fc1864900d7d8c504aa56985.png)
(*3rd harmonic*)

![ff8df600e03f324c39891a1a43423d7f.png](../../../../_resources/ff8df600e03f324c39891a1a43423d7f.png)
(*5th harmonic*)

*and so on ...*
> secara intuitif, pada n harmonic nilai amplitudo merupakan perkalian dari 1/n. dan merupakan kelipatan n dari freq fundamendal.

kelima harmonik ketika dijumlahkan didapatkan representasi sebagai berikut
![0219da42800c21575ca4e25543c882bd.png](../../../../_resources/0219da42800c21575ca4e25543c882bd.png)
secara matematika dapat diluliskan sebagai berikut
![6ca982b5fa05dde296096c3eb8d479eb.png](../../../../_resources/6ca982b5fa05dde296096c3eb8d479eb.png)


pada kehidupan nyata, misalnya gelombang singal analog dari audio.wav, dapat direkonstruksi dengan menjumlahkan sinyal sinusoidal setiap waktu yang sesuai. This is the basic idea of the Fourier analysis method. semakin banyak sinusoidal yang ditambahkan maka semakin merepresentasikan gelombang yang dianalisis.

komposisi frequensi dapat direpresentasikan
![105fc3a563aceb2fa48c3825ca49df59.png](../../../../_resources/105fc3a563aceb2fa48c3825ca49df59.png)
y-axis adalah nilai amplitudo frequensi. harmonik selanjutnya (3f0, 5f0, 7f0, ...) merupakan kelipatan bilangan integer dari frequensi fundamental. 

Fungsi periodik sembarang s(t) direpresentasikan sebagai berikut pada periode T0
![be3504d104c4c3f8ded079168d0ccdf5.png](../../../../_resources/be3504d104c4c3f8ded079168d0ccdf5.png)
dimana omega (w) bernilai sebagai berikut
![0d6743f59b5f2d83299cb4adcfe660da.png](../../../../_resources/0d6743f59b5f2d83299cb4adcfe660da.png)

The term ω0 ((2Π/T)  represents the fundamental frequency of the periodic function f(t). The integral multiples of ω0 like, 2ω0, 3ω0, 4ω0 So on are known as the harmonic frequencies of f(t)

koefisien s0, an, dan bn disebut Fourier Series Coefficients. konstanta s0 adalah offset DC dan koefisien an merepresentasikan gelombang kosinus sedangkan koefisien bn merepresentasikan gelombang sinus

![ad062dadbfcf6979b19b853e307dbe30.png](../../../../_resources/ad062dadbfcf6979b19b853e307dbe30.png)
*koefisien elemen ke-n*

![49003eec83e03eaf73acc9392a25c132.png](../../../../_resources/49003eec83e03eaf73acc9392a25c132.png)
*koefisien elemen kosinus*

![e886ef72b7e30a9318c27772e75d5600.png](../../../../_resources/e886ef72b7e30a9318c27772e75d5600.png)
*koefisien elemen sinus*

s(t) diekspresikan dalam domain waktu. tetapi an dan bn (sebagai absolut |an| and |bn|) dapat merepresentasikan amplitudo s(t)

apabila koefisien-koefisien diatas diaplikasikan untuk mencari Fourier series coefficients didapatkan sebagai berikut
![8db4ca0a1736792b5a57edb9dcd0de65.png](../../../../_resources/8db4ca0a1736792b5a57edb9dcd0de65.png)
![848bc067631f823596cbcee4050ec009.png](../../../../_resources/848bc067631f823596cbcee4050ec009.png)
*representasi singal f(t) dalam domain frekuensi*

koefisien an dan bn dapat direpresentasikan sebagai satu variabel independen, **Cn**, yang disebut besaran (magnitude).

![08702fa5aa27b4d5daf35b3698164f0a.png](../../../../_resources/08702fa5aa27b4d5daf35b3698164f0a.png)

karena sinus dan kosinus saling ortogonal dan memiliki frekuensi yang sama dapat dijumlahkan sebagai dua vektor dengan metode room-sum-square

![164ecbb298bf96042624e2d0c7c61808.png](../../../../_resources/164ecbb298bf96042624e2d0c7c61808.png)

![b6415158f0c8b6c809733f90069219f4.png](../../../../_resources/b6415158f0c8b6c809733f90069219f4.png)
*koefisien magnitude dalam domain frekuensi*

# Fourier Transform
merupakan sebuah konsep integral dari deret fourier. Transformasi fourier merupakan analis spektrum dasar. 

bilangan komplek kemudian disebut dengan phasor.
![61752bd5ef4a89bca9aaac13b805a3b9.png](../../../../_resources/61752bd5ef4a89bca9aaac13b805a3b9.png)
*vektor besaran sinusoidal (V) dapat diperoleh dengan vektorial real (a) dan imajiner (b), yaitu komponen sinus dan kosinus.*
menggunakan rumus euler untuk mendeskriksikan bilangan komplek V sebagai berikut

![bbc745d43ec5242076c7c069e225bbba.png](../../../../_resources/bbc745d43ec5242076c7c069e225bbba.png)
*definisi bilangan komplek V*

![fce15a99df5cc51b79be6f44314c6a8d.png](../../../../_resources/fce15a99df5cc51b79be6f44314c6a8d.png)
*kalkulasi magnitude V*

![dae601c6b995c1183d3e69a389657430.png](../../../../_resources/dae601c6b995c1183d3e69a389657430.png)
*kalkulasi komponen kosinus dari V*

![4e5c305907ae4e89133d870c8f9518b3.png](../../../../_resources/4e5c305907ae4e89133d870c8f9518b3.png)
*kalkulasi komponen sinus dari V*

As already mentioned, ‘a’ equals the real part of the complex vector ‘V’ and ‘b’ equals the imaginary part of it. 

![ac2c633948a884a04af47f04c6572c3e.png](../../../../_resources/ac2c633948a884a04af47f04c6572c3e.png)
*Definisi bagian real dan bagian imajiner V*


Reference [*](https://www.electronics-lab.com/article/the-fourier-analysis-part-1/)[*](https://www.electronics-lab.com/article/the-fourier-analysis-part-2/)