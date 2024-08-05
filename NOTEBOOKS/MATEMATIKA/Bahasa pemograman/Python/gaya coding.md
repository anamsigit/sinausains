saya import modul gunakan baris selanjutnya untuk memanggil modul tersebut. 

	import cv2
	import numpy

diatas adalah contoh yang benar sesuai pedoman yang direkomendasikan. kecuali jika dalam kondisi tertentu seperti  memerlukan lebih dari satu sub-library dari library yang sama

	from subprocess import Popen, PIPE

adapun urutan librarinya dari atas adalah 1) standard library 2) library pihak ketiga 3) local library atau library spesifik. dan setiap grup dipisahkan oleh baris yang kosong. Wildcard imports seperti tertulis, sedapat mungkin dihindari untuk mengatasi ketidaktahuan tentang modul apa yang di-import.

wajib dihindari menggunakan whitespace yang tidak perlu

	yes : spam(ham[1], {eggs: 2})
	no  : spam( ham[ 1 ], { eggs: 2 } )
	
gunakan spasi baik pada kanan maupun kiri diantara tanda untuk 1) assigment (=),  (+=, -=etc.), comparison (==, <, >, !=) dan boolean. Jika memungkinkan, tuliskan komentar dalam bahasa Inggris dan jangan menuliskan komentar untuk hal yang sudah langsung dapat dibaca dari kodenya. 