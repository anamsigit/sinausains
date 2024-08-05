![1c464e80135af869f48655b0250c8515.png](../../../../../_resources/1c464e80135af869f48655b0250c8515.png)

ini adalah mengkopi spider.txt dari direktori sebelummnya (..) ke direktori sekaran(.)

ls: menampilkan daftar file dan direktori dalam format standar.
ls -a: menampilkan semua file, termasuk yang diawali dengan titik (.).
ls -l: menampilkan daftar file dan direktori dalam format panjang (long format), termasuk informasi tentang hak akses, pemilik file, ukuran file, waktu modifikasi, dan lain-lain.
ls -la: menampilkan semua file, termasuk yang diawali dengan titik, dalam format panjang.
ls -h: menampilkan ukuran file dalam format yang mudah dibaca manusia (human-readable), seperti kilobyte (KB) atau megabyte (MB).
ls -R: menampilkan daftar file dan direktori secara rekursif, yaitu menampilkan isi dari setiap direktori secara terperinci.
ls -t: mengurutkan daftar file dan direktori berdasarkan waktu modifikasi, dengan yang paling baru di atas.

![1041e62807008b6da04c5c2c0631b0a9.png](../../../../../_resources/1041e62807008b6da04c5c2c0631b0a9.png)

ini adalah contoh redirecting, dimana dia akan menuliskan STDOUT ke sebuah file
![0385484e15b78e17142c3268595ef76f.png](../../../../../_resources/0385484e15b78e17142c3268595ef76f.png)

yang mana file pythonya tadi adalah 

![adce0367c9e2fea6f3606f24ed816570.png](../../../../../_resources/adce0367c9e2fea6f3606f24ed816570.png)

dan dibawah ini tanda < untuk STDIN, mengarahkan suatu file ke python

![9c5450811ec865c5b96759090bb1f2b9.png](../../../../../_resources/9c5450811ec865c5b96759090bb1f2b9.png)

![02aaf3bf2bc3e55d9712cc7d414e73ce.png](../../../../../_resources/02aaf3bf2bc3e55d9712cc7d414e73ce.png)

atau secara mudahnya adalah sebagai berikut
![43d01eff784a28ce44ffe6a1ef5e806a.png](../../../../../_resources/43d01eff784a28ce44ffe6a1ef5e806a.png)

# Pipeline
![2cb07ab600f57e63092f06a3e4aede78.png](../../../../../_resources/2cb07ab600f57e63092f06a3e4aede78.png)

pipe dilambangkan dengan ' | ' 

![21db6f5ef4cff90cec6aa3deea1c1765.png](../../../../../_resources/21db6f5ef4cff90cec6aa3deea1c1765.png)

![25df9f0909183d5b1df443eb49edaba6.png](../../../../../_resources/25df9f0909183d5b1df443eb49edaba6.png)

Using signals, we can tell a program that we want it to pause or terminate. We can also cause it to reload its configuration, or to close all open files.

CTRL + C membuat terminate
CTRL + Z 
This time the process didn't finish properly. We get a message saying that it's stopped. What's going on? The signal that we sent is called SIGSTOP. This signal causes the program to stop running without actually terminating. But don't worry, we can make it run again 

![1b14e29c308a9214cd9a54690e70efb1.png](../../../../../_resources/1b14e29c308a9214cd9a54690e70efb1.png)

kita dapat melanjutkanya lagi denan mengetikkan fg
![558eabcf01bed369346e0937a58ba1be.png](../../../../../_resources/558eabcf01bed369346e0937a58ba1be.png)

tetapi jika menggunakan CTRL + C itu membuat program finish dengan bersih

diatas dinamakan dengan SIGSTOP

To find out the PID that we want to send the signal to, we'll use the ps command which list the currently running processes. Depending on what options that we pass, it'll show different subsets of processes with different amounts of detail.

We'll run ping on one terminal, and then find its PID and kill it from a second terminal.

#### yolo ASSD

dibawah ini terbuka dua terminal, terminal satu menjalankan ping, terminal satunya lagi mencari PID untuk membunuh terminal satunya lagi yang sedang berjalan
![c8aa5609088125bb16f7861b772aa9e0.png](../../../../../_resources/c8aa5609088125bb16f7861b772aa9e0.png)

![8eb863ec6bc64ecc2d86b4d1f7ce6e39.png](../../../../../_resources/8eb863ec6bc64ecc2d86b4d1f7ce6e39.png)
kill untuk membutuh dengan menunjukkan PID nya

## Ringkasan kode
![9b9b1ef92bca30a7036ac2516c2d4fec.png](../../../../../_resources/9b9b1ef92bca30a7036ac2516c2d4fec.png)

![e1f2f1742d1630582130cc10d8ab13e6.png](../../../../../_resources/e1f2f1742d1630582130cc10d8ab13e6.png)

![de9f62325bd42cd20d0443f98be7ef84.png](../../../../../_resources/de9f62325bd42cd20d0443f98be7ef84.png)

![b9a3329cbe41984105d553ac1fd46071.png](../../../../../_resources/b9a3329cbe41984105d553ac1fd46071.png)