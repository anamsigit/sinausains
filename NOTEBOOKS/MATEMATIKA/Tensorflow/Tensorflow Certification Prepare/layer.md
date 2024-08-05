    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
	
model yang dibuat adalah terdiri atas
### Convolutional Layers (Layer Konvolusi):
Layer konvolusi bertanggung jawab untuk mengekstraksi fitur lokal dari gambar input menggunakan operasi konvolusi. Setiap layer konvolusi terdiri dari beberapa filter atau kernel yang digeser di atas gambar input dan melakukan perkalian dan penjumlahan elemen demi elemen untuk menghasilkan peta fitur. Peta fitur ini menangkap pola, tekstur, atau tepi yang berbeda yang ada dalam gambar input. Layer konvolusi mampu belajar dan mendeteksi fitur-fitur level rendah secara otomatis, seperti garis, lengkungan, atau gradien. Mereka adalah komponen utama dalam membangun jaringan saraf konvolusi (CNN).

### Max Pooling Layers (Layer Max Pooling):
Layer max pooling digunakan untuk mengurangi dimensi spasial dari peta fitur yang dihasilkan oleh layer konvolusi. Layer ini melakukan operasi pemilihan nilai maksimum pada setiap wilayah (misalnya, 2x2 atau 3x3) dalam peta fitur. Dengan mengambil nilai maksimum, layer max pooling mengabstraksi dan merangkum informasi yang relevan dari wilayah tersebut. Hal ini membantu mengurangi jumlah parameter yang perlu dipelajari oleh model, mengurangi overfitting, dan mempercepat komputasi.

### Dense Layers (Layer Dense):
Layer dense (layer terhubung penuh) adalah layer yang terdiri dari banyak neuron atau unit yang terhubung dengan semua neuron di layer sebelumnya. Layer ini mengambil semua fitur yang diperoleh dari layer sebelumnya dan menghubungkannya secara penuh (fully connected) dengan semua neuron di layer dense. Dense layers bertindak sebagai klasifikasi akhir dalam model, di mana mereka melakukan penyesuaian dan kombinasi kompleksitas fitur yang lebih tinggi untuk menghasilkan output yang akhir. Mereka juga bisa berperan dalam menyesuaikan bobot dan bias untuk menyesuaikan prediksi model dengan label yang benar.

