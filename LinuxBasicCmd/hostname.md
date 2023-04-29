## hostname Komutu


hostname komutu, Linux veya Unix sistemlerinde kullanılan ve bilgisayarın adını (hostname) görüntülemeye veya ayarlamaya yarayan bir komuttur. Bu komut, aynı zamanda ağ yapılandırması ve yönetimi sırasında da kullanılabilir.

Komutu kullanarak, bir terminal penceresinde veya bir komut dosyasında, sistemdeki bilgisayarın adını sorgulayabilir veya ayarlayabilirsiniz.

Kullanımı oldukça basittir. Terminalde sadece hostname komutunu yazarak, bilgisayarın adını görebilirsiniz. Eğer bilgisayarın adını değiştirmek istiyorsanız, hostname komutunu, yeni adı belirterek kullanabilirsiniz.

**Örneğin:**

hostname mycomputer 
 

yukarıdaki örnekte, "mycomputer" adlı yeni bir hostname tanımlandı. Daha sonra, bu yeni adı kullanarak sistemle etkileşime geçebilirsiniz.

Ayrıca, -i parametresi kullanılarak, bilgisayarın IP adresini de görüntüleyebilirsiniz. Örneğin:

hostname -i 
 

yukarıdaki örnekte, sistemdeki bilgisayarın IP adresi görüntülenir.

Bu komutun diğer parametreleri arasında -s (short), -f (full) ve -d (domain) gibi seçenekler de bulunmaktadır. Bu seçenekler, komutun çıktısının farklı şekillerde formatlanmasına ve bilgisayar adının farklı bileşenlerine erişmenize olanak tanır.

Özetle, hostname komutu, Linux ve Unix sistemlerindeki bilgisayar adını sorgulamak ve ayarlamak için kullanışlı bir araçtır