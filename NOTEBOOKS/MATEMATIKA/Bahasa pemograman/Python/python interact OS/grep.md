Grep stands for "Global Regular Expression Print", it is a command-line regex tool.

grep akan memunculkan semua tulisan yang mendandung angka yang dimaksud
![5fd054ea2cc40039e896c53bf33ce662.png](../../../../../_resources/5fd054ea2cc40039e896c53bf33ce662.png)

![138509ad61114aee1c74058147328a28.png](../../../../../_resources/138509ad61114aee1c74058147328a28.png)

dot akan merepresentasikan karakter apapun seperti dibawah ini
![eed5124dd87a4863f75188e68e49b4ac.png](../../../../../_resources/eed5124dd87a4863f75188e68e49b4ac.png)

 circumflex [^] : matching pada awal kalimat
 dollar sign [$] : matching pada akhir kalimat
 
 The characters such as dollar sign ($), circumflex (^), and dot (.) are collectively known as "Special characters" or "Metacharacters" in regex
 
 ## mathcing
 ![e0cf1ff4a4ab79940dd2932650a617da.png](../../../../../_resources/e0cf1ff4a4ab79940dd2932650a617da.png)
 
 mencocokkan satu karakter saja
 ![d25fc1ea008e9d833448b5a12925e5cd.png](../../../../../_resources/d25fc1ea008e9d833448b5a12925e5cd.png)
 
 menggabungkan regex dengan mathcing
 ![44ed365ded40d1f003e980f3c2c6d4df.png](../../../../../_resources/44ed365ded40d1f003e980f3c2c6d4df.png)
 
 ![78da9d73abdfcbf58efeb837c7f8fc06.png](../../../../../_resources/78da9d73abdfcbf58efeb837c7f8fc06.png)
 r"a.e.i" ini akan mengecek apakah huruf vokal berada di antara huruf tidak vokal
 
 berikan .IGNORECASE untuk mengabaikan besar kecil huruf
 ![8ebcb6d1bc30b133592f387f21e9f341.png](../../../../../_resources/8ebcb6d1bc30b133592f387f21e9f341.png)
 
 dot '.' can match any character, it is called wildcard because it can match more than one character
 
 ##### character class
 character class ditulis dalam bracket and let us list the character we want match inside of those bracket seperti ini
 ![3b81bc4b8ab3dc1e54f0b8c7cf84c837.png](../../../../../_resources/3b81bc4b8ab3dc1e54f0b8c7cf84c837.png)
 [x]way dimana x bisa berupa a-z
 tetapi itu tidak bisa mendektesi spasi
 ![282f462e775d7ac6c58810e4fc394515.png](../../../../../_resources/282f462e775d7ac6c58810e4fc394515.png)
 
 ![f449deb11eeb8e58ffe84efcbb1a5bbd.png](../../../../../_resources/f449deb11eeb8e58ffe84efcbb1a5bbd.png)
 diatas adalah untuk mengecek apakah suatu kalimat mengandung , . : ; ? atau !
 
 ![0ac9e54ea4f9c9d95a7c171206afac2e.png](../../../../../_resources/0ac9e54ea4f9c9d95a7c171206afac2e.png)
 
 untuk mencari cat atau dog
 ![e09bbdccdbbe39efd76121b3b4094b53.png](../../../../../_resources/e09bbdccdbbe39efd76121b3b4094b53.png)
 
 mencari akhiran yaitu dengan *x dimana x adalah karakter yang diinginkan, ini termasuk spasi juga akan diambil atau karakter apapun
 ![b8b8759db27e2556c12b969e111d5aa7.png](../../../../../_resources/b8b8759db27e2556c12b969e111d5aa7.png)
 
 tetapi jika anda ingin spesifik saja tambahkan bracket dan diisi apa yang diinginkan
 ![527a5256e8db578c7b4545b166694010.png](../../../../../_resources/527a5256e8db578c7b4545b166694010.png)
 
 (saya menyimak di coursera tidak sampai selesai)
 
 for more: www.regex101.com
 
 # Study case
 mengganti domain
 def contains_domain(address, domain):
  domain_pattern = r'[\w\.-]+@'+domain+'$'
  if re.match(domain_pattern, address):
    return True
  return False
  
  for tutorial : [*](https://googlecoursera.qwiklabs.com/focuses/26908998?parent=lti_session)