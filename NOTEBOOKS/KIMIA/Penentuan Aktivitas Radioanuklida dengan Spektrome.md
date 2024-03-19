## Rumus Penentuan Aktivitas Gama
Aktivitas didefinisikan sebagai jumlah peluruhan radioaktif yang terjadi dalam suatu sampel nuklida per unit waktu. Penentuan aktivitas radiasi gama dapat diukur dengan spektrometer gama. Adapun persamaan matematis yang dapat digunakan untuk mengukur aktivitas tersebut pada sampel air direpresentasikan sebagai berikut

$$ A_{i} = \frac{N_{s} - N_{b}}{n \cdot yield \cdot t \cdot V }$$

`Ai` : Aktivitas
`Ns` : cacah sample
`Nb` : cacah background
`n` : efisiensi
`yield` : probabilitas pancaran gamma
`t` : lama waktu pencacahan
`V`: volume sample

Variabel `yield`  adalah probabilitas sinar gama yang dipancarkan oleh radionuklida, semakin besar probabilitasnya maka semakin terlihat serapan gama tersebut pada spektrometer. Variabel net area sampel (`Ns`) dikurangi dengan net area *background* (`Nb`) bertujuan untuk memperoleh netto cacah. Kemudian nilai variabel `n` dapat didapat dari kalibrasi efisiensi spektromerter. 

### Probabilitas Pancaran Gama
Setiap radionuklida akan memancarkan sinar gamma dengan energi yang berbeda-beda. Energi tersebut memiliki probabilitas berbeda-beda pula yang kemudian ini dinamakan dengan `yield`. Misalkan pada radionuklida Bi-215 memancarkan sinar gamma dengan energi 130.58 KeV, 224.04 KeV, dan 293.56 KeV. 

Tabel 1. Probabilitas Sinar Gama Bi-215[*](http://www.lnhb.fr/nuclear-data/nuclear-data-table/). 
![9aa0ffc2bb150dc0f8f3a40e231e8035.png](../../../_resources/9aa0ffc2bb150dc0f8f3a40e231e8035.png)

Diantara ketiga energi tersebut, energi yang memiliki probabilitas tertinggi berada pada nilai 293.56 KeV dengan nilai `yield` 23.8. Maka spektrometer akan mudah menangkap radiasi pada energi 293.56 KeV. Nilai energi tersebut juga akan digunakan untuk menentukan nilai variabel `n`.