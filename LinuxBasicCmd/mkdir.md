## mkdir Komutu


Linux işletim sistemleri, klasörler ve dosyalar oluşturmak, silmek ve yönetmek için birçok farklı komut içerir. Bunlardan biri de "mkdir" komutudur. "mkdir" (make directory) komutu, yeni bir klasör oluşturmak için kullanılır.

# Temel kullanımı

"mkdir" komutunu kullanarak yeni bir klasör oluşturmak için aşağıdaki formatta bir komut yazmanız gerekir:

**Örneğin**, "test" adlı bir klasör oluşturmak için aşağıdaki komutu kullanabilirsiniz:

mkdir test

Bu komut, mevcut dizinde "test" adlı bir klasör oluşturur. Klasör adının yanı sıra, "mkdir" komutu bir dizi seçenek de alabilir. Bu seçenekler, klasörün oluşturulacağı dizinleri veya dosya izinlerini belirlemenize olanak tanır.

## Kullanım seçenekleri

-   "-p" seçeneği: Belirtilen klasör adının yanı sıra, alt klasörleri de oluşturur. Bu, birden fazla alt klasörün oluşturulması gerektiğinde kullanışlıdır.

**Örneğin**, "test1" adlı bir klasör içinde "test2" adlı bir alt klasör oluşturmak için aşağıdaki komutu kullanabilirsiniz:

mkdir -p test1/test2

Bu komut, "test1" klasörünü oluşturur ve içinde "test2" adlı bir alt klasör oluşturur.

-   "-m" seçeneği: Yeni klasörün dosya izinlerini belirlemenize olanak tanır.

**Örneğin**, "test" adlı bir klasör oluştururken dosya izinlerini ayarlamak için aşağıdaki komutu kullanabilirsiniz:

mkdir -m 777 test

Bu komut, "test" adlı klasörün tüm kullanıcılara rwx (okuma, yazma ve çalıştırma) izinleri verir.

-   "-v" seçeneği: İşlem sırasında yapılan işlemleri ekrana yazdırır.

**Örneğin**, "test" adlı bir klasör oluştururken işlemleri ekrana yazdırmak için aşağıdaki komutu kullanabilirsiniz:

mkdir -v test

Bu komut, "test" adlı klasörün oluşturulduğunu ekrana yazdırır.

## Sonuç olarak, 

"mkdir" komutu, Linux sistemlerinde yeni klasörler oluşturmak için kullanılan basit ama güçlü bir komuttur. Kullanıcıların dosya ve klasörleri daha iyi organize etmelerine ve dosya sistemi üzerinde daha iyi kontrol sağlamalarına yardımcı olur.



