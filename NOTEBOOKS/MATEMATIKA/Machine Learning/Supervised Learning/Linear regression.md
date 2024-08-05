simpel eksempel
![79834a37e90894c890f02203163ede3a.png](../../../../_resources/79834a37e90894c890f02203163ede3a.png)

umunya dalam komunitas Machine learning, variabel input dinotasikan dengan variabel x, sedangkan untuk ouput adadalah y. seperti halnya notasi fungsi, f(x) = y. 

x^(1) sebagai input pertama, x^(2) sebagai input kedua and so on. 

dalam machine learning, fungsi dinamakan dengan **Model** dan ouput dari model adalah prediction yang direpresentasikan dengan notasi "y hat" (ŷ). 
![4fd7a6ba594f834af42b0c2724f52754.png](../../../../_resources/4fd7a6ba594f834af42b0c2724f52754.png)

notasi y hat (ŷ) adalah hasil prediksi model untuk input x baru, sementara y adalah nilai aktual dari output yang sesuai dengan input x tersebut

sepertin ini
![c90c8bba6d6f177ce3631056817038d2.png](../../../../_resources/c90c8bba6d6f177ce3631056817038d2.png)
jadi gampang saja, anda membuat regresi linear dari data, kemudian fungsi hasil regresi linear digunakan untuk menerima input dari data yang ingin anda prediksi (ŷ).

> anda dapat mengoptimasi (fit) fungsi regresi anda dengan meilih antara linear regresion, exponent regression and so on, dalam excel, akan ditujukan nilai R, semakin R mendekati 1, maka semakin bagus model tersebut. 

dalam training set, dikenal istilah berikut
![de2061adf2aafce2b7dc2eac568032c7.png](../../../../_resources/de2061adf2aafce2b7dc2eac568032c7.png)
w adalah intersept. mari kita variasikan w dan b
![3dc34be2f1d6230fb88a490ec4697865.png](../../../../_resources/3dc34be2f1d6230fb88a490ec4697865.png)
contoh yang pertama, paling kanan, apabila w adalah 0 dan b 1.5, maka berapapun inputnya, y hat akan berbilai 1.5. kemudian untuk contoh yang ketiga, apapun inputnya, ia akan didongkrak keatas dengan nilai b = 1. tugas kita adalah mencari nilai yang tepat untuk parameter w dan b sehingga model kita dapat mendekati hasil yang sebenarnya (traingin exampel / labelled data).

to do it, lets measure how well a line fits the training data. 	to do that we construct a **cost function**. const function ini mengukur perbedaan antara y dan y hat, menunjukkan seberapa baik model telah berhasil dalam mempelajari pola dalam data dan membuat prediksi yang akurat. dimana `(ŷ - y)^2`  atau dinamakan dengan error. 
![897ec46475d1c86a75fb621bfb60d554.png](../../../../_resources/897ec46475d1c86a75fb621bfb60d554.png)
huruf i menunjukkan data ke berapa. lebih lengkapnya tampak seperti ini, dinamakan dengan squared error cost function :
![6e0ef564dbf7eb40900faf0c8a9f883b.png](../../../../_resources/6e0ef564dbf7eb40900faf0c8a9f883b.png)
dalam aplikasinya, beberapa orang mungkin menerapkan rumus yang berbeda untuk aplikasi yang berbeda. tetapi rumus diatas adalah umum untuk linear regression. 

dapat disederhanakan dengan mensubstitusi y hat
![fbd1e2dfc47c5c4ef57a3c61389743ad.png](../../../../_resources/fbd1e2dfc47c5c4ef57a3c61389743ad.png)
![b5f951df0bb289ea0e43bd03430683c0.png](../../../../_resources/b5f951df0bb289ea0e43bd03430683c0.png)
