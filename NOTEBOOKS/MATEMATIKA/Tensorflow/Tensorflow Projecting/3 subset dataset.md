1. Train Dataset (Dataset Latih):
Digunakan untuk melatih model.
Merupakan subset terbesar dari dataset.
Data pada subset ini digunakan oleh model untuk mempelajari pola dan mengoptimalkan parameter internalnya.
Model diberi umpan balik berdasarkan kinerja pada subset ini untuk memperbaiki dirinya sendiri.

2. Validation Dataset (Dataset Validasi):
Digunakan untuk mengatur parameter model dan memilih model terbaik.
Dataset ini digunakan untuk mengukur kinerja model selama pelatihan dan membandingkan performa berbagai model yang berbeda.
Parameter model dapat disesuaikan berdasarkan kinerja pada subset validasi untuk meningkatkan kemampuan generalisasi model.

3. Test Dataset (Dataset Uji):
Digunakan untuk menguji kinerja akhir model yang telah dilatih.
Subset ini tidak digunakan selama proses pelatihan atau validasi model.
Tujuannya adalah untuk memberikan estimasi kinerja model secara objektif pada data yang belum pernah dilihat sebelumnya.
Hasil evaluasi pada subset ini digunakan untuk memberikan gambaran tentang seberapa baik model dapat digeneralisasi pada data baru.