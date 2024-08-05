misalnya NN untuk rekognisi wajah
![1fd9ac9b429c2557873c7f8c33cb28f0.png](../../../../_resources/1fd9ac9b429c2557873c7f8c33cb28f0.png)
inputnya mungkin adalah intensitas dari setiap piksel gambar. 
![068e6ec2eaef9e2fcb6fc9b12123944a.png](../../../../_resources/068e6ec2eaef9e2fcb6fc9b12123944a.png)

training ini dinamakan dengan propagasi. 

cost function. ini mengukur perbedaan bagaimana nilai (weight) hasil training dan nilai (weight) yang akan diprediksi (untraining)
![552753077540e459b5aea30d20feb7cd.png](../../../../_resources/552753077540e459b5aea30d20feb7cd.png)
![493ae139f2826e4c35c919198de097f4.png](../../../../_resources/493ae139f2826e4c35c919198de097f4.png)
mari mengingat materi kalkulus
![8371ac3fcee36279383a7c86cb00b036.png](../../../../_resources/8371ac3fcee36279383a7c86cb00b036.png)
Cmin itu adalah yang terdekat dengan weight (hasil training). maka sebuah titk itu (hijau) dapat kita ketahui bagaimana lokasi. dengan diturunkan, kita akan tahu kemiringanya dan nilainya (positif atau negatif) ya kan dengan alat itu kita bisa melakukan operasi pada titik itu untuk mengetahui apa yang seharusnya dilakukan untuk mencapai Cmin. dan apabila kita itu telah di Cmin (global minima) turunanya akan menghasilkan 0.  

dalam keadaan nyata sangat jarang ditemukan grafik seperti diatas, akan sering menemukan yang seperti ini
![84291e2ae8d4ae4a720b6bbb1af2f1f7.png](../../../../_resources/84291e2ae8d4ae4a720b6bbb1af2f1f7.png)
ada local minima dan global minima, isolated weight. 

![cbc392b15416654461c758d1b3576a56.png](../../../../_resources/cbc392b15416654461c758d1b3576a56.png)
untuk seperti itu, jika kita ingin turun gunung 'we will need to build the jacobian by gathering together the partial derivatives of the cost function with respect to all relevant variable'.

![b2d0c4c2f8f11d8ecf29fc2034f1fffe.png](../../../../_resources/b2d0c4c2f8f11d8ecf29fc2034f1fffe.png)
itu menerapkan chain rule. back-propagation, using the chain rule, in order to train our neural networks.

![60e250ed8aaf96e84745e8b9547dc916.png](../../../../_resources/60e250ed8aaf96e84745e8b9547dc916.png)

![066f51f9ca6fa8dc6649452ce7be54df.png](../../../../_resources/066f51f9ca6fa8dc6649452ce7be54df.png)

File Contoh Neural Netork menggunakan traingin propagasi ada di : `D:\dokumen\Academic\Pemograman\python\Neural Network`

![9fcaeb006083023d08e9ecf3e0d094bd.png](../../../../_resources/9fcaeb006083023d08e9ecf3e0d094bd.png)