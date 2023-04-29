# mv Komutu


mv: mv komutu, dosya veya klasörleri taşımak veya yeniden adlandırmak için kullanılır. Örneğin, mv dosya1.txt dosya2.txt komutu, dosya1.txt'yi dosya2.txt olarak adlandırılan bir dosyaya yeniden adlandırır.

## mv komutu da bazı kullanışlı parametrelere sahiptir:

-   -i : Bu parametre, taşıma işlemi sırasında üzerine yazma işlemi gerçekleşmeden önce kullanıcıya bir onay sorar. Örneğin, mv -i dosya1.txt dosya2.txt komutu, dosya1.txt'yi dosya2.txt olarak adlandırılan bir dosyaya taşırken, eğer dosya2.txt adlı bir dosya zaten varsa kullanıcıya üzerine yazma işlemini onaylaması için bir soru sorar.
-   -u : Bu parametre, taşıma işlemi sırasında hedef dosyanın değiştirildiği durumlarda sadece daha yeni olan dosyaların taşınmasını sağlar. Örneğin, mv -u dosya1.txt dosya2.txt komutu, dosya1.txt'yi dosya2.txt olarak adlandırılan bir dosyaya taşırken, eğer dosya2.txt adlı bir dosya zaten varsa, sadece dosya1.txt daha yeni ise taşınır.