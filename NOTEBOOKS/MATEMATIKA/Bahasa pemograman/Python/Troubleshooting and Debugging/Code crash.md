![565f0d07abf6175740a2129c031163ec.png](../../../../../_resources/565f0d07abf6175740a2129c031163ec.png)

![fabba66096eaeefea2a5d63823d2e605.png](../../../../../_resources/fabba66096eaeefea2a5d63823d2e605.png)

![b46e3699c94ab055ad0153f54628b56d.png](../../../../../_resources/b46e3699c94ab055ad0153f54628b56d.png)

When this happens, the OS will raise an error like segmentation fault or general protection fault. What kind of programming error is this? It typically happens with low-level languages like C or C++ where the programmer needs to take care of requesting the memory that the program is going to use and then giving that memory back once it's not needed anymore

Common programming errors that lead to segmentation faults or segfaults include forgetting to initialize a variable, trying to access a list element outside of the valid range, trying to use a portion of memory after having given it back, and trying to write more data than the requested portion of memory can hold

One of the trickiest things about this invalid memory business is that we're usually dealing with undefined behavior. This means that the code is doing something that's not valid in the programming language.

![c5324c3af5c128e7b0c3cc7573128d26.png](../../../../../_resources/c5324c3af5c128e7b0c3cc7573128d26.png)

![806aaf0ed8ccbc7ff23ab39a41f75a9b.png](../../../../../_resources/806aaf0ed8ccbc7ff23ab39a41f75a9b.png)

Valgrind is available on Linux and Mac OS, and Dr. Memory is a similar tool that can be used on both Windows and Linux	

***
Correctly handling memory is a hard problem, and that's why there's a bunch of different programming languages like Python, Java, or Ruby that do it for us. But that doesn't mean programs written in these languages can't trigger weird problems.

![876061508382f49f7726bfbb6cb8fa15.png](../../../../../_resources/876061508382f49f7726bfbb6cb8fa15.png)

For a Python, program we can use the **BDB interactive debugger** which lets us do all the typical debugging actions like executing lines of code one-by-one or looking at how the variables change values. When we're trying to understand what's up with a misbehaving function on top of using debuggers, it's common practice to add statements that print data related to the codes execution.

 how do you even start reading through someone else's code? This depends a bit on personal preference and the size of the project. If there are only a couple of 100 lines of code, it's feasible to read all of them. But when the project has thousands or tens of thousands of lines of code, you can't really read the whole thing. You'll need to focus on the functions or modules that are part of the problem that you're trying to fix
 
 ***
 a simple example program that crashes with a seg fault.
 
 ![77734d85afac303775a7ba0f41d39bfb.png](../../../../../_resources/77734d85afac303775a7ba0f41d39bfb.png)
 
 ![7cce93411c846055d5e6783ff7ba6fec.png](../../../../../_resources/7cce93411c846055d5e6783ff7ba6fec.png)
 
 GDB shows a bunch of messages including its version, license, and how to get help. It then tells us that the program finished with a segmentation fault. It shows that the crash happened inside the strlen function in a file that's part of the system libraries
 
![9742cad3720d4be339f89f868de05f30.png](../../../../../_resources/9742cad3720d4be339f89f868de05f30.png)

### GDB Tools
The gdb command will debug a core dump and stop where the failure was recorded.

What are those weird numbers starting with 0x? Those are hexadecimal numbers, and they are used to show addresses in memory where some data is stored.

***

kind of problem is common when dealing with applications written in languages like C or C++. On the flip side, when using languages like Python, we usually need to deal with unexpected exceptions making our program crash

traceback
![d11e65a5f7df9c23ca5b6a1f413f63da.png](../../../../../_resources/d11e65a5f7df9c23ca5b6a1f413f63da.png)

At the bottom, we see the name of the exception. In this case, Key Error and the message in this case, product code, which is the name of the key that's failing. 

Above that, we see a list of function calls with two lines per function. The first line tells us the Python file that contains the function, the line number, and the name of the function. 

The second line shows us the contents of that line. This information is similar to the back-trace that we saw in our last video. But the order of the functions is reversed. The function at the bottom, update data, is the one where the exception occurred

### pdb3
pdb untuk python 
![74af50a612f2a63983de26f4270bcf33.png](../../../../../_resources/74af50a612f2a63983de26f4270bcf33.png)

We could run each of the instructions in the file one by one using the next command. But there's a lot going on here. So we need to go through a lot of lines until we reach the failure. Alternatively, we can tell the debugger to continue the execution until it either finishes or crashes

tuliskan continue

![019ba1406b32d758e93618d6fda64689.png](../../../../../_resources/019ba1406b32d758e93618d6fda64689.png)

PDB memungkinkan debugging dengan interaktif

PDB3 memungkinkan pengguna untuk melakukan tugas-tugas berikut saat debugging:

Menempatkan breakpoint pada bagian kode yang diinginkan
Menjalankan kode hingga breakpoint tercapai
Mengeksplorasi nilai variabel dan ekspresi pada saat runtime
Mengubah nilai variabel saat runtime
Menjalankan kode baris per baris dan melihat bagaimana kode bekerja
Menganalisis stack trace dan mengidentifikasi masalah pada program

***

kesalahn umum karena salah memberikan tanda > atau => namanya adalah off-by-one-error

Pertanyaan #4
A very common method of debugging is to add print statements to our code that display information, such as contents of variables, custom error statements, or return values of functions. What is this type of debugging called? printf debugging

![7f76d0436bb2b3448e9226f1e92ed032.png](../../../../../_resources/7f76d0436bb2b3448e9226f1e92ed032.png)


