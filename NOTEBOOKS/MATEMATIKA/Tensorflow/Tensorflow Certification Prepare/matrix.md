saya mencoba menggunakan model seperti ini

    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),  # Dense layer tambahan
        tf.keras.layers.Dense(8, activation='relu'),  # Dense layer tambahan
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

dan mendapatkan akurasi 82, kemudian saya minta chatGPT dan diberikan kode

    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
        tf.keras.layers.Conv1D(128, 5, activation='relu'),  # Menambahkan layer Conv1D
        tf.keras.layers.GlobalMaxPooling1D(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.2),  # Menambahkan layer Dropout
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
	
akurasinya naik sampai 98