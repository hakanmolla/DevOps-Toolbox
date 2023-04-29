## touch Komutu


Linux'da touch komutu, kullanıcının belirtilen dosya adı veya yolunda var olan bir dosyayı oluşturmasına veya dosyanın değiştirilme zamanını güncellemesine izin verir. Bu komut, dosyaların içeriğini değiştirmez, sadece dosyanın var olup olmadığını kontrol eder ve gerekirse oluşturur. Touch komutunun kullanımı oldukça basittir ve çoğu kullanıcının birkaç kez karşılaşabileceği bir komuttur.

Temel kullanım:

touch [seçenekler] dosya_adı

## touch komutunu kullanırken, kullanıcının birkaç farklı seçeneği vardır. En yaygın seçenekler şunlardır:

-   -a, --derece : Değiştirme tarihini ayarlamaz, ancak dosyanın erişim tarihini günceller. -c, --no-create : Dosya yoksa, dosyayı oluşturmayıp hata mesajı verir. 
-   -d, --tarih : Dosyanın değiştirilme tarihini, belirtilen tarih ve saatle değiştirir. -m, --derece : Erişim tarihini ayarlamaz, ancak dosyanın değiştirilme tarihini günceller. -r, --referans : Başka bir dosyadan değiştirme tarihini kopyalar. -t, --tarih : Değiştirme tarihini belirtilen tarih ve saatle değiştirir.

**Örnek kullanım:**

Yeni bir dosya oluşturma: touch file.txt Bu komut, file.txt adında bir dosya oluşturur. Eğer bu dosya önceden varsa, dosyanın değiştirme tarihini günceller.

Bir dosyanın değiştirilme tarihini belirli bir tarihe ayarlama: touch -t 202201012359.59 file.txt Bu komut, file.txt dosyasının değiştirme tarihini 2022 yılının 1 Ocak 23:59.59 tarihine ayarlar.

Bir dosyanın değiştirilme tarihini başka bir dosyaya göre ayarlama: touch -r file1.txt file2.txt Bu komut, file1.txt dosyasının değiştirme tarihini file2.txt dosyasına kopyalar.

Birden fazla dosya oluşturma: touch file1.txt file2.txt file3.txt Bu komut, file1.txt, file2.txt ve file3.txt dosyalarını oluşturur veya varsa değiştirir.

Bir klasör altında tüm dosyaların değiştirilme tarihini güncelleme: touch -c -m . Bu komut, mevcut tüm dosyaların değiştirilme tarihini günceller. "-c" seçeneği, mevcut olmayan dosyalar için hata mesajı görmezden gelir. "-m" seçeneği, dosyanın erişim tarihini değiştirmez, sadece değiştirme tarihini