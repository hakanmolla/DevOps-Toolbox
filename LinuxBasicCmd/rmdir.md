

## rmdir Komutu


rmdir komutu, Linux işletim sisteminde kullanılan bir komuttur ve boş bir dizini silmek için kullanılır. Dizin içinde dosya ya da alt dizin varsa, silme işlemi gerçekleştirilemez.

Kullanımı oldukça basittir. Sadece silmek istediğiniz boş dizinin adını parametre olarak vermeniz yeterlidir. Örneğin:

rmdir my_directory 
 

Bu komut, "my_directory" adlı dizini siler.

## rmdir komutunun bazı yaygın kullanılan parametreleri şunlardır:

-   -p: Silinecek dizinin yanındaki tüm üst dizinleri de siler. Örneğin, rmdir -p my_directory komutu, "my_directory" dizinini ve yanındaki tüm üst dizinleri siler.

-   -v: Silme işlemini gerçekleştirirken işlem hakkında bilgi verir.

-   --ignore-fail-on-non-empty: Boş olmayan bir dizin silmeye çalışırken, hata mesajı yerine uyarı mesajı gösterir ve devam eder.

-   --help: rmdir komutunun kullanımı hakkında bilgi almak için kullanılır.

-   --version: rmdir komutunun sürüm numarasını gösterir.

Örneğin, rmdir -pv my_directory komutu, "my_directory" dizinini ve yanındaki tüm üst dizinleri siler ve işlem hakkında bilgi verir.