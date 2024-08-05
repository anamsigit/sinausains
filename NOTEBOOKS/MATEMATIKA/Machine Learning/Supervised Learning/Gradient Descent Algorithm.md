alfa disebut dengan learning rate
![1c838d0689eb31a2074110ec9dc38b6a.png](../../../../_resources/1c838d0689eb31a2074110ec9dc38b6a.png)
learning rate bernilai antara 0 sampai dengan 1. yang dilakukan alfa adalah how big step you take downhill. ketika alfa rate anda cenderung besar, maka gradient descent cenderung agresive. 

sedangkan dibawah ini adalah turunan
![9c6727c0c3da14025567eb0ca4d46a83.png](../../../../_resources/9c6727c0c3da14025567eb0ca4d46a83.png)

dua parameter dalam model adalah w dan b, yang akan diubah dari w dan b lama menjadi w dan b baru sampai dengan konvergen (getting bottom surface). 
![a55767edcedf01b6dda866bbb742d4d1.png](../../../../_resources/a55767edcedf01b6dda866bbb742d4d1.png)

seperti PID yang kau pelajari selama KKCTBN ASSD, dimana nilai lama dimasukkan kedalam nilai baru. 
![ec04fa5ba3e05617e51cf259a004469c.png](../../../../_resources/ec04fa5ba3e05617e51cf259a004469c.png)
***
diatas menggunkaan multivariete calculus right, and maybe it is partial differential, cause ada dua yaitu turunan terhadap w dengan b konstan, dan turunan terhadap b dengan w konstan, sehingga terdapat dua perasaman right. dalam intuisi saya ... nilai w akan dikurangi dengan turunanya. sehingga dia akan terus menerus mencapai curam surface (local minima), jadi jika sebaliknya, anda ingin naik ke surface (local maksimum) anda ubah tanda negatif alfa menjadi positif alfa, saya kira. kemudian alfanya sendiri sudah keliatan akan meingkatkan agresivitas dari turunan dengan mengalikanya that right. 

***
the exactly
![fd050e5f684e3be816851d8b009dfeba.png](../../../../_resources/fd050e5f684e3be816851d8b009dfeba.png)
so it will decresed, dan berlaku jika nilai turunan bernilai negatif
![04d7fa7178b805ec8706d29554eb1ad6.png](../../../../_resources/04d7fa7178b805ec8706d29554eb1ad6.png)

# Learning rate
jika nilai alfa (learning rate) terlalu kecil, bisa saja ia sampai pada local miminum tetapi memerlukan langkah yang banyak. jika nilai alfa terlalu bear, bisa saja ia mengalami overshoot sehingga bisa jadi tidak pernah mencapai localm miminum. 

![2e3b1f0a42cb1c4949c044ba67f3d0ea.png](../../../../_resources/2e3b1f0a42cb1c4949c044ba67f3d0ea.png)
gambar diatas memberikan alasan bahwa ketika titik sudah mencapai local minimum ia akan berhenti, hal itu disebabkan ketika titik berada pada local mimum maka ia berada pada keadaan stasioner, dimana turunan pada fungsi tersebut menghasilkan angka nol. oleh karena menghasilkan angka nol maka `w = w - a.0` mengakibatkan w baru dan w lama akan benilai 0 terus. 	

learning rate yang baik adalah ketika masih jauh dengan local mimum ia bernilai besarm tetapi kalau sudah dekat, automatically menurun. 