## Print () fonksiyonu


, Python programlama dilinde sıklıkla kullanılan bir fonksiyondur ve temel olarak ekrana yazdırma işlemi yapar. Örneklerde gösterildiği gibi, print fonksiyonu parametre olarak aldığı değerleri ekrana yazdırır.

Örneğin, "Benim adım Hakan" yazdırmak istediğimizde, print fonksiyonunu kullanabiliriz. Bu durumda print("Benim Adım : ", Adı) şeklinde bir kod yazabiliriz. Burada, "Benim Adım: " ifadesi virgülle ayrılmış bir string (metin) ve Adı değişkeni ise yazdırılacak isimdir.

Print fonksiyonunda ayrıca sep ve end parametreleri kullanılabilir. Sep parametresi, virgülle ayrılmış farklı stringleri birleştirirken kullanılan ayraçtır. Örneğin, print("Benim ", "yaşım: ", sep="") ifadesinde, "" ifadesi sep parametresi olarak kullanılmaktadır ve ekrana "Benim*yaşım: " yazdırılır.

End parametresi ise yazdırma işleminden sonra imlecin nereye yerleşeceğini belirler. Varsayılan olarak, end parametresi "\n" (yeni satır) değerini alır. Ancak, end parametresine başka bir değer verilirse, yazdırma işleminden sonra imleç bu değerin işaret ettiği yere yerleşir. Örneğin, print("Merhaba", end="--") ifadesinde, end parametresi "--" olarak belirlenmiştir ve yazdırma işleminden sonra imleç "--" ifadesinin hemen yanında kalacaktır.

File parametresi ise yazdırılan verileri bir dosyaya yazdırmak için kullanılır. Örneğin, print("Merhaba Dünya!", file=open("log.txt", "a")) ifadesinde, yazdırılan "Merhaba Dünya!" cümlesi, "log.txt" isimli bir dosyaya eklenir. "a" parametresi ise dosyanın açık olduğunu belirtir ve dosyaya yazdırmak için kullanılan bir moddur.