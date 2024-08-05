
![11cb779a78cb15dde2b64a2d387be639.png](../../../../../_resources/11cb779a78cb15dde2b64a2d387be639.png)
![ea1d26f819c6f7f5eaadf7fecdebd88d.png](../../../../../_resources/ea1d26f819c6f7f5eaadf7fecdebd88d.png)

What is the purpose of organizing repositories into branches?
is to enable changes to be worked on without disrupting the most current working state.

master itu adalah kerja utama, sedangkan branch adalah untuk bereksperimen

> We can use the git branch command to list, create, delete, and manipulate branches.

seperti ini
![ccc3ff069c67492d56e1c222a5301e1a.png](../../../../../_resources/ccc3ff069c67492d56e1c222a5301e1a.png)
itu menambahakan brach bernama new-feature	

gunakan 

	git checkout new-feature

untuk berpindah direktori kerja ke branch new-feature. 
jika ingin membuat dan langsung masuk dalam direktori tersebut gunakan

	git checkout -b new-feature_v2
	
bisa diketahui kita di brach atau dimaster dengan git status
![bd877c7eb69f2f9b2acb8ac5cefda0e3.png](../../../../../_resources/bd877c7eb69f2f9b2acb8ac5cefda0e3.png)
jika ingin ke master, git checkout master

gunakan git brach -d < nama branch > untuk menghapus

******
## Marging
![688b02ed70d6604acc76bbd9382c3cf3.png](../../../../../_resources/688b02ed70d6604acc76bbd9382c3cf3.png)

ilustrasi marging
![512f6b55c0821e29d15a0a6a0c7e7b17.png](../../../../../_resources/512f6b55c0821e29d15a0a6a0c7e7b17.png)
setelah di marging
![0b02c411683d7e2df77ebbd2ba4bbb48.png](../../../../../_resources/0b02c411683d7e2df77ebbd2ba4bbb48.png)

#### fast-forward and three-way merge
dua algoritma yang digunakan git dalam merge branch ke master

Fast-forward merge terjadi ketika branch yang sedang di-merge ke master memiliki riwayat commit yang linear dan tidak ada commit baru di branch master sejak branch tersebut dibuat. Dalam situasi ini, Git dapat menggabungkan branch dengan cara langsung memindahkan referensi HEAD branch utama ke referensi HEAD branch yang sedang di-merge. ilustrasinya digambarkan diatas

cara merge

![4aac95a30dd467fa9621cede26d72ec5.png](../../../../../_resources/4aac95a30dd467fa9621cede26d72ec5.png)

diatas dapat dilihat, pertama membuat file, add, dan commit (ke brach) kemudian pindah ke master dengan checkout master. setelah di master kita bisa merge brach yang dimaksud

### Git conflict
sedamgangkan three way merge  Git harus menggabungkan dua branch yang memiliki commit yang berbeda di bagian yang sama dari file. Git akan mencoba untuk menggabungkan perubahan dari kedua branch secara otomatis, tetapi jika ada konflik Git akan meminta pengguna untuk memperbaikinya secara manual. Setelah konflik diatasi, Git akan membuat commit baru yang mewakili hasil penggabungan tersebut.

![0c1dc0ec8ab63148733bfb9c1785ebce.png](../../../../../_resources/0c1dc0ec8ab63148733bfb9c1785ebce.png)

seperti diatas adalah konflik, dimana dalam 1 file ada dua pengedit berbeda yang tidak bisa di merge, maka itu diserahkan ke developer untuk mewakiliki dari kedua perubahan tersebut. 

bisa dicek dengan git status
![4ebb61d484ee5402904ab7267f64f61a.png](../../../../../_resources/4ebb61d484ee5402904ab7267f64f61a.png)

untuk itu kita bisa membuka text editor yang disetel default olehnya
![b782e4fe2edb387bd777e7c7b9bf8c1e.png](../../../../../_resources/b782e4fe2edb387bd777e7c7b9bf8c1e.png)

dan hasilnya adalah seperi ini, ada mark yang menandakan ada perubahan disitu. jika sudah developer selesaikan, bisa langsung disimpan daja, dan kembali ke terminal tadi tambahakn file tadi 

![ca546000ed5ab0db37e25c00c9f8e1d8.png](../../../../../_resources/ca546000ed5ab0db37e25c00c9f8e1d8.png)

setelah itu git commit

git log --graph --online
melihat riwayat commit secara grafis dan membaca pesan commit dengan cepat dalam satu tampilan.

![25bee480589d841d6936520c7bd5cecb.png](../../../../../_resources/25bee480589d841d6936520c7bd5cecb.png)

seperti ini yang ditampilkan
![9b23b19662b3562874bd713d651731c9.png](../../../../../_resources/9b23b19662b3562874bd713d651731c9.png)

seperti ini contoh pembenaranya
![0022fcfaf9840f9369417eec9112834b.png](../../../../../_resources/0022fcfaf9840f9369417eec9112834b.png)
mennjadi 
![81ee2be2fde167ef88276f901ea2b96e.png](../../../../../_resources/81ee2be2fde167ef88276f901ea2b96e.png)

ilustrasi yang yang 3 way algorithm git
![09e428149483f8e77a372ec350ece670.png](../../../../../_resources/09e428149483f8e77a372ec350ece670.png)

## summary
![f37a54c1f83e9b065f853ad2a32a200c.png](../../../../../_resources/f37a54c1f83e9b065f853ad2a32a200c.png)

command would we use to throw away a merge, and start over is git --abort

ini saya di VM qwilabs
![b1868937c4f2a70c5e6bdfd946fcc5c9.png](../../../../../_resources/b1868937c4f2a70c5e6bdfd946fcc5c9.png)

masuk ges, itu adalah hasil git log, karena tadi saya telah commit maka nama saya tercatat disitu, untuk keluar dari log, ketikkan q dan enter

ketika di revert itu, adalah ketika dimana kesalahan itu ditemukan
misalnya aziz mengkomit, dan di aziz ternyata ditemui kesalahm maka revertnya adalah ke aziz

git revert [ID COMMIT]
dimana ID COMMIT dapat dilihat di git log, silakan dicari dan mungkin pesan commit akan membantu
