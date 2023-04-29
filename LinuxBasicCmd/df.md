## df Komutu


bir Unix veya Unix benzeri işletim sistemi kullandığınızı varsayarak, "df" komutunu aşağıdaki gibi kullanabilirsiniz:

df [seçenekler] [dizin veya dosya adı] 
 

Bu komut, dosya sistemlerinin disk alanı kullanımını gösterir. "df" komutu, disk alanının ne kadarının kullanıldığını, ne kadarının boş olduğunu ve dosya sisteminin kapasitesini gösterir. "df" komutu, disk alanı kullanımını belirlemek için oldukça yararlıdır ve sık sık sistem yöneticileri ve kullanıcılar tarafından kullanılır.

**Örneğin**, tüm dosya sistemlerinin disk alanı kullanımını görmek isterseniz, aşağıdaki komutu kullanabilirsiniz:

df

Bu komut, tüm dosya sistemlerinin disk alanı kullanımını yazdırır. Komutu çalıştırdıktan sonra, her dosya sisteminin kapasitesi, kullanılan alanı ve boş alanı yazdırılır.

##  "df" Komutunun Seçenekleri
-   "df" komutunun birkaç seçeneği vardır ve en yaygın olanları aşağıda açıklanmaktadır:

-   -h: Boyutu daha okunaklı hale getirmek için insan dostu bir çıktı verir.
-   -i: Inode kullanımını gösterir.
-   -t: Belirtilen dosya sistemi türünü gösterir.
-   -T: Dosya sistemlerinin türünü gösterir.

**Örneğin**, tüm dosya sistemlerinin disk alanı kullanımını insan dostu bir şekilde görmek isterseniz, aşağıdaki komutu kullanabilirsiniz:

df -h

Bu komut, tüm dosya sistemlerinin disk alanı kullanımını insan dostu bir şekilde yazdırır.

**Sonuç**
"df" komutu, Unix ve Unix benzeri işletim sistemlerinde disk alanı kullanımını belirlemek için oldukça yararlı bir araçtır. Bu makalede, "df" komutunun ne olduğunu, nasıl kullanıldığını ve en yaygın kullanılan seçeneklerini açıkladım. Umarım bu makale, "df" komutunu daha iyi anlamanıza yardımcı olmuştur.