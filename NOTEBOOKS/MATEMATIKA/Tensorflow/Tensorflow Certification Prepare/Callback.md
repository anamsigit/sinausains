callback adalah memanggil ditengah-tengah proses pelatihan model. fungsi callback akan sangat membantu dalam pengembangan machine learning. 

callback memungkinkan anda mengambil model terbaik disaat semua epochs belum selesai tereksekusi, karena tidak selalu model terbaik terdapat pada epochs terakhir. fungsi callback juga dapat menghentikan proses pelatihan yang sedang ongoing. 

atau dapat menggunakan callback untuk melacak metrik pelatihan seperti kehilangan (loss) atau akurasi pada setiap epoch (iterasi) atau batch