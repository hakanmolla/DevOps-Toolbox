## Sip Hata Mesajları
---
Sip Haberleşmesinde bilinen sip hata kodlarının anlamları ile birlikte aşağıdaki gibidir.
---
## En Çok Kullanılan SIP Mesajları ve Anlamları

**REGISTER  :**	To başlığı alanında listelenen URI’yi bir SIP sunucusuna kaydetmek ve Contact başlığı alanında verilen ağ adresiyle ilişkilendirmek içindir.
**INVITE    :**	Arama yapmak için bir iletişim başlatır. İstek bir kullanıcı istemcisi (ör. IP telefon) tarafından bir SIP sunucusuna gönderilir. Hali hazırda kurulmuş bir iletişim sırasında gönderildiğinde (RE-INVITE), oturumu değiştirir (ör. çağrıyı beklemeye alma).
**ACK       :**	Bir INVITE isteğine son bir yanıt aldığını doğrulamak için kullanılır.
**BYE       :**	Bir iletişimin sonlandırıldığını bildirir ve çağrıyı bitirir.
**CANCEL    :**	Bekleyen tüm istekleri iptal eder. Hala çalan bir çağrıyı cevaplamadan önce, sonlandırmak için kullanılır.
**UPDATE    :**	İletişim durumunu değiştirmeden oturumun durumunu değiştirir
**REFER     :**	Alıcıdan çağrıyı aktarmak amacıyla bir talepte bulunmasını ister.
**PRACK     :**	Geçici onay. Geçici bir yanıta yanıt olarak gönderilir.
**SUBSCRIBE :**	Bir bildirimden gelen olayların bildirilmesi için bir abonelik başlatır.
**NOTIFY    :**	Yeni bir etkinliğin bildirimlerini bir aboneye bildirmek için kullanılır.
**PUBLISH   :**	Bir etkinliği bildirim sunucusunda yayınlamak için kullanılır.
**MESSAGE   :**	Kısa mesaj gönderir. Anlık mesajlaşma uygulamalarında kullanılır.
**INFO      :**	Oturum durumunu değiştirmeyen oturum ortası bilgileri göndermek için kullanılır. Bu yöntem genellikle DTMF rölesi için kullanılır.
**OPTIONS   :**	Bir uç noktanın yeteneklerini sorgular. Genellikle NAT ve keepalive için kullanılır.

## 1xx = Bilgi İçerikli SIP Cevapları
---

