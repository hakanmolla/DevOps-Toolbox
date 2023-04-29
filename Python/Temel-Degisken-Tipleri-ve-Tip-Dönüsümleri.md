Temel Değişken Tipleri ve Tip Dönüşümleri:


 

Metinsel ifadeler -> str (tırnaklar içinde olan ifadeler metinsel ifadelerdir.)

Örneğin: First_name = "hakan"
Tam sayılar -> int (Matematikteki tam sayıları ifade eder)

Örneğin: Age = 33
Virgüllü Sayılar -> float (Matematikteki küsürlü sayıları ifade eder)

Örneğin: Fiyat = 12.4
True/False -> Boolean (True veya false değerini alır, yani evet/hayır, var/yok gibi ikilemlerde kullanılır)

Örneğin: Is_active = True
Metinden Tam Sayı Dönüşümü -> int fonksiyonunu kullanıyoruz, ancak burada dikkat etmemiz gereken şey, metin ifadesinin içinde harf veya özel karakter olmaması gerektiğidir. Sadece rakam olması gerekiyor.

Örneğin: age = "13"
Int(age) kullanarak, str bir ifadeyi int olarak çevirmiş olduk.
Virgüllü Sayıdan Tam Sayıya Dönüşümü: Bu dönüşümde yine int fonksiyonunu kullanıyoruz.

Örneğin: urun = 13.5
Tutar = int(urun) -> urun değerini, tutarın içinde bir tam sayı olarak aktardık.
Boolean Dönüşümü: bool(urun) -> Burada, bool dönüşümünde, urun adındaki değişkene bakıyor ve içinde bir değer varsa True, yoksa False olarak bize geri dönüş yapıyor.

Boolean Anlamak ve Karşılaştırma Operatörleri ve Mantıksal Operatörler

Örnek 1: Burada, username içinde bilgi var mı diye kontrol ediyoruz. Bu örnekte, username içinde bilgi olmadığından False gerekecektir.

Örneğin: username = ""
Print(bool(username))
Örnek 2: Burada, age içinde bilgi var mı diye kontrol ediyoruz. Bu örnekte, age içinde bilgi olduğundan True gelecektir.

Örneğin: age = 10
Print(bool(age))
Örnek 3: Bu, eşit mi operatörüdür (==). Bu örnekte, yaş değeri 0'a eşit mi sorusunu soruyoruz ve True cevabı alıyoruz.

Örneğin: age = 0
Print(bool(age == 0)
Örnek -4: Burada eşit değil mi kullanımını görüyoruz. Eşit değil mi iki türlü kullanılıyor (!=) ya da (not) ifadesini kullanıyoruz. Age bilgisi 0 eşit değil mi sorusunun cevabı bize True gelecektir.

age = 25 print(age != 0) print(not age == 0)

Örnek -5: Burada "Büyüktür" operatörünün kullanımını görüyoruz. Age bilgisinin 18'den büyük olup olmadığını soruyoruz.

print(age > 18)

Örnek -6: Burada "Küçüktür" operatörünün kullanımını görüyoruz. Age bilgisinin 18'den küçük mü olup olmadığını soruyoruz.

print(age < 18)

Örnek -7: Burada "Küçük veya Eşit" operatörünün kullanımını görüyoruz. Age bilgisinin 18'den küçük veya eşit mi olup olmadığını soruyoruz.

print(age <= 18)

Örnek -8: Burada "Büyük veya Eşit" operatörünün kullanımını görüyoruz. Age bilgisinin 18'den büyük veya eşit mi olup olmadığını soruyoruz.

print(age >= 18)

Örnek -9: Burada aralık sorusunun kullanımını görüyoruz. Age bilgisinin 20 ile 30 arasında olup olmadığını soruyoruz.

age = 25 print(20 < age < 30)

Örnek -10: Burada "Büyük veya Eşit" operatörünün kullanımını görüyoruz. Age bilgisinin 18'den büyük veya eşit mi olup olmadığını soruyoruz.

print(age >= 18)

Örnek -11: "OR" (veya) kullanımı. Bu kullanımda şartlardan sadece bir tanesi doğru olması yeterlidir. Sonuç True dönecektir.

gender = "f" age = 10 print("Yasi 18'den büyük mü veya kadın mı? OR kullanımı:", age > 18 or gender == 'f')

Örnek -12'de "and" (ve) kullanarak iki koşulu da sağlamanın gerektiği belirtiliyor. En az bir koşul yanlış ise sistem "False" döndürür.

Kod bloğunda, "username" değişkeni boş olarak tanımlanmış ve "age" değişkenine 20 değeri atanmıştır. Ardından, "age > 18" ifadesi ve "bool(username)" ifadesi "and" operatörü ile birleştirilerek, "print" fonksiyonu kullanılarak ekrana yazdırılmıştır. Bu kod bloğu, "age" değişkeninin 18'den büyük olduğu ve "username" değişkeninin boş olmadığı durumlarda "True" sonucunu verecektir.