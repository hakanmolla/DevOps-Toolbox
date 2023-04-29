## date Komutu


date komutu, sistem saatini ve tarihini görüntülemek için kullanılan bir Linux komutudur. Bu komut ayrıca sistem saatini ayarlamak veya belirli bir tarih / saat biçimini ayarlamak için de kullanılabilir.

Basitçe date komutunu çalıştırdığınızda, sistem tarihini ve saatini, yerel saati, zaman dilimini ve UTC saati gibi bilgileri gösteren çıktıyı alırsınız. 


**Örneğin** 

```base
date
```

## date komutu birçok parametre ile kullanılabilir. Bunlardan bazıları:

-   -s: Sistem tarihini ve saatini ayarlamak için kullanılır. Örneğin, date -s "20 JAN 2022 14:30:00" komutu, sistem saatinin 20 Ocak 2022 saat 14:30:00 olarak ayarlanmasını sağlar.
-   +%format: Tarih ve saat biçimlendirme için kullanılır. format parametresi, istenen tarih / saat biçimini belirleyen özel karakterlerle oluşturulur. Örneğin,  date +%Y-%m-%d komutu, "2022-01-20" gibi bir çıktı döndürür.
-   -u: UTC zaman dilimindeki tarihi ve saati görüntüler. Örneğin, date -u komutu, UTC zaman dilimindeki tarihi ve saatini gösterir.

Bu, date komutunun bazı temel kullanımlarından sadece birkaçıdır. man date komutu ile daha fazla bilgiye erişebilirsiniz.