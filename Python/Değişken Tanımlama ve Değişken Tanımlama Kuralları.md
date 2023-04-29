## Değişken Tanımlama ve Değişken Tanımlama Kuralları


 

Değişken tanımlama işlemi her yazılım dilinde çok önemlidir. Değişkenler, kullanıcı tarafından verilen uzun ifadeleri, bir matematik işleminin sonucunu veya bir fonksiyondan dönen sonuçları tutmak için kullanılır. Değişken tanımlama sırasında dikkat edilmesi gereken ve en çok sorulan soruların cevapları aşağıdaki gibidir.

Değişken İsimleri Nasıl Olmalıdır? Değişken isimleri, lütfen okunaklı ve gerekirse uzun olsun. Bunun en büyük nedeni, yazdığınız kodu sadece sizin okumayacağınız, sizden başka insanların da okuyacağı ve anlaması için değişken isimlerinizin okunaklı olması gerektiğidir. Örneğin, "x" diye bir değişken tanımladığınızda, bu "x" nedir sorusunu kodu okuyan kişinin sormasına izin vermeyin. "first_name" diye bir değişken tanımlarsanız, okuyan kişi bu değişkenin ne olduğunu hemen anlar ve bir ekip çalışmasında sizin zamanınızı alacak sorular sormaz.

Değişken Tanımlama Türleri:

camelCase: değişkenin ilk harfi küçük ve diğer kelimenin baş harfi büyük yazılır (örneğin, userName).
PascalCase: değişken isimlerinin ilk harfleri büyük yazılır (örneğin, UserName).
kebab-case: değişken isimleri küçük harfle yazılır ve araya "-" koyulur (örneğin, user-name).
snake_case: değişken isimleri küçük harfle yazılır ve araya "_" koyulur (örneğin, user_name).
Değişken İsimleri İngilizce mi Olmalı?

Değişken isimleri İngilizce olmak zorunda değil, ancak yazılımın aslında bir dil olduğunu unutmamak gerekir. Kodunuzun uluslararası okunabilirliği ve dünyanın her yerinde çalışabilmesi için değişken isimlerini İngilizce olarak tanımlamanız önerilir.

Değişken İsimleri Rakamla Başlayabilir mi?

Değişken isimleri rakamla başlayamaz, bir harfle başlayıp harfle devam edebilir veya harfle başladıktan sonra rakamla devam edebilir.

Değişken İsimleri Büyük Harfle Yazılabilir mi?

Zorunlu bir kural değildir, ancak kodunuzda bir kere sabit olarak tanımlanacak ve programın hiçbir yerinde değişmeyecek bir değişkeniniz varsa büyük harfle yazmanız önerilir. Örneğin,

Değişken isimleri büyük harfle yazılabilir mi? Zorunlu bir kural olmasa da, kodunuzda sabit olarak tanımlanacak ve programın hiçbir yerinde değişmeyecek bir değişkeniniz varsa, bu durumda büyük harfle yazmanızı tavsiye ederim. Örneğin, SERVER_IP = "127.0.0.1" gibi.

Değişken isimleri birden fazla kez kullanılabilir mi?

Evet, kullanılabilir, ancak dikkat edilmesi gereken şey, Python'un dinamik bir dil olmasıdır. Yukarıdan aşağıya çalıştığından, değişkeni birden fazla kez kullandığınızda, içinde bir değer varsa o değer silinecektir. Bu nedenle, mümkünse kullanmamanızı öneririm.

Değişken isimlerini büyük harfle yazmakla küçük harfle yazmak arasındaki fark var mı?

Yazım kurallarında, tüm dünyanın kabul ettiği bazı kurallar vardır ve bu kurallara uymak istiyorsanız dikkat etmeniz gerekmektedir. Büyük harfle yazılan değişkenler, sunucu bilgileri veya ayar değişkenleri gibi görünebilir ve bir kere tanımladıktan sonra daha fazla tanımlama gibi okunabilirliği sağlamak için kabul edilen tanımlardır. Ancak, bu zorunlu değildir.

Değişken isimleri büyük harfle (USER_NAME) ve küçük harfle (user_name) yazılsa da aynı sonucu alır mıyız?

Değişken tanımlarken büyük küçük harf uyumluluğu vardır. USER_NAME ve user_name aslında farklı iki değişken anlamına gelir, bu nedenle tek bir harf bile büyük yazsanız tamamen farklı bir değişken olacaktır ve bunu üzerine aynı sonuçları alamazsınız.

Not: Değişken tanımlama işlemleri genel olarak bir kültür gibidir. O dili yazan kişilerin kendi aralarında uyguladıkları ve kodu yazan kişinin o dile ne kadar önem verdiğini, bu dile ne kadar hakim olduğunu anlayabildikleri bir kültür gibi düşünebilirsiniz.

Örneğin, JavaScript kodu yazan insanlar genellikle camelCase tarzı kod yazarlar, ancak Python'da snake_case yapısı kullanılır. Python'da yazılan bir kodda çok fazla CamelCase yapısını görürlerse, bu kodu yazan kişinin JavaScript'ten geldiğini anlarlar. :)