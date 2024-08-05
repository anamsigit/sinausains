![2af9343a7aeb1986dbf1b6a51091b6e0.png](../../../../../_resources/2af9343a7aeb1986dbf1b6a51091b6e0.png)

## Pull request
![b86f11c526324bad5d7929d022453fcf.png](../../../../../_resources/b86f11c526324bad5d7929d022453fcf.png)

We've created a commit on our forked repo. But we haven't yet created the pull request that will send the changes to the owner of the original repo

Pull request adalah sebuah fitur yang tersedia di GitHub yang memungkinkan seorang pengguna (biasanya  kontributor) untuk mengajukan perubahan kode ke sebuah proyek open-source yang dihosting di GitHub. Prosesnya dimulai dengan melakukan fork (menyalin) repositori proyek ke akun GitHub milik kontributor, lalu membuat branch baru untuk membuat perubahan pada kode, kemudian mengajukan pull request untuk meminta pemilik proyek menggabungkan perubahan yang dibuat.

ini adalah bagaiman membuat file readme, membuat brach dan push to server
![04b03711c4cc7fbb170327c257a7c67d.png](../../../../../_resources/04b03711c4cc7fbb170327c257a7c67d.png)

dan bisa dilihat di github
![dfcc3b4c5cceb4f2dc5d6602976abc6f.png](../../../../../_resources/dfcc3b4c5cceb4f2dc5d6602976abc6f.png)

setelah itu bisa di pull request kepada si owner untuk dipertimbangkan. mungkin bisa terjadi percakapan sepertin ini
![7afedfcb9c1703a0d2ee70885c0ac38c.png](../../../../../_resources/7afedfcb9c1703a0d2ee70885c0ac38c.png)

maka jika ingin mengubah, edit di lokal. kemudian git commit. kemudian git push. 

***
Git Rebase dapat digunakan untuk mengubah komentar pada commit sebelumnya. dilakukan dengan memanfaatkan opsi "-i" atau "--interactive"

	git rebase -i

![b6dc14775b637f33946f3c754622f0c5.png](../../../../../_resources/b6dc14775b637f33946f3c754622f0c5.png)

diatas adalah ada dua file yang berbeda jalur, ketika di push akan menimbulkan masalah, tetapi kita bisa memaksanya menjadi git push -f. but it will possibly resulting in permanent data loss

![8a6668ea24b5652fe485f4caa5fb741e.png](../../../../../_resources/8a6668ea24b5652fe485f4caa5fb741e.png)

![e7cb96c6859b448ab3218b799e3fb085.png](../../../../../_resources/e7cb96c6859b448ab3218b799e3fb085.png)

![73893a04f7b3f92fc5fb7c37e885805a.png](../../../../../_resources/73893a04f7b3f92fc5fb7c37e885805a.png)

 On top of this, if the person contributing the changes of volunteer that's just trying to help, they may lose their motivation to work on the project if you make them wait too long for feedback. 
 
 You should also be careful with which patches you accept or reject
 
 ***
 A tool like an issue tracker or bug tracker can help us coordinate our work better. An issue tracker tells us the tasks that need to be done, the state they're in and who's working on them.
 
 ![dbe4aa52255ff582bb9c59542b492641.png](../../../../../_resources/dbe4aa52255ff582bb9c59542b492641.png)
 
 >We can reference issues in our commits with automatic links by using one of the keywords followed by a hashtag (#) and the issue number

What is an artifact in terms of continuous integration/continuous delivery (CI/CD) pipelines?
answer : Any file generated as part of the CI/CD pipeline.

Continuous Integration system is similar with Run tests automatically


*** 

append a line: "Closes: #1" at the beginning to indicate that you're closing the issue. Adding this keyword has an additional effect when using Github to manage your repos, which will automatically close the issue for you (for more information, please see the documentation here).

ini fork repositoriesmu, kamu pull reques ke ownernya dengan mengajukan branch anda
![16a9a967eeb4b449d86098eea87aeff9.png](../../../../../_resources/16a9a967eeb4b449d86098eea87aeff9.png)

branchnya yaitu namanya improve-username-behavior

![bddb724432fead50281169b06bd84537.png](../../../../../_resources/bddb724432fead50281169b06bd84537.png)


![b15338a17c8393b071d13d1497d2fcc2.png](../../../../../_resources/b15338a17c8393b071d13d1497d2fcc2.png)

![7be264f7f4c8b419cec18598e131f30a.png](../../../../../_resources/7be264f7f4c8b419cec18598e131f30a.png)