# SIP Yanıt Kodları

## 1xx = bilgi içerikli yanıtlar

- **100 Deniyor**
- **180 Çalıyor**
- **181 Arama Yönlendiriliyor**
- **182 Sıraya Alındı**
- **183 Oturum Devam Ediyor**

## 2xx = başarı yanıtları

- **200 TAMAM**
- **202 Kabul Edildi: Göndermeler için kullanılır**

## 3xx = yeni adrese yönlendirme yanıtları

- **300 Çoklu Seçenekler**
- **301 Kalıcı Olarak Yeri Değişti**
- **302 Geçici Olarak Yeri Değişti**
- **305 Proxy Kullan**
- **380 Alternatif Servis**

## 4xx = talebin yerine getirilememesi

- **400 Geçersiz Talep**
- **401 Yetki Dışı Kullanım: Sadece kayıt hizmeti verenler tarafından kullanılır Proxy’ler, proxy yetkilendirmesi için 407’yi kullanmalıdır**
- **402 Ödeme Gerekiyor (gelecekte kullanılmak üzere ayrılmıştır)**
- **403 Yasak**
- **404 Bulunamadı: Kullanıcı bulunamadı**
- **405 İzin Verilmeyen Yöntem**
- **406 Kabul Edilemez**
- **407 Proxy Kimlik Doğrulanması Gerekiyor**
- **408 Talep Zaman Aşımı: Kullanıcı gerekli süre içerisinde bulunamadı**
- **410 Gitmiş: Bir zamanlar var olan bu kullanıcı artık burada yok**
- **413 Talep Çok Büyük**
- **414 Talep-URI Çok Uzun**
- **415 Desteklenmeyen Medya Tipi**
- **416 Desteklenmeyen URI Şeması**
- **420 Geçersiz Uzantı: Geçersiz SIP Protokol Uzantısı kullanıldı, sunucu tarafından anlaşılmadı**
- **421 Uzantı Gerekiyor**
- **423 Ara Çok Kısa**
- **480 Geçici Olarak Ulaşılamıyor**
- **481 Arama/İşlem Mevcut Değil**
- **482 Döngü Tespit Edildi**
- **483 Çok Fazla Sayıda Sekme**
- **484 Eksik Adres**
- **485 Belirsiz**
- **486 Burası Meşgul**
- **487 Talep Sona Erdirildi**
- **488 Burada Kabul Edilemez**
- **491 Talep Beklemede**
- **493 Deşifre Edilemiyor: S/MIME metni deşifre edilemiyor**

## 5xx = sunucu hataları

- **500 Dahili Sunucu Hatası**
- **501 Geçerli Değil: SIP talep metodu burada geçerli değildir**
- **502 Geçersiz Ağ Geçidi**
- **503 Hizmet Sunulamamaktadır**
- **504 Sunucu Zaman Aşımı
