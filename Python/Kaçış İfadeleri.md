## Kaçış İfadeleri:


 

String ifadelerini ekrana yazarken bazen kaçış ifadelerine ihtiyaç duyarız. Bildiğiniz üzere Python string ifadelerini tırnaklar içerisinde yazıyoruz ve açılan tırnağın kapanışını arıyor. Siz string ifadenin açılışını çift tırnak ile yaptınız fakat cümle içerisinde çift tırnak kullanmanız gerekiyor. Bu durumda kaçış ifadelerini kullanabilirsiniz. Ters taksim (") işareti kendisinden sonra gelen tırnağın Python aradığı kapatma tırnağı olmadığını söylüyor. Bunun dışında Python bize sunduğu bazı özel kaçış ifadeleri bulunmaktadır. Aşağıdaki gibidir:

Kaçış ifadesi örneği-1: print(""Client" kelimesi Türkçede "Müşteri" anlamına gelir.")

Ekran Çıktısı: "book" kelimesi Türkçede "kitap" anlamına gelir.

\n = Ekrana yazdırdığınız ifadeyi alt satırda indirerek yazmaya devam eder.

\enter tuşu = Programı alt satırdan devam etmek üzere okumaya devam eder.

\t = Tap kadar boşluk verir. \a = Kaçış sesinde bir bib sesi çalar. Bir uyarıcı olarak kullanılabilir.

\r = Python bu işareti gördüğü zaman imleci satır başına koyacaktır ve bundan önceki metinleri ekrana silip

\r den sonraki yazıları satır başından yazmaya devam edecektir.

\v = Python bu işareti gördüğünde düşey sekme dediğimiz şeyi yapacaktır.

\b = İmleci bir adım sola kaydırır.

r= print(r"Kaçış dizileri: , \n, \t, \a, \, r") şeklinde kullanıldığında kaçış dizileri etkisiz hale getirilir.

 

\' : Tek tırnak işareti (') kullanımı için kaçış ifadesidir. Örneğin: print('Python\'da kaçış ifadeleri kullanılır.')

\" : Çift tırnak işareti (") kullanımı için kaçış ifadesidir. Örneğin: print("Python'da kaçış ifadeleri kullanılır.")

\\ : Ters bölü işareti (\) kullanımı için kaçış ifadesidir. Örneğin: print("Python dosya yolu belirlerken C:\\Users\\KullanıcıAdı\\Belgeler")

\n : Yeni satır karakteri ekler. Örneğin: print("Merhaba,\nDünya!")

\t : Sekme karakteri ekler. Örneğin: print("Adı\tSoyadı\tYaş\nAli\tKaya\t24\nAyşe\tYılmaz\t31")

\b : Geri alma karakteri (backspace) ekler. Örneğin: print("Birkaç karakter silinir.\b\b\bpython")

\r : Satır başına döner ve metnin başından yazmaya başlar. Örneğin: print("Python\rData")

\a : Bilgisayarınızda varsayılan olarak tanımlanmış bir uyarı sesi çalar. Örneğin: print('\a')

\f : Sayfa atlaması yapar. Örneğin: print("Önceki sayfanın sonuna geldik.\fYeni sayfaya geçildi.")

\v : Dikey sekme karakteri ekler. Ancak bazı platformlar tarafından desteklenmeyebilir. Örneğin: print("Birkaç satır aşağıda.\vPython")

Bu kaçış ifadeleri, Python'da metinlerin işlenmesinde çok kullanışlıdır.