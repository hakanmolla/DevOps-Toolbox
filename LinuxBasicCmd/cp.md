## cp Komutu


cp komutu, bir dosyayı veya klasörü başka bir dosyaya veya klasöre kopyalamak için kullanılır. Örneğin, cp dosya1.txt dosya2.txt komutu, dosya1.txt'yi dosya2.txt olarak adlandırılan yeni bir dosyaya kopyalar.

## cp komutu bazı kullanışlı parametrelere sahiptir:

- -r : Bu parametre, klasörleri kopyalamak için kullanılır. Örneğin, cp -r klasor1 klasor2 komutu, klasor1 adlı klasörü klasor2 adlı yeni bir klasöre kopyalar.
- -i : Bu parametre, kopyalama işlemi sırasında üzerine yazma işlemi gerçekleşmeden önce kullanıcıya bir onay sorar.

**Örneğin**, cp -i dosya1.txt dosya2.txt komutu, 

dosya1.txt'yi dosya2.txt olarak adlandırılan bir dosyaya kopyalarken, eğer dosya2.txt adlı dosya zaten varsa kullanıcıya üzerine yazma işlemini onaylaması için bir soru sorar.