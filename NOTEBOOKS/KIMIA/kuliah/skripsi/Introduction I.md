Noise
lamda vs intensitas plasmon
paladium
peak bergeser ketika paladium berinteraksi dengan analit (hidrogen)

![bab7a4f7797ae53b30f0c6cc40214eb5.png](../../../../_resources/bab7a4f7797ae53b30f0c6cc40214eb5.png)

overtime
itu kondisi ideal

![8df5012b6a91aa0434b07f6ec3b5163a.png](../../../../_resources/8df5012b6a91aa0434b07f6ec3b5163a.png)
yang merah adalah noise

noise besar
![dfb55e83925609349606246546605dae.png](../../../../_resources/dfb55e83925609349606246546605dae.png)

singal harus lebih besar dari 3x noise

pendanaan

pemodelan yang mendekati puncak. untuk centroid

![195e652fca158307a6e7e6f6ed0639c7.png](../../../../_resources/195e652fca158307a6e7e6f6ed0639c7.png)

drift, yaitu proses fisika yang tidak sederhana, dirasakan oleh nanopartikel. kehadiran dari molekul. perubahan dari temperature. merubah posisi dari plasmon. 

AI untuk memisahkan drift dari real signal. 

analit: logam berat
mendektesi pb, ion Fe. 

plasmon spektroskopi, menggunakan plasmon, untuk membantu proses katalisis metilen blue. 

fiber optik, LSPR. polimer kitosan
ketika menangkap logam berat kayak pB
![6075745474408f4c7b2fb3e208e25401.png](../../../../_resources/6075745474408f4c7b2fb3e208e25401.png)

emasnya tidak stabil, ketika dicelupkan dari konsentrasi pb. masalah stabilisasi. 

plasmon katalisis
plasmon enchanced catalysis

metilen blue (limbah)
memecah dengan bantuan nanopartikel. 
menambah panas untuk memecah MB

![7908851b6bdfbe6105d0519616f96ddc.png](../../../../_resources/7908851b6bdfbe6105d0519616f96ddc.png)

peak emas bergeser kekiri dan intensitas menurun. bergeser panjang gelombang lebih rendah, nanopartikel semakin kecil karena dipecah oleh laser. 

MB, seberapa membantu kehadiran emas untuk degrasi MB, ketika ada penurunan intensitas MB maka konsentrasinya semakin menurun. 

![472236027a85823492ed702df4d9694a.png](../../../../_resources/472236027a85823492ed702df4d9694a.png)

600nm. MB, prosesnya kompleks, menjadi senyawa lebih sederhana, atau lebih transparan (tidak menyerap). rentang 300 sampai 700 hanya ada dua peak.  (cahaya tampak)

SEJARAHHH
SPR
thin film. eksitasi dengan gelombang elektromagnetik. metal adalah material plasmoik. ketika ada gelombang berjalan, maka elektronya juga ikut berosilasi. refraktif index, kepadatan material maka makin tinggi index refraktif

misal udara n=1
![ab27bfcc7f43f88156d77837004c93a1.png](../../../../_resources/ab27bfcc7f43f88156d77837004c93a1.png)
ketika ada air n = 1,3

sulit mengarahkan gelombang elektromagnetik sejajar dengan thin film. maka ditembak dari sudut tertentu, 
syarat
1. panjang gelombang elektromagnetik harus sama dengan panjang gelombang plasma material
2. momentum harus sama juga. dari elektromagnetik harus sama dengan momentum dari plasma.
![92af640e8bcb66cf515b73439bc88d41.png](../../../../_resources/92af640e8bcb66cf515b73439bc88d41.png)

kalau momentum terlalu kuat, maka tidak harmoni plasmanya (tidak sama sama bergerak)
![1877f47fa0dfcce9ade845e7b3ac9026.png](../../../../_resources/1877f47fa0dfcce9ade845e7b3ac9026.png)

momentum ada komponen vektor, 
![ebaab14e3a93b4b762b97f81d55f4883.png](../../../../_resources/ebaab14e3a93b4b762b97f81d55f4883.png)
maka penentuan momentum akan penting dengan angle tertentu (angle resonance)

pergeser dinamis
lonceng, ketika lonceng ditempelkan permen karet, trus ditempel permen karet. maka frekuensinya berbeda, ini maka momentumnya juga berbeda. 

SPR dan LSPR menghasilkan data yang sama. yaitu pergeseran plasmon resonansi. 

target pak iwan: ngikutin saya.

GUI:
bright spektrum: backgrounnya (serapan kuvet)
dark spektrum: backgrounnya (serapan kuvet yang ada sampelnya)

Intensitas au = I row - I ref / (dinormaliasi)

![2b917e88cc004e844b01497c05d47c09.png](../../../../_resources/2b917e88cc004e844b01497c05d47c09.png)

mendapatkan serapan au sebenarnya
![d363bdcca0484df70fc8e5c8fce3f0ca.png](../../../../_resources/d363bdcca0484df70fc8e5c8fce3f0ca.png)

![8c5ba9d70ed635f26158633079e04b53.png](../../../../_resources/8c5ba9d70ed635f26158633079e04b53.png)

tracking satu posisi dulu saja. 

peak gues: tebakan posisinya dimana misal di 500 (kan harus dibantu)
![9df07cf7ebce793652314951a673662f.png](../../../../_resources/9df07cf7ebce793652314951a673662f.png)

tracking secara realtime
![f326c5227d601d0f062ee9de4d59f50b.png](../../../../_resources/f326c5227d601d0f062ee9de4d59f50b.png) dengan lamda

fitting paling polynomial fitting

excel
WL = panjang gelombang
data = spektrum mentah row, setiap satuan waktu ada spektrum tersendiri. 
t = waktu
spektra = spektrum matang, row yang sudah dikurangi ref
![36cdcf4c9d28690fc51e8d62380d8995.png](../../../../_resources/36cdcf4c9d28690fc51e8d62380d8995.png)
integrasi time (int) = seberapa lama exposure spektrumnya, semakin lama pengambilan data, exposure semakin lama maka semakin lembut
triger time = tidak terlalu penting

peak = hasil fitting
c = centroid, nilai x atau pusat massa
exrinsion = nilain y nya
FWHM = lebar dari puncaknya, ternyata ketika bergeser maka FWHM juga melebar, dan ini bisa dianalisis. 

ada
FWHM 
extinsion c
dan centroid

dilihat mana yang paling stabil dimana noisenya kecil, dan driftnya paling minimum. 

puncak satu peak, yaitu palladium dan hidrogen hidrogen tidak ada peaknya. (atau mungkin peaknya diluar) 

bermain di 300nm sampai 700nm (level 1) yaitu di rentang cahaya tampak. plasmonik lebih advance mereka main di rentang infrared. 