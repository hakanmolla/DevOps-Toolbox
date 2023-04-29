## cat Komutu


Linux'un temel komutlarından biri olan cat (concatenate) komutu, bir veya birden fazla dosyanın içeriğini birleştirerek çıktı olarak sunar. Bu komut aynı zamanda dosya içeriğini görüntülemek, yeni dosyalar oluşturmak ve dosyaları birbirine eklemek için de kullanılabilir.

cat komutu, terminal penceresinde kullanılır ve dosya adı ile birlikte çağrılır. Örneğin, cat example.txt komutu, example.txt dosyasının içeriğini terminal penceresinde görüntüler. Eğer birden fazla dosya ismi belirtilirse, cat komutu bu dosyaların içeriklerini birleştirerek çıktı verir.

cat komutu ayrıca > işareti kullanılarak dosyalara yazma işlemi için de kullanılabilir. 

**Örneğin**, cat > example.txt komutu, kullanıcının girdiği metni example.txt dosyasına yazar.

## cat komutunun bazı yaygın kullanımları şunlardır:

Dosyaların içeriklerini birleştirmek için: cat file1.txt file2.txt > combined.txt
Dosya içeriğini ekranda görüntülemek için: cat file.txt
Kullanıcının girdiği metni dosyaya yazmak için: cat > file.txt
Dosya içeriğinde arama yapmak için: cat file.txt | grep "search term"
cat komutunun parametreleri arasında en yaygın olanları şunlardır:

-   -n : Satırları numaralandırır
-   -b : Boş olmayan satırları numaralandırır
-   -s : Arka arkaya gelen boş satırları tek bir satır olarak görüntüler
-   -E : Satırların sonuna $ işareti ekler
-   -T : Sekme karakterlerini ^I şeklinde görüntüler

Bu parametreler, cat komutunun işlevselliğini değiştirerek çıktıyı farklı şekillerde düzenler.

