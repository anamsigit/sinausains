![e07e2a3f4ee4389425658eaf8370aa0d.png](../../../../../_resources/e07e2a3f4ee4389425658eaf8370aa0d.png)

CPU diambil bagianya oleh beberapa proses. So if the problem is that your program needs more CPU time, you can close other running programs that you don't need right then. If the problem is that you don't have enough space on disk, you can uninstall applications that you don't use, or delete or move data that doesn't need to be on that disk and so on. 

salah satu tool untuk menujukkan kinerja hardware adalah top

![3c729d4ee86da7863720cc22cc40d62e.png](../../../../../_resources/3c729d4ee86da7863720cc22cc40d62e.png)

disitu ditampilkan PID, itu bisa untuk menghentikan dari terminal yang berbeda dengna menunjukkan PID terkait. 	

![0fcf088dfc9bea08dd0c294b220b528b.png](../../../../../_resources/0fcf088dfc9bea08dd0c294b220b528b.png)

 ***
 bagaimana komputer menggunakan sumber daya
 ![f98cbd23191ecb48ef8d0d65b0658869.png](../../../../../_resources/f98cbd23191ecb48ef8d0d65b0658869.png)
 
 dalam ram, aplikasi akan cepat karena
 ![ed3459fc4801fd6bb8faad8041bacec3.png](../../../../../_resources/ed3459fc4801fd6bb8faad8041bacec3.png)
 
 dalam disk lebih lambat daripada ram
 ![4fa1bf0cd56c68cdb5ae0b392a85fe19.png](../../../../../_resources/4fa1bf0cd56c68cdb5ae0b392a85fe19.png)
 
 apalagi dalam network 
 ![6a1db90b20bb9dbb56d4e8e82f434ae8.png](../../../../../_resources/6a1db90b20bb9dbb56d4e8e82f434ae8.png)
 
 ![523ca3a97e4515969c67ff739aef48bb.png](../../../../../_resources/523ca3a97e4515969c67ff739aef48bb.png)
 
 komputer yang lambat juga dapat diakibatkan karena ada software software rusak. atau karena malware juga bisa. 
 
 *** 
 mengecek website apakah berfungsi dengan seharusnya atau tidak dapat mengetikkan perintah berikut di terminal. 
 
 ![8c0ca5b94d978c16ce9cb46b0cd3f500.png](../../../../../_resources/8c0ca5b94d978c16ce9cb46b0cd3f500.png)
 
 ![679e9f8c14daf37db2ce838e659e01be.png](../../../../../_resources/679e9f8c14daf37db2ce838e659e01be.png)
 
 diatas adalah merubah prioritas, ffmept memakan resource banyak, maka kita otak atik dengan perintah pidof
 
 prioritas dalam linux direpresentasikan dari angka 0 ke angka 19. tetapi kita bisa mengubahnya untuk suatu proses tertentu yang kita inginkan. 
 
 ffmeg sudah tidak menjadi prioritas lagi. 
 
 gunakan perintah berikut
 ![06a1acfc1b53ef2db32cbe8dc403b3ea.png](../../../../../_resources/06a1acfc1b53ef2db32cbe8dc403b3ea.png)
 pipeline less digunakan agar bisa di scrolldown
 
 kemudian pilih /ffmeg
 
 kasus diatas adalah ketika linuxmu menghosting website, dan website itu pelan, maka anda mencoba untuk memprioritaskan hosting linux.
 
 sepertinya tepatnya adalah mengalokasikan memori ffmeg. 