## tail Komutu


tail komutu, bir dosyanın son birkaç satırını veya sürekli olarak değişen bir dosyanın son kısmını görüntülemek için kullanılır. Adı, "kuyruk" anlamına gelen "tail" kelimesinden gelir, çünkü bir dosyanın sonunda olan verileri görüntüler.

Temel olarak, tail komutu bir dosyanın son kısmını görüntüler ve bunu yapmak için iki ana parametre alır:

-n veya --lines: Bu parametre, görüntülenecek satır sayısını belirler. Örneğin, tail -n 10 komutu, dosyanın son 10 satırını görüntüler.

-f veya --follow: Bu parametre, dosyanın sonuna eklenen herhangi bir veriyi gerçek zamanlı olarak görüntülemek için kullanılır. Örneğin, tail -f /var/log/syslog komutu, syslog dosyasına eklenen her yeni satırı ekranda gösterir.

## Bunların yanı sıra, tail komutu bazı diğer seçenekler de alır:

-   -c veya --bytes: Bu parametre, görüntülenecek byte sayısını belirler. Örneğin, tail -c 100 komutu, dosyanın son 100 byte'ını görüntüler.

-   -q veya --quiet: Bu parametre, dosyanın adını görüntülemeden sadece içeriği görüntüler.

-   -v veya --verbose: Bu parametre, dosyanın adını görüntüler.

**Örnek kullanımlar:**

-   tail myfile.txt: myfile.txt dosyasının son 10 satırını görüntüler.

-   tail -n 20 myfile.txt: myfile.txt dosyasının son 20 satırını görüntüler.

-   tail -f /var/log/syslog: syslog dosyasına eklenen her yeni satırı gerçek zamanlı olarak görüntüler.

-   tail -c 100 myfile.txt: myfile.txt dosyasının son 100 byte'ını görüntüler.

-   tail -q myfile.txt: Sadece myfile.txt dosyasının içeriğini görüntüler.