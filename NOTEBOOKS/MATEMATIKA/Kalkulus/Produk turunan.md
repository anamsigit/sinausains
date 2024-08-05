# Chain of Rule
$$ \frac{dy}{dx} = a\frac{da}{dx} + b\frac{db}{dx} + c\frac{dc}{dx} + d\frac{dd}{dx} + e\frac{de}{dx} + ...\frac{d...}{dx} + ... $$

turunan y terhadap x pada sebuah persamaan fungsi sebenarnya berlandaskan 

$$ a  = x^3 $$
$$ a' = 3x^{3-1} $$
$$ a' = 3x^{2} $$

misalnya

$$ y = x^3(4-x)^\frac{1}{2} $$
maka turunan y terhadap x adalah  
$$ \frac{dy}{dx} = a\frac{da}{dx} + b\frac{db}{dx} $$ 
dimana 
$$ a = x^2 $$
dan 
$$ b = (4 - x)^\frac{1}{2} $$

sehingga untuk turunan a terhadap x
$$ \frac{da}{dx} = \frac{d(x^2)}{dx}$$
$$ \frac{da}{dx} = 2x$$

sehingga untuk turunan b terhadap x
$$ \frac{db}{dx} = \frac{d((4 - x)^\frac{1}{2})}{dx}$$
$$ \frac{db}{dx} = \frac{1}{2}(4-x)^{-\frac{1}{2}}$$

maka kembali pada *chain rule*
$$ \frac{dy}{dx} = a\frac{da}{dx} + b\frac{db}{dx} $$
substitusi mendapatkan

$$ \frac{dy}{dx} = x^32x + (4 - x)^\frac{1}{2}\frac{1}{2}(4-x)^{-\frac{1}{2}} $$

> aturan tersebut adalah sumber dari hafalan dibawah, mengapa sekolah tidak mengajarkan ini sehingga tidak perlu menghafal rumus, hanya mengandalkan kemampuan aljabar

> yang mendapat turunan adalah yang mendandung apa yang diturunkan, misalnya turunan y terhadap x (dy/dx), maka semua variabel x pada persamaan y akan diturunkan, dengan catatan dipisahkan oleh kali (x) atau bagi (/)

### Turunan fungsi pangkat
$$ f(x)  = x^3 $$
$$ f'(x) = 3x^{3-1} $$
### Turunan fungsi perkalian
$$ f(x) = x^2 \cdot z^3 $$
> $$ f'(x) = u'v + vu' $$
$$ f'(x) = 2xz^3 + 3z^2x^2 $$
### Turunan fungsi pembagian
> $$ f'(x) = \frac{u'x - vx'}{v^2} $$
### Turunan fungsi pangkat
$$ f(x) = [u(x)]^n $$
> $$ f'(x) = nu^{n-1}u' $$

misalnya  
$$ y = (2 + 5x^2)^5 $$
$$ y' = 5 \cdot 10  (2 + 5x^2)^{5-1} $$