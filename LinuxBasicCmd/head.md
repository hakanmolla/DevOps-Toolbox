## head Komutu


Taban olarak kullanılan bir Linux veya Unix sistemine sahip olan herkesin başına gelebilecek şeylerden biri, dosyaların içeriğinin okunması gerektiğinde başa veya sona odaklanmasıdır. Bu tür durumlarda kullanılabilecek birkaç farklı seçenek var, ancak başlık komutu genellikle bu amaçlar için tercih edilen bir seçenektir. Başlık komutu, bir dosyanın başlangıcındaki belirli sayıda satırı yazdırmak için kullanılır.

Kullanımı oldukça basittir. Temel kullanımı şu şekildedir:

head [seçenekler] [dosya adı] 
 

Burada [seçenekler] başlığı nasıl yazdıracağını belirlerken, [dosya adı] yazdırılacak dosyanın adıdır. Varsayılan olarak, head komutu ilk 10 satırı yazdırır, ancak seçeneklerle bu sayı değiştirilebilir.

-n seçeneği, yazdırılacak satır sayısını belirlemenizi sağlar. Örneğin, -n 5 seçeneği, sadece ilk 5 satırın yazdırılmasını sağlar.

Ayrıca, head komutu birden fazla dosya adı ile de kullanılabilir. Bu durumda, head komutu tüm dosyaların başlık bilgilerini sırayla yazdırır. Örneğin:

head file1.txt file2.txt file3.txt 
 

Bu komut, file1.txt dosyasının başlığını, ardından file2.txt dosyasının başlığını ve son olarak file3.txt dosyasının başlığını yazdırır.

-v seçeneği, head komutunu, dosya adlarını ve her dosyanın başlığından önce dosya adını yazdırmak için kullanabilirsiniz. Örneğin:

head -v file1.txt file2.txt 
 

Bu komut, file1.txt ve file2.txt dosyalarının başlıklarını sırayla yazdırmadan önce her dosya adını da yazdırır.

Son olarak, head komutu ile bir dizinin tüm dosyalarının başlık bilgilerini yazdırabilirsiniz. Bu, tüm dosyaların başlıklarını tek bir çıktıda görmenizi sağlar. 

**Örneğin:**

head * 
 

Bu komut, bulunduğunuz dizindeki tüm dosyaların başlıklarını sırayla yazdırır.

Bu şekilde, head komutunun kullanımı oldukça basittir ve bir dosyanın başlangıcındaki belirli bir sayıda satırın yazdırılmasını gerektiğinde oldukça faydalıdır.