
## Asterisk AGI Nedir?

Asterisk AGI (Asterisk Gateway Interface), Asterisk PBX sistemiyle etkileşim kurmak için kullanılan bir arabirimdir. AGI, uygulamalarınızın Asterisk ile doğrudan iletişim kurmasını ve arama süreçlerini yönetmesini sağlar.

Asterisk AGI, uygulamalarınızın bir dizi işlem gerçekleştirmesine izin verir, örneğin:

-	Arama oluşturma ve alma
-	Arama yönlendirme ve yönetimi
-	Arama durumunu izleme
-	Sesli yanıt sistemi oluşturma
-	Otomatik arama
-	Faks gönderme ve alma

Asterisk AGI, herhangi bir programlama dilinde yazılabilen bir API'dir. AGI, programlama dili bağımsız olduğundan, birçok farklı dilde uygulamalar yazmak mümkündür.

## Asterisk AGI'yi Kullanmak

Asterisk AGI'yi kullanmak için öncelikle bir AGI scripti yazmanız gerekir. AGI scriptleri, PBX sistemine bağlandığında çalışacak olan uygulamalarınızı içerir.

Bir AGI scripti, AGI protokolünü kullanarak Asterisk PBX sistemine bağlanır ve AGI ile iletişim kurar. AGI protokolü, AGI scriptine çeşitli bilgiler sağlar, örneğin:

-	Çağrının kim tarafından yapıldığı
-	Çağrının hangi numaradan yapıldığı
-	Çağrının hangi numaraya yapıldığı
-	Çağrının yönlendirme bilgileri
-	Çağrının durumu (başlatıldı, sonlandırıldı, bekletiliyor vb.)

AGI scriptleri, birçok programlama diliyle yazılabilir, örneğin PHP, Python, Ruby, Perl, Bash vb. AGI scripti, Asterisk PBX sistemiyle doğrudan iletişim kurarak çağrıyı yönetir.

AGI scripti, önce Asterisk PBX sistemiyle bağlantı kurar, sonra AGI protokolünü kullanarak çağrı bilgilerini alır. Daha sonra, çağrıyı yönetmek için gerekli işlemleri gerçekleştirir ve sonunda çağrıyı sonlandırır.

## AGI scriptleri, bir dizi işlem gerçekleştirebilir, örneğin:

-	Arama oluşturma ve alma
-	Arama yönlendirme ve yönetimi
-	Arama durumunu izleme
-	Sesli yanıt sistemi oluşturma
-	Otomatik arama
-	Faks gönderme ve alma

## Sonuç

Asterisk AGI, uygulamalarınızın Asterisk PBX sistemine doğrudan erişimini sağlar. AGI scriptleri, çağrıyı yönetmek için birçok işlem gerç