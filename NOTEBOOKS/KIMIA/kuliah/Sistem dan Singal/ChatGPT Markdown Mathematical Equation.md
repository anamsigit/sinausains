ganti garing (tertentu) dengan $
\(f(x)\) menjadi
 $(f(x)$) ini juga perlu dipecahkan
 $(f(x)$$)$ 

Rumus umum untuk representasi deret Fourier dari suatu fungsi periodik \(f(x)\) adalah sebagai berikut:

$$ [f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos \left(\frac{2\pi n x}{T}\right) + b_n \sin \left(\frac{2\pi n x}{T}\right) \right]\] $$

Di sini:

- $(f(x)$) adalah fungsi periodik yang ingin diuraikan menjadi deret Fourier.
- $(a_0$) adalah koefisien konstan (bias) dan dapat dihitung dengan rumus:

  $[a_0 = \frac{1}{T} \int_{-T/2}^{T/2} f(x) , dx$]

  Di mana \(T\) adalah periode dari fungsi \(f(x)\).

- $(a_n$) dan $(b_n$) adalah koefisien harmonik yang dapat dihitung dengan rumus berikut:

  \[a_n = \frac{2}{T} \int_{-T/2}^{T/2} f(x) \cos \left(\frac{2\pi n x}{T}\right) \, dx\]

  \[b_n = \frac{2}{T} \int_{-T/2}^{T/2} f(x) \sin \left(\frac{2\pi n x}{T}\right) \, dx\]

Rumus di atas menguraikan fungsi periodik \(f(x)\) menjadi jumlah dari deret Fourier yang terdiri dari komponen-komponen harmonik dengan frekuensi-frekuensi \(n/T\), di mana \(n\) adalah bilangan bulat positif.

Penting untuk dicatat bahwa deret Fourier ini adalah representasi tak hingga, dan dalam prakteknya, kita sering menggunakan jumlah terbatas dari suku-suku (atau jumlah hingga) untuk mendekati fungsi asli dengan tingkat akurasi tertentu. Jumlah hingga dari suku-suku deret Fourier ini disebut "truncated Fourier series."