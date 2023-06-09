## Sip Hata Mesajları

* Sip Haberleşmesinde bilinen sip hata kodlarının anlamları ile birlikte aşağıdaki gibidir.

## En Çok Kullanılan SIP Mesajları ve Anlamları

* **REGISTER  :**	To başlığı alanında listelenen URI’yi bir SIP sunucusuna kaydetmek ve Contact başlığı alanında verilen ağ adresiyle ilişkilendirmek içindir.
* **INVITE    :**	Arama yapmak için bir iletişim başlatır. İstek bir kullanıcı istemcisi (ör. IP telefon) tarafından bir SIP sunucusuna gönderilir. Hali hazırda kurulmuş bir iletişim sırasında gönderildiğinde (RE-INVITE), oturumu değiştirir (ör. çağrıyı beklemeye alma).
* **ACK       :**	Bir INVITE isteğine son bir yanıt aldığını doğrulamak için kullanılır.
* **BYE       :**	Bir iletişimin sonlandırıldığını bildirir ve çağrıyı bitirir.
* **CANCEL    :**	Bekleyen tüm istekleri iptal eder. Hala çalan bir çağrıyı cevaplamadan önce, sonlandırmak için kullanılır.
* **UPDATE    :**	İletişim durumunu değiştirmeden oturumun durumunu değiştirir
* **REFER     :**	Alıcıdan çağrıyı aktarmak amacıyla bir talepte bulunmasını ister.
* **PRACK     :**	Geçici onay. Geçici bir yanıta yanıt olarak gönderilir.
* **SUBSCRIBE :**	Bir bildirimden gelen olayların bildirilmesi için bir abonelik başlatır.
* **NOTIFY    :**	Yeni bir etkinliğin bildirimlerini bir aboneye bildirmek için kullanılır.
* **PUBLISH   :**	Bir etkinliği bildirim sunucusunda yayınlamak için kullanılır.
* **MESSAGE   :**	Kısa mesaj gönderir. Anlık mesajlaşma uygulamalarında kullanılır.
* **INFO      :**	Oturum durumunu değiştirmeyen oturum ortası bilgileri göndermek için kullanılır. Bu yöntem genellikle DTMF rölesi için kullanılır.
* **OPTIONS   :**	Bir uç noktanın yeteneklerini sorgular. Genellikle NAT ve keepalive için kullanılır.

## 1xx = Informational SIP responses / Bilgi İçerikli SIP Cevapları

* `100 Trying / Deniyor` – Gelişmiş arama yapılmaktadır böylece çatal oluşturan bir proxy 100 Deniyor cevabı göndermelidir.
* `180 Ringing / Çalıyor` – Hedef Kullanıcı Temsilcisi DAVET mesajını almış ve aramanın kullanıcısına uyarı vermektedir.
* `181 Call Is Being Forwarded  / Arama' Yönlendiriliyor` – İsteğe bağlıdır, aramanın yönlendirildiğini belirtmek için Sunucu gönderir.
* `182 Queued / Sıraya Alındı` – Hedef geçici olarak kullanılamıyor; sunucu, hedef kullanılana kadar aramayı sıraya aldı.
* `183 Session Progress / Oturum Devam Ediyor` – Bu cevap halen kurulan bir arama için ekstra bilgi göndermede kullanılabilir.
* `199 Early Dialog Terminated / Erken Diyalog Sonlandı` – Erken diyaloğun sonlandığını belirtmek için Kullanıcı Temsilcisi Sunucusu gönderir.

## 2xx = Success responses / Başarı cevapları :

* `200 Ok / Tamam` – Talebin başarılı olduğunu gösterir.
* `202 No Notification / Kabul edildi` – Temelde başvurular için kullanılan talebin işleme alındığını gösterir.
* `204 No Notification / Bildirim Yok` – Talebin başarılı olduğunu fakat cevap alınmadığını gösterir.

## 3xx = Redirection responses / Yeni adrese yönlendirme cevapları :

* `300 Multiple Choices / Çoklu Seçenekler` – Kullanıcının/müşterinin seçeceği çeşitli seçeneklerden birine çözümlenen adres.
* `301 Moved Permanently / Kalıcı Olarak Taşındı` – Orjinal Talep URL’si geçersizdir, yeni adres İletişim başlığında sunulmaktadır.
* `302 Moved Temporarily / Geçici Olarak Taşındı` – Müşteri, İletişim alanındaki adreste denemelidir.
* `305 Use Proxy / Proxy Kullanın` – İletişim alanı, istenen yere ulaşmada kullanılması gereken bir proxy detayı verir.
* `380 Alternative Service / Alternatif Hizmet` – Arama başarısız oldu fakat alternatifler mesaj gövdesinde sunulmaktadır.

## 4xx = Request failures / Talebin yerine getirilememesi:

