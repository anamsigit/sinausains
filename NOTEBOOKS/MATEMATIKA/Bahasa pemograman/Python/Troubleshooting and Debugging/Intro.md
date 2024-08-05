![8dca9c683f49c03e1b126eef56772d2d.png](../../../../../_resources/8dca9c683f49c03e1b126eef56772d2d.png)

we'll look at different ways that we can approach understanding what's going on and finding the root cause of an issue, including using a process ***called binary*** search to troubleshoot problems.

![57409c5f5f26c4d4cc32759e9b0dfa8b.png](../../../../../_resources/57409c5f5f26c4d4cc32759e9b0dfa8b.png)

![46056706516002a7b837ace2b43cd25b.png](../../../../../_resources/46056706516002a7b837ace2b43cd25b.png)

"Bug" merujuk pada kesalahan dalam kode yang menyebabkan program tidak berfungsi seperti yang diharapkan. Bug bisa terjadi karena kesalahan sintaksis, kesalahan logika, atau masalah pada lingkungan program

Trobleshooting
dilakukan pada tingkat yang lebih tinggi atau abstrak, dengan tujuan menemukan dan mengidentifikasi masalah serta melibatkan analisis.

Debugging
dilakukan untuk mencari dan mengidentifikasi kesalahan atau bug pada kode program yang lebih spesifik dan terfokus. melibatkan langkah-langkah teknis

## Tools
Tools like tcpdump and Wireshark can show us ongoing network connections, and help us analyze the traffic going over our cables. ools like ps, top, or free can show us the number and types of resources used in the system. We can use a tool like strace to look at the system calls made by a program, or ltrace to look at the library calls made by the software. 


1. The first step is getting information
2. Finging the root cause
3. Melakukan perbaikan yang diperlukan

![9a61a5f53a6fa4c9a9c8a62ee952e4de.png](../../../../../_resources/9a61a5f53a6fa4c9a9c8a62ee952e4de.png)

### Strace
alat ini memungkinkan melihat apa yang dilakukan program. misalnya ini

![4bdf7fc986bf2d43d2199fb945ee4cac.png](../../../../../_resources/4bdf7fc986bf2d43d2199fb945ee4cac.png)

![8b5b0d4992fd64727a1b54f63a54de8a.png](../../../../../_resources/8b5b0d4992fd64727a1b54f63a54de8a.png)


![0534823c9fd36833e8ae21e135a7e243.png](../../../../../_resources/0534823c9fd36833e8ae21e135a7e243.png)
outputnya 
use the- 0 flag of the astrois command to store the output into a file

![449a077097069717ea95d1557ab76613.png](../../../../../_resources/449a077097069717ea95d1557ab76613.png)
dari atas dapat diketahui bahwa the application tries to open a directory called .config purple box, which doesn't exist.


## Strace
 utilitas pada sistem operasi Linux yang digunakan untuk memantau sistem panggilan (system calls) dan sinyal yang dilakukan oleh sebuah program. dia mencatat seluruh interaksi program dengan sistem operasi. 
 
Strace dapat membantu mengidentifikasi masalah seperti:

1. Kesalahan saat membuka atau menutup file
2. Kesalahan saat melakukan operasi I/O (Input/Output) pada file
3. Kesalahan saat melakukan alokasi memori, dll.

gunakan 

	strace ./script.py | less  

agar tidak terlalu panjang. 