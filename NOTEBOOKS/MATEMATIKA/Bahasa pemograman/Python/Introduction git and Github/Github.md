![ded72fefd6d840dfd9dcdebb2b01b6c3.png](../../../../../_resources/ded72fefd6d840dfd9dcdebb2b01b6c3.png)

![5547e39eb446742eff1c1a26f7678e2c.png](../../../../../_resources/5547e39eb446742eff1c1a26f7678e2c.png)

so.. the Github is A remote repository hosting service for Git

cloning github ke local
![21c2aa53093582afaf986ac9d69cb9ec.png](../../../../../_resources/21c2aa53093582afaf986ac9d69cb9ec.png)

kemudian di local ita mengolah dengan git
![a09c99b5fc243722ed50c5a54dc875fc.png](../../../../../_resources/a09c99b5fc243722ed50c5a54dc875fc.png)

kemudia jika ingin mengunggah ke cloud (github) gunakan git push (guakan git clone untuk membawanya ke local)

![7a9df88120663d709e952c79412e2ab4.png](../../../../../_resources/7a9df88120663d709e952c79412e2ab4.png)

maka di github akan ada pemberitahuan. 

	git pull 

adalah perintah untuk mengambili perubahan baru dari repositori (local). 
![cf60eb0e1ad6eb0ff9d0e317d785c921.png](../../../../../_resources/cf60eb0e1ad6eb0ff9d0e317d785c921.png)

beberapa remote repositori terkenal 
![729ed101398efda04d72bb15949321f7.png](../../../../../_resources/729ed101398efda04d72bb15949321f7.png)

git config --global credential.helper cache allows us to configure the credential helper, which is used for **Allowing automated login to GitHub**

jika ada perubahan besar di repositori, git akan meminta konfirmasi anda terlebih dahulu.


****
![c0589760f1cd628d6232ad91203c877a.png](../../../../../_resources/c0589760f1cd628d6232ad91203c877a.png)

kesalahan karena :
Git rejected our change, that's because the remote repository contains changes that we don't have in our local branch that Git can't fast-forward.

![c559c264dcd81c3595eb118c52a495bf.png](../../../../../_resources/c559c264dcd81c3595eb118c52a495bf.png)

itu karena ada branch yang tidak menyambung, ditunjukkan oleh grafik. 

The graph indicates that our current commit and the commit in the origin/master branch share a common ancestor, but they don't follow one another.
	
itu artinya kita harus melakukan algoritma tida jalan seperti yang telah dijelaskan pada chapter sebelumnya

This means that we'll need to do a three-way merge. To do this, let's look at the actual changes in that commit by running git log -p origin/master.

dan disini letak tubrukanya

![9b09e57d086b59810033abc55808b99a.png](../../../../../_resources/9b09e57d086b59810033abc55808b99a.png)

jika dibuka di text editor seperti ini
![2ed7a92965f69fff13a7a7f387b24986.png](../../../../../_resources/2ed7a92965f69fff13a7a7f387b24986.png)

setelah itu seperti langkah-langkah selanjutnya yaitu

git add < nama file >
git commit 
git push (kita ulangai lagi untuk upload ge server)

dan hasilnya seperti ini
![9fc49037d8289fd604e5fe22adb8ad50.png](../../../../../_resources/9fc49037d8289fd604e5fe22adb8ad50.png)


****
gunakan git checkout -b namabranch atau git checkout -brach namabranch 

untuk menuju ke direktori kerja branch

upload branch lokal ke branch server dengan 

	git push -u 
	
misalnya ini push brach refactoru dari lokal se server

![c8f3ac34522df859ff70ec8bd3b08cbe.png](../../../../../_resources/c8f3ac34522df859ff70ec8bd3b08cbe.png)

The command "git rebase refactor" will move the current branch on top of the refactor branch.

![4c8d7bd0c18a8b6a886e5a097222b4f6.png](../../../../../_resources/4c8d7bd0c18a8b6a886e5a097222b4f6.png)

perbedaan utama antara git rebase dan git merge adalah bagaimana Git menggabungkan perubahan dari branch sumber ke branch target dan bagaimana hal itu mempengaruhi sejarah commit. Git merge membuat commit merge baru, sementara Git rebase memindahkan commit dari satu branch ke branch target dan mengubah sejarah commit pada branch sumber.

seperti ini rebase workflownya

![410c549c8870109ea2d91d7149627135.png](../../../../../_resources/410c549c8870109ea2d91d7149627135.png)
![8a00bb8751d479300e1688756852da75.png](../../../../../_resources/8a00bb8751d479300e1688756852da75.png)
kemudian menjadi seperti ini
![a017610488bd1cf1831c99e1fd42adbc.png](../../../../../_resources/a017610488bd1cf1831c99e1fd42adbc.png)

karena
menjaga sejarah tetap linier membantu debugging terutama ketika kami mencoba mengidentifikasi commit mana yang pertama kali menimbulkan masalah dalam proyek kami. 

![20afce7c54620bf9b09392fb9f152adc.png](../../../../../_resources/20afce7c54620bf9b09392fb9f152adc.png)

***
![68e91f9df9d4daeb2ab1dde5533b91cb.png](../../../../../_resources/68e91f9df9d4daeb2ab1dde5533b91cb.png)


![121ac02396f5a4e734fa152008f6a485.png](../../../../../_resources/121ac02396f5a4e734fa152008f6a485.png)

It's better if you split it into different commit. This makes it easier to understand what's going on with each commit.

![2db7ea2a186beae9c6f43672608d0770.png](../../../../../_resources/2db7ea2a186beae9c6f43672608d0770.png)

![7f315618c100f74d162f68d52435dbe2.png](../../../../../_resources/7f315618c100f74d162f68d52435dbe2.png)

****

![b4442efa087003d34753a00e432a42f1.png](../../../../../_resources/b4442efa087003d34753a00e432a42f1.png)

![4660fe625ebe3bf2343bdc9947bd4bff.png](../../../../../_resources/4660fe625ebe3bf2343bdc9947bd4bff.png)

To change the base of the current branch, we can use the git rebase < branchname > command. In contrast, the git checkout < branchname > command is used to switch to a different branch


****

![5daa5d441a4772b7fdd9045d3eca3dc1.png](../../../../../_resources/5daa5d441a4772b7fdd9045d3eca3dc1.png)

jika anda sudah maka digithub ada id yang mempush nya
![2d077ebdbae4ae93f2b9c4428aaf1a54.png](../../../../../_resources/2d077ebdbae4ae93f2b9c4428aaf1a54.png)
pojok kiri atas	

alurnya kek gini
masuk ke git

buat token (atau kalao dulu pake username dan password) tetapi sekarang password diganti dengan token yang digenerate dari github untuk masalah keamanan. 

git add
git commit -m 'tambahkan catatan'

***ketika di githun ditambahkan suatu file diaman di lokal tidak ada, maka itu akan error. harusnya kondisi di github dan di lokal adalah sama ketika anda memberikan kode***

	git push origin main

maka kita perlu tarik dulu yang dari server ke local

	git pull origin main

kemudian baru kita push lagi

	git push origin main

