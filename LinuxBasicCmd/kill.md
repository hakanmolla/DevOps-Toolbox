## kill Komutu


"kill" komutu, bir Unix veya Unix benzeri işletim sisteminde çalışan işlemleri sonlandırmak veya durdurmak için kullanılan bir komuttur. Bu komut, belirtilen işlem kimlik numarasına (PID) veya işlem adına göre işlemleri sonlandırabilir.

Aşağıdaki şekilde "kill" komutunun kullanımı açıklanmaktadır:

kill [seçenekler] PID 
 

## "kill" Komutunun Seçenekleri


-   -s SINYAL veya --signal=SINYAL: Belirtilen sinyali gönderir. Varsayılan olarak, "kill" komutu, işlemi sonlandırmak için "TERM" sinyalini kullanır.
-   -l veya --list: Kullanılabilen sinyallerin bir listesini gösterir.

**Örnek Kullanım**
Belirli bir PID'ye sahip işlemi sonlandırmak için aşağıdaki komutu kullanabilirsiniz:

kill 1234 
 

Bu komut, "1234" PID'ye sahip işlemi sonlandırır.

**Örneğin**, "kill" komutunu "TERM" sinyali yerine "KILL" sinyaliyle kullanmak isterseniz, aşağıdaki komutu kullanabilirsiniz:

kill -s KILL 1234 
Bu komut, "1234" PID'ye sahip işlemi "KILL" sinyaliyle sonlandırır.

Sonuç
"kill" komutu, Unix ve Unix benzeri işletim sistemlerinde çalışan işlemleri sonlandırmak veya durdurmak için kullanılan bir komuttur. Bu makalede, "kill" komutunun ne olduğunu, nasıl kullanıldığını ve en yaygın kullanılan seçeneklerini açıkladım. Umarım bu makale, "kill" komutunu daha iyi anlamanıza yardımcı olmuştur.