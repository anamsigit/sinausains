I/O Stream adalah mekanisme dasar untuk melakukan operasi input dan output di program anda

![836c9ec8b857696df8797028dc70e115.png](../../../../../_resources/836c9ec8b857696df8797028dc70e115.png)

The standard output stream or STDOUT is a pathway between a program and a target of output, like a display

STDOUT generally takes the form of text displayed in a terminal
STDERR Standard error displays output like standard out, but is used specifically as a channel to show error messages and diagnostics from the program. It's usually printed to the screen

## Shell
adalah command line untuk berinteraksi dengan OS, di linux disebut dengan bash

we can check variables using the env or nth command

	$env

variabel defaulf
![f7cd93e58518c6a1f61588c904bdd407.png](../../../../../_resources/f7cd93e58518c6a1f61588c904bdd407.png)

python dapat berjalan di command prompt
membuat variable
![e72ddd44d45104f6df381c18bb496de0.png](../../../../../_resources/e72ddd44d45104f6df381c18bb496de0.png)

#### command line arguments 
parameter yang diteruskan ke program ketika program pertama berjalan. 

	import sys
	print(sys.argv)

#### exit status
exit status, adalah nilai yang dikembalikan oleh program ke shell
![ad5969b8f357d2e05c0dc0bc545b81d3.png](../../../../../_resources/ad5969b8f357d2e05c0dc0bc545b81d3.png)
jika program berjalan akan mengembalikan angka 0, yang berarti berhasil, dan sebaliknya. 

![d7b25646f3f0a08bba4d529183ffa2b9.png](../../../../../_resources/d7b25646f3f0a08bba4d529183ffa2b9.png)

dalam kasus tersebut, meskipun kode error digenerate oleh python itu adalah hasil tidak error, tetapi python memodifikasinya
![cb1c22e452d8dc5a0cf6e0f38bc03588.png](../../../../../_resources/cb1c22e452d8dc5a0cf6e0f38bc03588.png)

## Subproses
subproses, meaning sub of a parent proses. digunakan untuk mengeksekusi perintah shell atau subproses pada sistem operasi yang sama dengan Python. Fungsi ini mengembalikan objek CompletedProcess yang berisi informasi tentang hasil dari proses yang dijalankan.

subproses.run lebih direkomendasikan daripada os.system() dan subprocess.call()

dibawah ini hanya bisa dilakukan di python 3.7 or above untuk menjalankan capture_output
![004209fd960497074287b3dd8ec66304.png](../../../../../_resources/004209fd960497074287b3dd8ec66304.png)

0 adalah stdout yang menandakan berhasil di execute dapat dihasilkan lewat python ketika mengaktifkan capture_output=True

![6934d7e415a6708efb4d7b9ff3516638.png](../../../../../_resources/6934d7e415a6708efb4d7b9ff3516638.png)

UTF-8 adalah encode dari byte2 ada lain misalnya Big 5

![ae76f498f02728060ffa13aa22bfc6a4.png](../../../../../_resources/ae76f498f02728060ffa13aa22bfc6a4.png)
di encode secara default pengaturanya adalah engan UTF-8, kecuali anda mengubahnya sendiri

** ' **f we're automating a one-off, well-defined task, we're developing a solution quickly is the biggest requirement, then using system commands and subprocesses can help a lot** ' **

contoh nyata penggunaan subproses
1. menjalankan perintah shell dari dalam program Python. Misalnya, jika kita ingin membuat salinan backup dari file atau direktori
2. Menjalankan skrip Python dari dalam program Python: Kita juga dapat menggunakan subprocess.run() untuk menjalankan skrip Python lain dari dalam program Python
3. menangkap output dari perintah shell atau subproses yang dijalankan. Misalnya, jika kita ingin menjalankan perintah ls pada sistem Unix dan menangkap outputnya
4. menjalankan subproses dengan opsi tambahan seperti mengatur direktori kerja, mengatur variabel lingkungan, dan memasukkan masukan (input) ke dalam subproses. contoh script

import subprocess

	# Menjalankan skrip Python lain dengan opsi tambahan
	result = subprocess.run(['python', 'other_script.py', '--dir', '/path/to/dir'], cwd='/path/to/script')

tiap spasi dalam terminal, direpresentasikan commas (,) dalam subproses ini

# log files

![006b9a626fbec66ce3cbf3bf9e50c088.png](../../../../../_resources/006b9a626fbec66ce3cbf3bf9e50c088.png)

ini adalah hasil log files, kita dapat memanfaatkan regex untuk ekstraksi / memfilter informasi yang dapat diambil dari log files.

misalnya adalah seperti ini![9ab3c11bb9a9c22ceb7e1858b5a871f7.png](../../../../../_resources/9ab3c11bb9a9c22ceb7e1858b5a871f7.png)

kita masukkan ke script
![500f65a1e36ac5cdee841e2082540d79.png](../../../../../_resources/500f65a1e36ac5cdee841e2082540d79.png)
 
 
 ini 

 ![05fdd869bcff9849c825d6e916c3ad7d.png](../../../../../_resources/05fdd869bcff9849c825d6e916c3ad7d.png)
 
 hasilnya
 
 ![2a940dab7f8f6ce954d725b0a1d6347f.png](../../../../../_resources/2a940dab7f8f6ce954d725b0a1d6347f.png)
 
 dia itu ekstraksi dari sys.log dengan file python ygy dan memanfaatkan pattern regex. 