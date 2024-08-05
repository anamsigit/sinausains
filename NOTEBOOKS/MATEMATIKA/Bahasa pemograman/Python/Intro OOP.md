analoginya : Di dalam pabrik mobil, terdapat berbagai jenis komponen untuk memproduksi mobil, seperti mesin, kaca, roda, dan lain sebagainya. Setiap komponen tersebut memiliki atribut dan perilaku tertentu, misalnya mesin memiliki kekuatan mesin, kaca memiliki ketahanan terhadap benturan, dan roda memiliki ukuran yang berbeda-beda.

setiap komponen tersebut dapat direpresentasikan sebagai objek. Misalnya Kaca dapat diwakili oleh objek "Kaca" yang memiliki atribut "ketahanan terhadap benturan" dan metode "membuka jendela". Roda dapat diwakili oleh objek "Roda" yang memiliki atribut "ukuran" dan metode "berputar".

pabrik mobil juga terdapat blueprint atau rancangan untuk membuat mobil, yang mirip dengan kelas dalam PBO. Blueprint tersebut berisi informasi mengenai jenis komponen yang digunakan, bagaimana cara merakit mobil, dan spesifikasi lainnya. 

Dengan menggunakan PBO, pembuatan mobil dapat dilakukan dengan lebih efisien dan terstruktur. Setiap komponen dapat dikembangkan secara terpisah, sehingga memungkinkan modifikasi atau perbaikan tanpa harus merusak bagian lainnya. Selain itu, dengan menggunakan konsep enkapsulasi, detail implementasi dari setiap komponen dapat disembunyikan, sehingga memungkinkan penggunaan kembali komponen tersebut dalam berbagai jenis mobil yang berbeda.

conoth kode dasar OOP

	class Manusia:
  	  def berbicara(self):
   	     print("Halo, apa kabar?")
        
	orang1 = Manusia()
	orang1.berbicara() # output: Halo, apa kabar?
	
akan lebih mudah memahami OOP jika diaplikasikan kedalam sebuah game. dimana beberapa karakter adalah hasil dari blueprint (class). ada satu karakter yang memiliki kekuatan terntentu, dan warna atau nama yang berbeda-beda. dengan OOP akan lebih maintenance jika dalam pemograman prosedural satu sama lainya akan terikat dan membuat variable satu satu untuk setiap karakternya. 

> saya mendapat pemahaman lebih baik dari video berikut ( 10 mins) [*](https://youtu.be/cnUJmFcyU4w)



