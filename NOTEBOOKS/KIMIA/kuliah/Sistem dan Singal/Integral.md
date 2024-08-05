integral masuk kedalam rumpun kalkulus. disebut juga dengan antiturunan. 

Kalau ada sebuah fungsi f(x) diturunkan, maka menjadi f’(x). Nah, integral kan kebalikannya turunan, jadi f’(x) dibalik lagi. Maka, hasilnya balik menjadi f(x).

![97dcadc8be22143b6981a0e775d01cee.png](../../../../_resources/97dcadc8be22143b6981a0e775d01cee.png)
![775e06f34c59ee5e9e994cf9bd3f453a.png](../../../../_resources/775e06f34c59ee5e9e994cf9bd3f453a.png)

## Integral Tentu
Integral tentu adalah integral yang udah punya nilai awal dan akhir, punya batas yang jelas.
![1baf8247fc28047e67da0bfb102e4d54.png](../../../../_resources/1baf8247fc28047e67da0bfb102e4d54.png)

## Integral Tak Tentu
integral tak tentu nggak punya batas dan belum punya nilai yang jelas. Nilai yang nggak jelas ini dilambangkan dengan konstanta ( C ). Sedangkan, lambang integral tak tentu nggak punya batas atas dan batas bawah, karena nggak terbatas.

![9e9560a12971c0f31fa66576dac8a788.png](../../../../_resources/9e9560a12971c0f31fa66576dac8a788.png)

***
Hitung integral tentu dari fungsi $(f(x) = 2x^2 + 3x - 5$) dari $(x = 1$) hingga $(x = 4$). **Jawabanya adalah** $(\frac{269}{6}$).

menggunakan python: 
## SciPy
	from scipy import integrate
	def f(x):
    	return 2*x**2 + 3*x - 5
	x = [1, 4] #batas bawah ke batas atas
	result, _ = integrate.quad(f,x[0] , x[1])
	