* `400 Bad Request / Geçersiz Talep` – Talep, hatalı söz dizimi nedeniyle anlaşılamadı.
* `401 Unauthorized / Yetkisiz Kullanım` – Talep, kullanıcı yetkisi gerektirir. Bu cevap UAS’ler ve kaydolanlar tarafından kullanılır.
* `402 Payment Required  / Ödeme Gerekli` – (Gelecekte kullanılmak üzere ayrılmıştır).
* `403 Forbidden / Yasaklı` – Sunucu talebi anladı fakat yerine getirmeyi reddediyor.
* `404 Not Found / Bulunamadı` – Sunucu, kullanıcının (Kullanıcı bulunamadı) bulunmadığı tanımlayıcı bilgisine sahiptir.
* `405 Method Not Allowed / İzin Verilmeyen Yöntem` – Talep Satırında belirtilen yöntem anlaşıldı fakat izin verilmiyor.
* `406 Not Acceptable / Kabul Edilemez` – Kaynak sadece Kabul edilemez içeriğe sahip cevaptlar üretebilmektedir.
* `407 Proxy Authentication Required / Proxy Kimlik Doğrulaması Gerekli` – Talep, kullanıcı kimlik bilgilerinin doğrulanmasını gerektiriyor.
* `408 Request Timeout / Talep Zaman Aşımı` – Kullanıcı gerekli süre içerisinde bulunamadı.
* `409 Conflict / Uyumsuzluk` – Kullanıcı zaten kayıtlıdır (kullanım dışı).
* `410 Gone / Gitmiş` – Bir zamanlar var olan bu kullanıcı artık burada yok.
* `411 Length Required / Uzunluk Gerekli` – Sunucu, geçerli bir içerik uzunluğu olmayan talebi kabul etmez (kullanım dışı).
* `412 Conditional Request Failed  / Koşullu Talep Başarısız Oldu` – Belirtilen ön koşul yerine getirilmedi.
* `413 Request Entity Too Large / Talep Metni Çok Fazla` – Talep gövde metni çok fazla.
* `414 Request URI Too Long / Talep URL’si Çok Uzun` – Sunucu talebi yerine getirmeyi reddediyor, Talep URL’si sunucunun yorumlayabileceğinden uzun.
* `415 Unsupported Media Type / Desteklenmeyen Medya Tipi` – Talep gövde metni desteklenmeyen bir formatta.
* `416 Unsupported URI Scheme / Desteklenmeyen URL Düzeni` – Talep URL’si sunucu tarafından tanınmıyor.
* `417 Uknown Resource-Priority / Bilinmeyen Kaynak Önceliği` – Bir kaynak önceliği seçenek etiketi vardı fakat Kaynak Önceliği başlığı yoktu.
* `420 Bad Extension / Geçersiz Uzantı` – Geçersiz SIP Protokol Uzantısı kullanıldı fakat sunucu tarafından anlaşılmadı.
* `421 Extension Required / Uzantı Gerekli` – Sunucu, Desteklenenler başlığında listelenmeyen özel bir uzantı gerektiriyor.
* `422 Session Interval Too Small / Oturum Aralığı Çok Az` – Talep, minimum sürenin altında bir Oturum Bitiş Tarihi başlık alanı içeriyor.
* `423  Interval Too Brief / Ara Çok Kısa` – Kaynağın sona erme süresi çok kısa.
* `424 Bad Location Information/ Kötü Kullanım Bilgileri` – Talebin konum içeriği hatalıydı veya başarısız oldu.
* `428 Use Identity Header / Kullanım Kimliği Başlığı` – Sunucu politikası bir Kimlik başlığı gerektiriyor fakat bir başlık sunulmadı.
* `429 Provide Referrer Identity / Referans Veren Kimliği Sağlayın` – Sunucu, talep üzerine geçerli bir Referansı Veren token’ı almadı.
* `430 Flow Failed / Akış Başarısız Oldu` – Bir kullanıcı temsilcisine özel akış başarısız oldu fakat diğer akışlar başarılı olabilir.
* `433 Anonymity Disallowed / Anonimliğe İzin Verilmez` – Talep reddedildi çünkü anonimdi.
* `436 Bad Identity Info  / Geçersiz Kimlik Bilgileri` – Talebin bir Kimlik Bilgileri başlığı vardır ve içindeki URL düzeninin referansı verilemez.
* `437 Unsupported Certificate / Desteklenmeyen Sertifika` – Sunucu, talebi imzalayan alan için sertifikanın geçerliliğini doğrulayamadı.
* `438 Invalid Identity Header / Geçersiz Kimlik Başlığı` – Sunucu bir talebi imzalamada kullanılan geçerli bir sertifika aldı ancak imzayı doğrulayamadı.
* `439 First Hop Lacks Outbound Support / İlk Atlamada Giden Desteği Yok – İlk giden proxy, “giden” özelliğini desteklemiyor.
* `440 Max-Breadth Exceeded / Maksimum Genişlik Aşıldı` – Bir SIP proxy, cevap kavramının istenen bir parallel çatal yerine getirmek için yeterli Maksimum Genişliğe sahip olduğunu belirlediyse ve bu proxy seri çatallamayla telafi etmede isteksizse ya da bunu başaramıyorsa veya bir yeniden yönlendirme gönderiyorsa, bu proxy bir 440 cevabı vermelidir. 440 cevabı alan bir müşteri, talebinin tüm olası yerlere ulaşmadığını anlayabilir.
* `469 Bad Info Package/ Geçersiz Bilgi Paketi` – Bir SIP UA, UA’nın alım isteği belirtmediği bir Bilgi Paketine bağlı bir BİLGİ talebi alırsa; UA, UA’nın BİLGİ taleplerini almak istediği Bilgi Talepleri bulunan bir Recv bilgileri başlığı içeren bir 469 cevabı GÖNDERMELİDİR.
* `470 Consent Needed  / Onay Gerekli` – Talep kaynağı, böyle bir talebi yerine getirmek için alıcının iznine sahip değildi.
* `480 Temporarily Unavailable / Geçici Olarak Ulaşılamıyor` – Aranan kişiye şu anda ulaşılamıyor.
* `481 Call/Transaction Does Not Exist / Arama/İşlem Mevcut Değil` – Sunucu, herhangi bir diyalog veya işlemle eşleşen bir talep almadı.
* `482 Loop Detected / Döngü Tespit Edildi` – Sunucu bir döngü tespit etti.
* `483 Too Many Hops / Çok Fazla Atlama` – Maksimum İletme başlığı ‘0’ değerine ulaştı.
* `484 Address Incomplete / Eksik Adres` – Talep URL’si eksik.
* `485 Ambiguous / Belirsiz` – Talep URL’si belirsiz.
* `486 Busy Here / Burası Meşgul` – Aranan kişi meşgul.
* `487 Request Terminated / Talep Sona Erdi` – Talep sonlandırıldı veya iptal edildi.
* `488 Not Acceptable Here / Burada Kabul Edilmez` – Talep URL’si oturum tanımının bazı yönleri kabul edilmez.
* `489 Bad Event / Kötü Olay` - Sunucu, Olay başlığı alanında belirtilen bir olay paketini anlamadı.
* `491 Request Pendin/ Talep Beklemede` – Sunucuda aynı diyalogdan birkaç bekleyen talep var.
* `493 Undecipherable / Deşifre Edilemiyor` – Deşifre Edilemiyor Talebi, alıcının deşifre edemediği şifrelenmiş bir MIME gövde metni içerir.
* `494 Security Agreement Required / Güvenlik Anlaşması Gerekli` – Sunucu, müzakere edilmiş bir güvenlik mekanizması gerektiren bir talep aldı.

## 5xx = Server errors / Sunucu hataları :

* `500 Server Internal Error / Dahili Sunucu Hatası` – Bazı beklenmeyen koşullar nedeniyle sunucu talebi yerine getiremedi.
* `501 Not Implemented / Uygulanmadı` – SIP talep yöntemi burada uygulanmaz.
* `502 Bad Gateway / Geçersiz Ağ Geçidi` – Sunucu bir talebi yerine getirmeye çalışırken, alt sistemdeki bir sunucudan geçersiz bir cevap aldı.
* `503 Service Unavailable / Hizmet Kullanılamıyor` – Sunucu bakımda veya geçici olarak aşırı yükleme vardır, talep işlenemiyor.
* `504 Server Time-out / Sunucuda Zaman Aşımı` – Sunucu bir talebi işlemeye çalışırken başka bir sunucuya erişmeye çalıştı, zamanında cevap veremedi.
* `505 Version Not Supported / Sürüm Desteklenmiyor` – Talepteki SIP protokolü sürümü sürücü tarafından desteklenmiyor.
* `513 Message Too Large / Mesaj Çok Fazla` – Talep mesaj uzunluğu, sürücünün işleyebileceğinden daha uzundur.
* `555 Push Notification Service Not Supported / Anlık Bildirim Hizmeti Desteklenmiyor` – Sunucu, pn sağlayıcı URL parametresinde belirtilen anlık bildirim hizmetini desteklemiyor.
* `580 Precondition Failure / Ön Koşul Geçersizliği` – Sunucu, teklifte belirtilen bazı sınırlamaları karşılayamıyor veya karşılamak istemiyor.

## 6xx = Global failures / Global olarak yerine getirilemeyenler:

* `600 Busy Everywhere / Her Yer Meşgul` – Tüm olası hedefler meşguldür.
* `603 Decline / Reddedilme` – Hedef, aramaya katılamıyor veya katılmak istemiyor; alternatif hedef bulunmuyor.
* `604 Does Not Exist Anywhere / Hiçbir Yerde Bulunmuyor` – Talep edilen kullanıcının hiçbir yerde bulunmadığına dair sunucunun yetkisel bilgisi mevcuttur.
* `606 Not Acceptable  / Kabul Edilemez` – Kullanıcının temsilcisine başarıyla ulaşıldı ancak oturum tanımının bazı yönleri kabul edilmedi.
* `607 Unwanted / İstenmedi` – Aranan taraf, arayan tarafın aramasını istemedi. Arayan tarafın gelecekteki girişimlerinin de benzer şekilde reddedilmesi muhtemeldir.
