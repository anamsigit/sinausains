![324f436613a3b7aed5aa1792d2627e34.png](../../../../../_resources/324f436613a3b7aed5aa1792d2627e34.png)

itu ada try-except nya lur
If there's an error, it then goes into the accept part of the block that matches the error and does whatever cleanup is necessary. Here we have only one except block, for the OSError error type, but there could be more blocks if the functions called could raise other types of errors. So when writing a try-except block, the important thing to remember is that the code in the except block is only executed if one of the instructions in the try block raise an error of the matching type.

bahasa indonesianya, itu jika masuk kedalam blok except, adalah jika kesalahanya adalah sama seperti yang dikondisikan (OSError) dan dari blok itu bisa melakukan pembersihan. itu dasanya kemarin itu sepertinya echo $?

![fee51946f9d424786fbc9da629f94542.png](../../../../../_resources/fee51946f9d424786fbc9da629f94542.png)

********
![009ca44ddcb3dea5e4e589eb56fdf2e1.png](../../../../../_resources/009ca44ddcb3dea5e4e589eb56fdf2e1.png)

dititik beratkan pada fungsi ValueError()
jika dijalankan seperti ini
![4cf4d752b7dd23577344654156e71835.png](../../../../../_resources/4cf4d752b7dd23577344654156e71835.png)

jika di inputkan dengan value yang benar

![74684337be584c97e1328245f383984f.png](../../../../../_resources/74684337be584c97e1328245f383984f.png)

dan dibawah ini jika kita tidak mngatur ValueError

![8eadaefea9fa8ae727d9265807517e93.png](../../../../../_resources/8eadaefea9fa8ae727d9265807517e93.png)

kemudian dibawah ini menunjukkan bahwa [] berpengaruh 
![386d0cbb744cb0e77af406701432edf6.png](../../../../../_resources/386d0cbb744cb0e77af406701432edf6.png)

### assert
let's look at an alternative to the raise keyword that we can use for situations where we want to check that our code behaves the way it should particularly when we want to avoid situations that should never happen. This is the assert keyword. This keyword tries to verify that a conditional expression is true, and if it's false it raises an assertion error with the indicated message. seperti ini penggunaanya

![383d7d3257229adbc39e6b6c03c6e7e2.png](../../../../../_resources/383d7d3257229adbc39e6b6c03c6e7e2.png)

the result

![e070e86f90301a7141e5fbe234afdb59.png](../../../../../_resources/e070e86f90301a7141e5fbe234afdb59.png)

kesimpulan:

![2801f37a5aae60338261ec50658cf450.png](../../../../../_resources/2801f37a5aae60338261ec50658cf450.png)

**************
![0feede830fb1b6427579818974ba5aac.png](../../../../../_resources/0feede830fb1b6427579818974ba5aac.png)

![0c6b018c6f5a8826ed7e9694fd55a1a4.png](../../../../../_resources/0c6b018c6f5a8826ed7e9694fd55a1a4.png)

so 

![f79e85de9544f3a5f72149e25ceebaae.png](../../../../../_resources/f79e85de9544f3a5f72149e25ceebaae.png)

## practical

![518213943384f37f01d9468f896b6db3.png](../../../../../_resources/518213943384f37f01d9468f896b6db3.png)

itu adalah salah satu contoh yang mengatakan, error tidak menunjukkan yang seharusnya. buka di 0_IntroPython untuk praktik notebook yang sama (saya sudah mendownload)

dan seperti ini seharusnya pembenaranya

![1922c98d521cae3fc8678ba516c619a7.png](../../../../../_resources/1922c98d521cae3fc8678ba516c619a7.png)

aplikasinya untuk index out of range
![3e51bde44fa4100ae4ec1e28a05b6edc.png](../../../../../_resources/3e51bde44fa4100ae4ec1e28a05b6edc.png)

anda bisa mengolah sedemikian rupa sehingga output dari sebuah error adalah pesan yang bisa dibaca orang awam

![883f2bde734359c1315ecbbad6327ab1.png](../../../../../_resources/883f2bde734359c1315ecbbad6327ab1.png)

