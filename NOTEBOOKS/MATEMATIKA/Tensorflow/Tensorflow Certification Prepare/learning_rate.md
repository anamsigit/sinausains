learning rate yang kecil berarti memerlukan lebih banyak iterasi untuk mencapai konvergensi sehingga membutuhkan banyak resource untuk training model. tetapi learning rate yang kecil bisa saja membuat model terjebak dalam local minima alih-alih mencapai global minima. 

tetapi apabila learning_rate yang terlalu besar, bisa saja model akan selalu melompati global minima pada setiap iterasi. 

pemilihan learning rate adalah dengan mencoba-coba dan mengevaluasi. dimulai dari 0.1, 0.001, 0.0001 dan mengamati bagaimana model akurasinya meningkat. 