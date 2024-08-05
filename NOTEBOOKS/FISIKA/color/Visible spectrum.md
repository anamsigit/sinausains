![020e773d0291095519c93157dc0c7f82.png](../../../_resources/020e773d0291095519c93157dc0c7f82.png)
*tristimulus curves graph*
grafik sebagai fungsi untuk mencari warna pada visible spectrum melalui kombinasi red, green, blue. misalnya untuk mencari warna apa yang terdapat pada panjang gelombang 800nm, maka R bernilai 1, G bernilai 0.7 dan R bernilai 0 sebagai sumbu X, dan luminance sebagai sumbu Y. 

mengapa RGB?
ketiga elemen tersebut cukup mewakilli variasi warna yang dapat dideteksi indra manusia. red merepresentasikan warna pada spektrum tinggi, green pada spektrum sedang, dan blue pada spektrum tinggi. 

![473264a5e28ab323c6f31d476e126e52.png](../../../_resources/473264a5e28ab323c6f31d476e126e52.png)
*visible spectrum*
dimana dapat menemukan hijau tua, hijau tua dapat ditemukan ketika luminance dikonsepkan. 

![dc10a6b43bb0fc0df634ac4bbb1a8d84.png](../../../_resources/dc10a6b43bb0fc0df634ac4bbb1a8d84.png)
*luminance*
luminance rendah berarti hanya sedikit atom dalam material yang memendarkan spektrum tampak. hal tersebut membuat material tersebut lebih hitam. 

![c0b558f5c39be69c467105e870c63d2a.png](../../../_resources/c0b558f5c39be69c467105e870c63d2a.png)
*visible spectrum with luminance*
konsep luminance akan memberikan variasi warna yang lebih banyak. misalnya seperti coklat. 

![d85ce056cf9a3ff3f9af942d5b9e98a3.png](../../../_resources/d85ce056cf9a3ff3f9af942d5b9e98a3.png)
*tetapi masih belum dapat untuk menemukan warna tersebut*

memperkenalkan ruang warna 3D
![1d4e4c28b46b5d7d1539d7c919b24698.png](../../../_resources/1d4e4c28b46b5d7d1539d7c919b24698.png)
koordinat diwakiliki oleh RGB yang telah dinormalisasi, R sebagai long cones(L), G sebagai midle cones(M), dan B sebagai high short(S).

dengan ruang 3D warna, setiap warna dapat direpresentasikan sebagai matrix
![861a7d469bd0f0c8c7c8eccd4ca2abd3.png](../../../_resources/861a7d469bd0f0c8c7c8eccd4ca2abd3.png)

misalnya untuk 500nm yang telah dinormalisasi. *nilai LMS ditampilkan dalam ilustrasi*
![6143cba97dbd6aab96ab566c58812212.png](../../../_resources/6143cba97dbd6aab96ab566c58812212.png)
![d1a59764bff0c5654f1423e4bb2de143.png](../../../_resources/d1a59764bff0c5654f1423e4bb2de143.png)
![44a685a28ef4f4046663cd28877492af.png](../../../_resources/44a685a28ef4f4046663cd28877492af.png)
![426663fa090ea9d2fbd82bd47d64119e.png](../../../_resources/426663fa090ea9d2fbd82bd47d64119e.png)

sistem untuk merubah panjang gelombang menjadi ruang warna 3D
![20fffc4e5bdc06f2ed038d8719ae0823.png](../../../_resources/20fffc4e5bdc06f2ed038d8719ae0823.png)
dikenal dengan persamaan parametrik
![934a336e5fd6cc741bb4773d0de2fb19.png](../../../_resources/934a336e5fd6cc741bb4773d0de2fb19.png)
persamaan parametrik memungkinkan kita menggambarkan jalur atau bentuk dalam ruang warna tristimulus dengan menggunakan parameter-parameter tertentu.

L(t)=f1(t)
M(t)=f2(t)
S(t)=f3(t)

Di sini, t adalah parameter yang bisa diatur untuk mendapatkan berbagai nilai L, M, dan S. Fungsi-fungsi akan menentukan bagaimana nilai-nilai tristimulus berubah seiring perubahan parameter t, yang pada gilirannya akan mempengaruhi warna yang dihasilkan oleh kurva tersebut.

![384ba6b5619646c26e1f9e07c2ae0c0d.png](../../../_resources/384ba6b5619646c26e1f9e07c2ae0c0d.png)

![ec5d4793e9c40326c9aee05d4b4493da.png](../../../_resources/ec5d4793e9c40326c9aee05d4b4493da.png)
parameter dalam funsi semakin besar (panjang gelombang), menghasilkan kurva tiga dimensi seperti dibawah
![3617fa8f6d3ddb1c7a015ba3b3f613e2.png](../../../_resources/3617fa8f6d3ddb1c7a015ba3b3f613e2.png)
(plot konversi panjang gelombang ke ruang warna 3D).

ruang 3D menyisakan beberapa titik yang belum diketahui warna yang akan dihasilkan
![4525a2fa89401aaf8cf4f3c5c42dac41.png](../../../_resources/4525a2fa89401aaf8cf4f3c5c42dac41.png)

cyan dan warna sebagainya yang belum terepresentasi oleh tristimulus curves graph dapat diketahui lewat ruang warna 3D
![288b68ba2d7436d05e9401ad3d130b92.png](../../../_resources/288b68ba2d7436d05e9401ad3d130b92.png)

luminance pada ruang warna 3D akan mengarahkan pada nilai L, M, S yang semakin mendekati nilai 0. 
![98a2079283046f436c1174418cfb2cd5.png](../../../_resources/98a2079283046f436c1174418cfb2cd5.png)

> lalu bagaimana ketika gelombang elektromagnetik dikonversi ke ruang warna 3D hanya menghasilkan sebagian warna saja?

well dalam keadaan nyata, cahaya yang dipancarkan merupakan gabungan dari cahaya yang disebut dengan cahaya polikromatik. 

![2e0bcde1071c23a5cdaf1a400bdb17fd.png](../../../_resources/2e0bcde1071c23a5cdaf1a400bdb17fd.png)