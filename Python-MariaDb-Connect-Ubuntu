# MariaDB Veritabanına Bağlanma

## Gereksinimler

Öncelikle `libmariadb-dev` paketini sistemimize kurmalıyız:

```bash
sudo apt install libmariadb-dev
```

Daha sonra mariadb Python modülünü pip3 kullanarak yükleyebiliriz:

```bash
pip3 install mariadb
```


## Örnek Kod

```bash

import sys
import mariadb

try:
    # MariaDB veritabanına bağlanma
    con = mariadb.connect(
        user="username",
        password="password",
        host="localhost",
        port=3306,
        database="asterisk"
    )
except mariadb.Error as ex:
    print(f"MariaDB'ye bağlanırken bir hata oluştu: {ex}")
    sys.exit(1)

# Veritabanı adını görüntüleme
print("Bağlanılan veritabanı: ", con.database)

# Bağlantıyı kapatma
con.close()

print("Bağlantı kapatıldı.")


```


Bu kod örneğinde, Python kullanarak MariaDB veritabanına bağlanma işlemi gösterilmektedir. "username" kullanıcı adı, "password" şifresi, "localhost" host adresi, 
3306 port numarası ve "DB_NAME" veritabanı adı ile bir bağlantı kurulmaktadır. Bağlantı başarılı olursa, kullanılan veritabanının adı ekrana yazdırılır 
ve bağlantı kapatılır.

Umarım bu örnekle .md uzantısı için istediğiniz okunaklı formata ulaşmışsınızdır. Eğer eklemek istediğiniz başka bir şey varsa, lütfen belirtin, yardımcı olmaktan mutluluk duyarım!
