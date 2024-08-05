jadi untuk mengukur parameter w dan b dari nilai yang telah anda tentukan anda dapat menggunakan cost function. 
![1ec4de4775779443a000fe9a60a9612f.png](../../../../_resources/1ec4de4775779443a000fe9a60a9612f.png)
the goal is make J be as small as possible. 

misalkan input adalah 0
![a9f4b65756ecbb313ed027a6fe004530.png](../../../../_resources/a9f4b65756ecbb313ed027a6fe004530.png)
maka garis exacly bergabung dengan sumbu x. dan mari kita hitung cost function dengan input 0. J(0) dihitung seperti diatas dan didapatkan nilinya 2.3. begitu pula jika kasusnya garis agak keatas yaitu dengan input w = 0.5
![636ccf604086d434a9c33c10f1cec7ba.png](../../../../_resources/636ccf604086d434a9c33c10f1cec7ba.png)

> w akan memengaruhi kemiringan (slope) sedangkan b akan mengangkat garis kearah bawah atau atas. 

![1c6379f09261231e04b7d59ba8d74b85.png](../../../../_resources/1c6379f09261231e04b7d59ba8d74b85.png)

# Visualisasi cost function
![01320afd8268500282d0dc0c09fa9a59.png](../../../../_resources/01320afd8268500282d0dc0c09fa9a59.png)
contoh lainya. 
![29e9386c781f3cb729db49d848abac42.png](../../../../_resources/29e9386c781f3cb729db49d848abac42.png)
ketika anda menarik dari node data (merah silang) ke garis gradian untuk grafik kiri, itu sama saja anda menarik titik yang dibuat oleh angka -0.15 dan 800 di grafik kanan, titik itu kemudian ditarik garis ke pusat lingkaran (minimum). contoh lainya yang memiliki fits lebih baik. 
![17dd4d8849c191ff2f1e6fcea30eae54.png](../../../../_resources/17dd4d8849c191ff2f1e6fcea30eae54.png). hampir!
![384b9db471093a3b4d82b24ce22c0f37.png](../../../../_resources/384b9db471093a3b4d82b24ce22c0f37.png)

**algorithm to automatiaclly finding the values of parameter w and b they give uou the best fit line that minimizes the cost function J, Algoritma itu dinamakan Gradien Descent. Algoritma ini adalah algoritma sangat penting dalam machine learning. Gradient DEscent dan variations tidak hanya digunakan dalam regresi linear, tetapi tetapi banyak digunakan dalma model machine learning yang komplek**