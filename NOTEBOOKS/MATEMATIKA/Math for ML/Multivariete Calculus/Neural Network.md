Neural Newtork menunjukkan bagaimana pentingnya multivariate. ia bisa digunakan untuk image recognition. Neural Network sebenarnya adalah fungsi matematika yang mengambil suatu variabel dan mengambelikan suatu variabel. kedua variabel tersebut adalah suatu vektor. 
![626f988de1340e80fc8ab01c4dcfc7bf.png](../../../../_resources/626f988de1340e80fc8ab01c4dcfc7bf.png)

## Neural simpel
dibawha ini satu network dijelaskan
![9fd4e5a97970f7ef5c2a8c7e9b94c3b3.png](../../../../_resources/9fd4e5a97970f7ef5c2a8c7e9b94c3b3.png)
dimana w dan b adalah suatu konstanta dan sigma adalah fungsi. 
![db42f9568f848e96ab564048e0a726c9.png](../../../../_resources/db42f9568f848e96ab564048e0a726c9.png)

> Sigma that gives neural networks theri association to the brain.

neuron dalam otak menerima informasi dari senyawa tetangga dan simulasi elektrika. dan ketika total dari simulasi melampaui ambang batas tertentu, neuron akhirnya teraktivasi untuk mensimulasi neuron lainya

ketika neuron bertambah, mereka saling dihubungkan dengan weight (w)
![fb50fc597134eef4ca3716aa60047e5e.png](../../../../_resources/fb50fc597134eef4ca3716aa60047e5e.png)
![7a054aa936220b1522949a23bfb97586.png](../../../../_resources/7a054aa936220b1522949a23bfb97586.png)
jika disederhanakan rumusnya menjadi seperti ini
![9e52f2b9dc825220a925a5a32b7398b7.png](../../../../_resources/9e52f2b9dc825220a925a5a32b7398b7.png)

![6c3b3dfea463f53a32900eeb72bf8fec.png](../../../../_resources/6c3b3dfea463f53a32900eeb72bf8fec.png)

sepertin dibawah ini tampak bagaimana vektor disimpan dalam matrik
![7a5382d7d49a980c53fc6fba3c831849.png](../../../../_resources/7a5382d7d49a980c53fc6fba3c831849.png)

### satu layer
![351368f7027747e7f3111c4c404c2556.png](../../../../_resources/351368f7027747e7f3111c4c404c2556.png)
### dua layer
![19a60348ee51ee50759e0d8525c63bc0.png](../../../../_resources/19a60348ee51ee50759e0d8525c63bc0.png)

***
![357ceef769116e7d7112cae204b91e1e.png](../../../../_resources/357ceef769116e7d7112cae204b91e1e.png)

aktivasi neuron pada layer final ditentukan oleh aktivasi dari neuron sebelumnya. 
![7df231ef8deef4dac19e265f5903fc76.png](../../../../_resources/7df231ef8deef4dac19e265f5903fc76.png)
dimana w(1) adalah weight dari koneksi antar neuron, dan b(1) adalah bias dari neuron (1). kemudian mereka diberikan fungsi aktivasi, sigma, yang memberikan aktivasi kepada neuron (1). Our small neural network won't be able to do a lot - it's far too simple

Let's assume we want to train the network to give a NOT function, that is if you input 1 it returns 0, and if you input 0 it returns 1.

![fcff2042e6945b4f5c3a0aaa09e5ea5a.png](../../../../_resources/fcff2042e6945b4f5c3a0aaa09e5ea5a.png)
![20c6df58c68d59f3d29a20a3d1d1ac9d.png](../../../../_resources/20c6df58c68d59f3d29a20a3d1d1ac9d.png)
hasilnya adalah : 0.833654607012 dan -0.885351648202 untuk input -1. (ini salah ya bukan NOT Function, tapi intinya seperti itu)

Mari kita tambah jaringan syarafnya
![bbddf93d2ecf5f86c45ed56df0d9b717.png](../../../../_resources/bbddf93d2ecf5f86c45ed56df0d9b717.png)
![b0e323d78de90c8ca01f75fcc375ed7b.png](../../../../_resources/b0e323d78de90c8ca01f75fcc375ed7b.png)

sehingga fungsi untuk beberapa neuron menjadi sepertin ini ![ce23cc02ba4458e60aae32fcf7b79036.png](../../../../_resources/ce23cc02ba4458e60aae32fcf7b79036.png)

nilai-nilai input dapat ditampung dalam matrik seperti dibawah ini
![329447c389c0ea6e412335be0b56258a.png](../../../../_resources/329447c389c0ea6e412335be0b56258a.png)

***
![a35b9f81fc081e345907431e3c409692.png](../../../../_resources/a35b9f81fc081e345907431e3c409692.png)
![026830379336db503a660a24625cca77.png](../../../../_resources/026830379336db503a660a24625cca77.png)
rumusnya sepertin in ![2f4bcac8f35cb5d8163a2d463b9e391c.png](../../../../_resources/2f4bcac8f35cb5d8163a2d463b9e391c.png)

instrument neural network
![7ed2698792d25fbd804ce23d2b383261.png](../../../../_resources/7ed2698792d25fbd804ce23d2b383261.png)