## echo Komutu


Tabir-i caizse "Merhaba Dünya" programlamada bir klasiktir ve öğrenme aşamasında sık sık kullanılır. Bu programı birkaç farklı şekilde yazmak mümkündür. Bash komut satırı arayüzü kullanarak bunu gerçekleştirmek için echo komutunu kullanabilirsiniz.

echo komutu, terminal penceresindeki metni yazdırmak için kullanılır. Bu komut, argüman olarak verilen metni ekrana yazdırır. echo komutunun genel formatı şöyledir:

echo [OPTION] [STRING] 

OPTION seçeneklerine, birazdan ayrıntılı olarak bakacağız, ancak STRING bir zorunlu argümandır. Bu, yazdırmak istediğiniz metnin kendisidir.

Örneğin, aşağıdaki komutu çalıştırdığınızda "Merhaba Dünya" metni ekrana yazdırılacaktır:

echo "Merhaba Dünya" 
echo komutu, birden fazla argümanı birleştirmek için kullanılabilir. Aşağıdaki örnekte, birden fazla kelimeyi bir araya getirerek bir cümle oluşturuyoruz:

echo "Bu bir" "cümledir." 
 

Çıktı şöyle olacaktır:

Bu bir cümledir. 
echo komutu, bir değişkenin değerini yazdırmak için de kullanılabilir. Örneğin, aşağıdaki komut, $USER ortam değişkeninin değerini ekrana yazdırır:

echo $USER 
 

echo komutunun kullanabileceğiniz bazı seçenekleri de vardır. Bunlar şunlardır:

-   -n: Bu seçenek, echo komutunun normalde yaptığı gibi alt satıra geçmemesini sağlar. Bu seçeneği kullanarak metnin sonuna hiçbir şey eklenmez. Örneğin:

echo -n "Merhaba " echo "Dünya"

Bu örnekte, çıktı "Merhaba Dünya" olacaktır.

-   -e: Bu seçenek, echo komutunu kaçış dizilerini tanımak için etkinleştirir. Örneğin:

echo -e "Merhaba\nDünya" 
 

Bu örnekte, \n kaçış dizisi yeni bir satıra geçmek için kullanılır. Çıktı iki satırda görünecektir.

Bu, echo komutunun basit bir tanıtımıdır. Bu komutun daha gelişmiş özellikleri vardır ve bazı durumlarda kullanımı önerilmez. Ancak, öğrenme aşamasında bu komutun basit bir şekilde kullanımı, terminal penceresinde yazdırılan metni anlamak için oldukça