'100 Deniyor' – Gelişmiş arama yapılmaktadır böylece çatal oluşturan bir proxy 100 Deniyor cevabı göndermelidir.
'180 Çalıyor' – Hedef Kullanıcı Temsilcisi DAVET mesajını almış ve aramanın kullanıcısına uyarı vermektedir.
'181 Arama' Yönlendiriliyor – İsteğe bağlıdır, aramanın yönlendirildiğini belirtmek için Sunucu gönderir.
182 Sıraya Alındı – Hedef geçici olarak kullanılamıyor; sunucu, hedef kullanılana kadar aramayı sıraya aldı.
183 Oturum Devam Ediyor – Bu cevap halen kurulan bir arama için ekstra bilgi göndermede kullanılabilir.
199 Erken Diyalog Sonlandı – Erken diyaloğun sonlandığını belirtmek için Kullanıcı Temsilcisi Sunucusu gönderir.
2xx = Başarı cevapları
200 Tamam – Talebin başarılı olduğunu gösterir.
202 Kabul edildi – Temelde başvurular için kullanılan talebin işleme alındığını gösterir.
204 Bildirim Yok – Talebin başarılı olduğunu fakat cevap alınmadığını gösterir.
3xx = Yeni adrese yönlendirme cevapları
300 Çoklu Seçenekler – Kullanıcının/müşterinin seçeceği çeşitli seçeneklerden birine çözümlenen adres.
301 Kalıcı Olarak Taşındı – Orjinal Talep URL’si geçersizdir, yeni adres İletişim başlığında sunulmaktadır.
302 Geçici Olarak Taşındı – Müşteri, İletişim alanındaki adreste denemelidir.
305 Proxy Kullanın – İletişim alanı, istenen yere ulaşmada kullanılması gereken bir proxy detayı verir.
380 Alternatif Hizmet – Arama başarısız oldu fakat alternatifler mesaj gövdesinde sunulmaktadır.
4xx = Talebin yerine getirilememesi
400 Geçersiz Talep – Talep, hatalı söz dizimi nedeniyle anlaşılamadı.
401 Yetkisiz Kullanım – Talep, kullanıcı yetkisi gerektirir. Bu cevap UAS’ler ve kaydolanlar tarafından kullanılır.
402 Ödeme Gerekli – (Gelecekte kullanılmak üzere ayrılmıştır).
403 Yasaklı – Sunucu talebi anladı fakat yerine getirmeyi reddediyor.
404 Bulunamadı – Sunucu, kullanıcının (Kullanıcı bulunamadı) bulunmadığı tanımlayıcı bilgisine sahiptir.
405 İzin Verilmeyen Yöntem – Talep Satırında belirtilen yöntem anlaşıldı fakat izin verilmiyor.
406 Kabul Edilemez – Kaynak sadece Kabul edilemez içeriğe sahip cevaptlar üretebilmektedir.
407 Proxy Kimlik Doğrulaması Gerekli – Talep, kullanıcı kimlik bilgilerinin doğrulanmasını gerektiriyor.
408 Talep Zaman Aşımı – Kullanıcı gerekli süre içerisinde bulunamadı.
409 Uyumsuzluk – Kullanıcı zaten kayıtlıdır (kullanım dışı).
410 Gitmiş – Bir zamanlar var olan bu kullanıcı artık burada yok.
411 Uzunluk Gerekli – Sunucu, geçerli bir içerik uzunluğu olmayan talebi kabul etmez (kullanım dışı).
412 Koşullu Talep Başarısız Oldu – Belirtilen ön koşul yerine getirilmedi.
413 Talep Metni Çok Fazla – Talep gövde metni çok fazla.
414 Talep URL’si Çok Uzun – Sunucu talebi yerine getirmeyi reddediyor, Talep URL’si sunucunun yorumlayabileceğinden uzun.
415 Desteklenmeyen Medya Tipi – Talep gövde metni desteklenmeyen bir formatta.
416 Desteklenmeyen URL Düzeni – Talep URL’si sunucu tarafından tanınmıyor.
417 Bilinmeyen Kaynak Önceliği – Bir kaynak önceliği seçenek etiketi vardı fakat Kaynak Önceliği başlığı yoktu.
420 Geçersiz Uzantı – Geçersiz SIP Protokol Uzantısı kullanıldı fakat sunucu tarafından anlaşılmadı.
421 Uzantı Gerekli – Sunucu, Desteklenenler başlığında listelenmeyen özel bir uzantı gerektiriyor.
422 Oturum Aralığı Çok Az – Talep, minimum sürenin altında bir Oturum Bitiş Tarihi başlık alanı içeriyor.
423 Ara Çok Kısa – Kaynağın sona erme süresi çok kısa.
424 Kötü Kullanım Bilgileri – Talebin konum içeriği hatalıydı veya başarısız oldu.
428 Kullanım Kimliği Başlığı – Sunucu politikası bir Kimlik başlığı gerektiriyor fakat bir başlık sunulmadı.
429 Referans Veren Kimliği Sağlayın – Sunucu, talep üzerine geçerli bir Referansı Veren token’ı almadı.
430 Akış Başarısız Oldu – Bir kullanıcı temsilcisine özel akış başarısız oldu fakat diğer akışlar başarılı olabilir.
433 Anonimliğe İzin Verilmez – Talep reddedildi çünkü anonimdi.
436 Geçersiz Kimlik Bilgileri – Talebin bir Kimlik Bilgileri başlığı vardır ve içindeki URL düzeninin referansı verilemez.
437 Desteklenmeyen Sertifika – Sunucu, talebi imzalayan alan için sertifikanın geçerliliğini doğrulayamadı.
438 Geçersiz Kimlik Başlığı – Sunucu bir talebi imzalamada kullanılan geçerli bir sertifika aldı ancak imzayı doğrulayamadı.
439 İlk Atlamada Giden Desteği Yok – İlk giden proxy, “giden” özelliğini desteklemiyor.
440 Maksimum Genişlik Aşıldı – Bir SIP proxy, cevap kavramının istenen bir parallel çatal yerine getirmek için yeterli Maksimum Genişliğe sahip olduğunu belirlediyse ve bu proxy seri çatallamayla telafi etmede isteksizse ya da bunu başaramıyorsa veya bir yeniden yönlendirme gönderiyorsa, bu proxy bir 440 cevabı vermelidir. 440 cevabı alan bir müşteri, talebinin tüm olası yerlere ulaşmadığını anlayabilir.
469 Geçersiz Bilgi Paketi – Bir SIP UA, UA’nın alım isteği belirtmediği bir Bilgi Paketine bağlı bir BİLGİ talebi alırsa; UA, UA’nın BİLGİ taleplerini almak istediği Bilgi Talepleri bulunan bir Recv bilgileri başlığı içeren bir 469 cevabı GÖNDERMELİDİR.
470 Onay Gerekli – Talep kaynağı, böyle bir talebi yerine getirmek için alıcının iznine sahip değildi.
480 Geçici Olarak Ulaşılamıyor – Aranan kişiye şu anda ulaşılamıyor.
481 Arama/İşlem Mevcut Değil – Sunucu, herhangi bir diyalog veya işlemle eşleşen bir talep almadı.
482 Döngü Tespit Edildi – Sunucu bir döngü tespit etti.
483 Çok Fazla Atlama – Maksimum İletme başlığı ‘0’ değerine ulaştı.
484 Eksik Adres – Talep URL’si eksik.
485 Belirsiz – Talep URL’si belirsiz.
486 Burası Meşgul – Aranan kişi meşgul.
487 Talep Sona Erdi – Talep sonlandırıldı veya iptal edildi.
488 Burada Kabul Edilmez – Talep URL’si oturum tanımının bazı yönleri kabul edilmez.
491 Talep Beklemede – Sunucuda aynı diyalogdan birkaç bekleyen talep var.
493 Deşifre Edilemiyor – Deşifre Edilemiyor Talebi, alıcının deşifre edemediği şifrelenmiş bir MIME gövde metni içerir.
494 Güvenlik Anlaşması Gerekli – Sunucu, müzakere edilmiş bir güvenlik mekanizması gerektiren bir talep aldı.
5xx = Sunucu hataları
500 Dahili Sunucu Hatası – Bazı beklenmeyen koşullar nedeniyle sunucu talebi yerine getiremedi.
501 Uygulanmadı – SIP talep yöntemi burada uygulanmaz.
502 Geçersiz Ağ Geçidi – Sunucu bir talebi yerine getirmeye çalışırken, alt sistemdeki bir sunucudan geçersiz bir cevap aldı.
503 Hizmet Kullanılamıyor – Sunucu bakımda veya geçici olarak aşırı yükleme vardır, talep işlenemiyor.
504 Sunucuda Zaman Aşımı – Sunucu bir talebi işlemeye çalışırken başka bir sunucuya erişmeye çalıştı, zamanında cevap veremedi.
505 Sürüm Desteklenmiyor – Talepteki SIP protokolü sürümü sürücü tarafından desteklenmiyor.
513 Mesaj Çok Fazla – Talep mesaj uzunluğu, sürücünün işleyebileceğinden daha uzundur.
555 Anlık Bildirim Hizmeti Desteklenmiyor – Sunucu, pn sağlayıcı URL parametresinde belirtilen anlık bildirim hizmetini desteklemiyor.
580 Ön Koşul Geçersizliği – Sunucu, teklifte belirtilen bazı sınırlamaları karşılayamıyor veya karşılamak istemiyor.
6xx = Global olarak yerine getirilemeyenler
600 Her Yer Meşgul – Tüm olası hedefler meşguldür.
603 Reddedilme – Hedef, aramaya katılamıyor veya katılmak istemiyor; alternatif hedef bulunmuyor.
604 Hiçbir Yerde Bulunmuyor – Talep edilen kullanıcının hiçbir yerde bulunmadığına dair sunucunun yetkisel bilgisi mevcuttur.
606 Kabul Edilemez – Kullanıcının temsilcisine başarıyla ulaşıldı ancak oturum tanımının bazı yönleri kabul edilmedi.
607 İstenmedi – Aranan taraf, arayan tarafın aramasını istemedi. Arayan tarafın gelecekteki girişimlerinin de benzer şekilde reddedilmesi muhtemeldir.
