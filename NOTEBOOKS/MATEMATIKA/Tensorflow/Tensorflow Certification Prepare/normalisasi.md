normalisasi adalah proses untuk menyeragamkan fitur-fitur dataset yang akan dilatih sehingga diharapkan tidak ada data yang dominan hanya karena perbedaan skala saja misalnya. 

	import tensorflow as tf
	from tensorflow.keras.datasets import fashion_mnist

	# Memuat data Fashion MNIST
	(train_images, train_labels), 	(test_images, test_labels) = fashion_mnist.load_data()

	# Normalisasi data
	train_images = train_images / 255.0
	test_images = test_images / 255.0
	
membagi nilai piksel dalam citra dengan 255 untuk melakukan normalisasi data. Ini dilakukan dengan asumsi awal bahwa piksel dalam citra memiliki rentang nilai antara 0 hingga 255. Dengan membagi setiap nilai piksel dengan 255, kita mendapatkan rentang nilai antara 0 hingga 1.	 

Setelah normalisasi, train_images dan test_images akan berisi data citra yang sudah dinormalisasi, dengan piksel-piksel dalam rentang 0 hingga 1.