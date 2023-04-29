## less Komutu


less komutu, bir dosyanın içeriğini okumak için kullanılan bir terminal editörüdür. more komutuna benzer, ancak less daha fazla özellik ve işlevsellik sunar.

Kullanımı oldukça basittir, sadece komut satırına less komutunu yazın ve ardından okumak istediğiniz dosyanın yolunu verin. Örneğin: 

less dosya.txt 
Bir kez açıldığında, dosyanın içeriğini görüntülemek için aşağı ok tuşunu kullanabilirsiniz. İçeriği yukarı doğru kaydırmak için yukarı ok tuşunu kullanın. Dosyadan çıkmak için q tuşuna basın.

## less komutunun bazı faydalı parametreleri vardır:

-   -N : satır numaralarını gösterir
-   -i : büyük/küçük harf duyarlılığı olmadan arama yapar
-   -F : tek dosya sayfasını otomatik olarak kapatır (birçok dosya görüntüleniyorsa)
-   /aranan_kelime : belirli bir kelimeyi aramak için kullanılır (ileri arama)
-   ?aranan_kelime : belirli bir kelimeyi geriye doğru aramak için kullanılır (ters arama)

Örneğin, less -N dosya.txt komutu, dosyanın satır numaralarını da görüntüler. less -i dosya.txt komutu ise büyük/küçük harf duyarlılığı olmadan dosyayı arar.