Supervised learning adalah yang sering digunakan dalam kehidupan nyata. supervised learning berkembang degan cepat. 

salah satu algorithmnya regression, yang bersifat kuantitatif
![25c6596ee5b14e0fc2aae66bac7b3cbc.png](../../../../_resources/25c6596ee5b14e0fc2aae66bac7b3cbc.png)
atau anda bisa mengoptimasinya dengan meningkatkan fitting
![48e0a197361806d5f6b19d7f353c8c90.png](../../../../_resources/48e0a197361806d5f6b19d7f353c8c90.png)

dibawah ini adalah supervised learning untuk klasifikasi, yaitu untuk mendektesi kanker apakah termasuk kanker ganas atau jinak.
data adalah berupa ukuran kanker dan klasifikasinya (sudah diketahui). data tersebut dinamakan juga labeled data
![d95bf710d236969280b9c488a3e13e3c.png](../../../../_resources/d95bf710d236969280b9c488a3e13e3c.png)
sehingga ketika di plot, akan nampak dibawah ini
![78206300107666c38faa92a1fd64cb42.png](../../../../_resources/78206300107666c38faa92a1fd64cb42.png)
pertanyaanya adalah bagaimana kita memprediksi untuk ukuran ini, termasuk kanker apakah itu
![daf536ba0d6bbddd1c8828ef6fb031ff.png](../../../../_resources/daf536ba0d6bbddd1c8828ef6fb031ff.png)
kita tambahkan kelas baru
![1a62292073168538c60be57ba97d396d.png](../../../../_resources/1a62292073168538c60be57ba97d396d.png)

sebelumnya kita hanya memiliki satu input saja, yaitu ukutan tumor. tetapi kita dapat menambahkan input lebih dari satu misalkan umur
![f1f6c09b056d7bb86674d0c7574a1713.png](../../../../_resources/f1f6c09b056d7bb86674d0c7574a1713.png)
lingkaran untuk kelas jinak dan silang untuk kelas ganas.
dalam kasusnya, ternyata kanker yang akan kita deteksi ditujukan oleh koordinat yang dibentuk titik orange. kita dapat menggunkaan algoritma klasifikasi seperti K-nearest untuk mengklasifikasikanya. 
![36b3c761c250bda043bd60a94342b9d1.png](../../../../_resources/36b3c761c250bda043bd60a94342b9d1.png)

