## number
tipe numerik dibagi 3 menjadi : int; float; dan complex. contoh complex :

	c = 1+2j
	isinstance(1+2j,complex))
	#output is true
	
integer tidak dibatasi oleh angka atau panjang tertentu namun dibatasi oleh memori yang tersedia. 

#### batasan akurasi variable tipe float
python melakukan pemotongan pada dikit ke 16 pada variable float dengan kata lain bilangan pecahan dibatasi akurasinya pada 15 desimal.

python juga mendukung bilangan imajiner dan bilangan kompleks. nilai bilangan kompleks dituliskan dalam formulasi ```x + yj``` . yakni x adalah bilangan real dan y adalah bilangan imajiner. contohnya

	c = 1 + 5j

## string
...
## boolean
#### false boolean
dapat direpresentasikan dengan None, False, 0, 0.0, 0j,  (), {}

Untuk objek yang didefinisikan sendiri, representasi nilai Boolean akan bergantung dari definisi metode khusus bernama ```__bool__(self)```. Jika metode ini mengembalikan True maka interpretasi nilai dari objeknya akan True, demikian juga sebaliknya.

## list
elemen list pada python tidak harus memiliki tipe data yang sama, tidak seperti bahasa lain. dibawah beberapa contoh pemanggilan nilai pada list :

x[-1] : mengambil elemen dengan index paling belakang ke-1 dari list x
x[3:5] : membuat list baru dari anggota elemen list x dengan index 3 sampai index 4
x[:5] : membuat list baru dari anggota elemen list x dari index 0 sampai index 4
x[-3:] : membuat list baru dari anggota elemen list x mulai index ke-3 dari belakang hingga paling belakang.
x[1:7:2] artinya membuat list dari anggota elemen List x dengan index 1 sampai index 6, dengan "step" 2 (dalam hal ini hanya index 1, 3, 5).

menghapus elemen pada list

	del x[2]

slicing operator [ ] dapat digunakan pada string untuk mengambil valuenya. sebuah string utuh berifat mutable (bisa diubah) tapi elemenya bersifat immutable (tidak bisa diubah)

> string utuh misalnya "hello world"

> elemenya berupa huruf 'o' saja pada kalimat diatas

misalnya
	x	= "Hello wordl"
	print(x[4]) #output 'o'
	print(x[6:11]) # output 'World'
	x[5]= "d" #output error
	


## tuple
tuple adalah jenis dari list yang tidak dapat diubah elemennya. umumnya digunakan data yang bersifat sekali tulis, dan dapat dieksekusi lebih cepat. contoh tupple

	x = (5,'program', 1+3j)

Seperti list, kita dapat melakukan slicing, namun pada tuple kita tidak dapat melakukan perubahan

	print(t[0:3]) # output (5, 'program', (1+3j))
	
## set
set adalah kumpulan item bersifat unik dan tanpa urutan, pada set dapat dilakukan union dan intersection sekaligus melakukan **penghapusan data duplikat otomatis**

karena bersifat unordered, maka tidak bisa diambil elemenya dengan proses slicing.

## dictionary
dictionary adalah kumpulan pasangan kunci-nilai yang bersifat tidak berurutan. untuk mengakses datanya, harus mengetahui kuncinya (key). misalnya

	d = {1:'value','key':2}
	print(d['key']) # output '2'
	
dictionary tidak bisa dipanggil dengan urutan indeks. 

## konversi antar tipe data
	print(set([1,2,3]))

mengubah list menjadi set

	print(tuple({5,6,7}))
	
mengubah set menjadi tuple. 

untuk konversi ke dictionary, data harus memenuhi persyaratan key-value. berikut adalah dua contoh konversi

list dari beberapa list yang isinya pasangan nilai menjadi dictionary

	print(dict([[1,2],[3,4]]))
	# output {1: 2, 3: 4}

contoh konversi list dari beberapa tuple yang isinya pasangan nilai menjadi dictionary

	print(dict([(3,26),(4,44)]))
	# output {3: 26, 4: 44}
	
