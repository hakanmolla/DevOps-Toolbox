## uptime Komutu


uptime komutu, Linux işletim sistemi üzerinde sistemin ne kadar süredir çalıştığını, kullanıcı sayısını, yüksekliği ve ortalama yüksekliği gösteren bir komuttur.

Komutu çalıştırmak için terminal ekranına "uptime" yazmanız yeterlidir. Çıktıda, sistem çalışma süresi, toplam kullanıcı sayısı, etkin kullanıcı sayısı ve yüksekliği (1 dakika, 5 dakika ve 15 dakika) listelenir.

Örneğin, aşağıdaki çıktıda sistem, 43 gün, 1 saat, 45 dakika ve 54 saniyedir çalışıyor ve 3 kullanıcı bağlıdır:

$ uptime

18:52:51 up 43 days, 1:45, 3 users, load average: 0.19, 0.10, 0.06

Bu çıktıda, "load average" kısmı, sistemdeki yükün yoğunluğunu gösterir. 1 dakika, 5 dakika ve 15 dakika aralıklarındaki yüksekliklerin sırasıyla 0.19, 0.10 ve 0.06 olduğunu gösterir. Yükseklik değerleri, ne kadar yüksek olduğuyla ilgili bir fikir verir. Örneğin, 1.00'den yüksek bir yükseklik, işlemcinin tam kapasiteyle çalıştığı anlamına gelir ve bu durumda sistemin daha yavaş çalışmasına neden olabilir.

Uptime komutu, sistem durumu hakkında hızlı bir bakış sağlamak için yararlı bir araçtır.