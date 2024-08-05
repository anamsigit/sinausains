#### isalpha()
jika semua karakter dalam string adalah huruf alfabet

#### isalnum() 
alfanumerik yaitu hanya huruf atau hanya angka atau berisi keduanya

#### isspace()
jika string berisi hanya karakter whitespace, seperti spasi, tab, newline, atau karakter whitespaces lainnya

#### zfill()
Anda akan menemui kebutuhan untuk menambahkan awalan 0 misalnya seperti, 0001 untuk angka awalan 1, 0101 untuk angka awalan 101, dan sebagainya. 

	angka = 5
	print (str(angka).zfill(5));
	angka = 300
	print (str(angka).zfill(5));
	
bisa juga diterapkan pada string, misalnya

	kata = 'aku'
	print (kata.zfill(5))
	# output: 00aku
	
center, membuat string menjadi ketengah dengan suatu skala yang ditentukan, misalnya

	'Dicoding'.center(20, '-')
	output:
	'------Dicoding------'
	
selain center, ada juga rjust() dan ljust()

	\n

membuat baris baru

#### raw string
mencetak string sesuai dengan apa pun input atau teks yang diberikan

	print(r'Di\tIna')
	# output :Di\tIna

Seharusnya, perintah \t akan membuat tab dan menghasilkan Di    Ina, tapi karena kita menggunakan raw strings, maka kalimat tersebut secara mentah tercetak apa adanya.

#### count
mengetahui berapa kali suatu objek muncul dalam list

	genap = [2, 4, 4, 6, 6, 6]
	print(genap.count(6))

#### fungsi pengali pada list

	x = [7]*7
	print(x)
	# output: [7,7,7 ... ]
	
#### range

	print([_ for _ in range(0,20,5)])
	# output: [0, 5, 10, 15]
	
#### in dan not in

	x = " satu dua"
	print('dua' in x)
	# output: True
	
#### double variable

	apparel, color = 'shirt', 'white'
	apparel, color = color, apparel
	
#### sort
Metode sort menggunakan urutan ASCII, sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).

	kendaraan = ['motor', 'mo', 'he', 'Pesawat']
	kendaraan.sort()
	print(kendaraan)
	# output: ['Pesawat', 'he', 'mo', 'motor']
	
Untuk mengatasi kendala ini, Anda dapat memasukkan keyword str.lower pada parameter. Hal ini akan membuat metode sort menganggap semua objek menggunakan huruf kecil

	kendaraan = ['Motor', 'Mo', 'he', 'pesawat']
	kendaraan.sort(key=str.lower)
	print(kendaraan)

#### modulo
Mengembalikan sisa bagi. misalnya 13 % 3 menghasilkan 1.

#### operasi matematis

| BItwise OR
^ Bitwise XOR
& Bitwise AND
...

#### trailing commas
Koma di bagian akhir (trailing commas) umumnya bersifat opsional, kecuali untuk tipe tuple dengan satu elemen. Hal ini umumnya diperjelas dengan kurung untuk menghindari penghapusan.

	FILES = ('setup.cfg',)

