dua jenis kesalahan berdasarkan kejadiannya

1. Kesalahan sintaksis (syntax errors) atau sering disebut kesalahan penguraian (parsing errors).
2. Pengecualian (exceptions) atau sering disebut kesalahan saat beroperasi (runtime errors).

Kesalahan sintaksis terjadi ketika Python tidak dapat mengerti apa yang Anda perintahkan. 

seperti yang diketahui pembagian dengan angka nol akan menyebabkan error

	z = 0
	try:
  	x = 1 / z
  	print(x)
	except ZeroDivisionError:
  	print('cannot divide by zero')

 aplikasi sudah mengalami pengecualian sehingga yang tercetak adalah operasi print(‘cannot divide by zero’).
 
 Pernyataan except dilanjutkan dengan kelompok (tipe) kesalahan yang ingin ditangani, atau bisa juga berupa tuple dari satu atau lebih tipe kesalahan yang akan ditangani, contoh penanganan lainya 
 
 	except (FileNotFoundError, ):

atau dengan menggabungkan beberapa penanganan

	except (ValueError, TypeError):

> Di dalam statement try, arti dari except adalah __Pernyataan yang dioperasikan jika terjadi pengecualian__.

