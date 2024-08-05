### String
string adalah modul bawaan python yang tidak perlu dideklasrasikan lagi (import string)

### Scrapper
Web scrapping adalah sebuah proses terotomasi untuk mendapatkan dan parsing data dari web. Disiplin seperti data science, business intelligence, dan lainnya mendapatkan banyak manfaat dari menganalisis data pada situs-situs yang ada di internet dua modul populer yang termasuk scrapper adalh 

1. urllib
2. beautifulsoup

berikut kodingnya

	from urllib.request import urlopen
	url = "http://python.org/"
	page = urlopen(url)
	html = page.read().decode("utf-8")
	start_index = html.find("<title>") + len("<title>")
	end_index = html.find("</title>")
	title = html[start_index:end_index]
	title
	
### Regex
Regex atau regular expression adalah sebuah cara untuk mencari teks berdasarkan pola tertentu. Ketika kita ingin mencari sebuah kata dalam kamus, misalnya arti dari kata parsing, kita akan mencari kata tersebut di halaman yang memiliki kata dengan awalan p, atau pa. Regex bekerja dengan konsep yang sama. Pada regex, kita mencari sebuah kata atau kumpulan kata dengan memberikan pola yang kita inginkan. Contoh umum regex adalah pada email di mana kita dapat menggunakan regex untuk mengecek apakah karakter @ ada pada email atau tidak

### argparse
contoh penggunaan

	$python panggildicoding.py -o

dalam file panggildicoding perlu dideklarasikan modul tersebut terlebih dahulu 

	import argparse

