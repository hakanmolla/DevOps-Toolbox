## Postgresql Odbc & Asterisk Odbc Config

```bash
sudo apt update 
```

```bash 
sudo apt upgrade -y 
```

```bash 
 apt install odbc-postgresql
```

```bash 
apt install unixodbc
```

- etc/odbc.ini dosyaısnı içinde adaptör ayarlarını giriniz. 

```bash 
vim etc/odbc.ini
```

- odbc.ini dosyasını aşağıdaki metini ekleyiniz. 

```bash 
[Asterisk]
Description=PostgreSQL ODBC driver for Unicode
Driver=PostgreSQL Unicode
Username= Kullanıcı_Adı
Database= Db_Adı
Servername= Server_Adresi
Port=5432
PASSWORD=Kullanıcı_password
```
- bağlantı testi yapısınız lütfen 

```bash

isql -v MyPostgreSQLUnicode


BU cıktığı görüyorsanız bağlantı başarıdır. 
+---------------------------------------+
| Connected!                            |
|                                       |
| sql-statement                         |
| help [tablename]                      |
| quit                                  |
|                                       |
+---------------------------------------+
SQL>
```
## Asterisk Config 

-  res_odbc.conf dosyasını içine giriniz. 
```bash 
vim  res_odbc.conf 
```
- aşağıdaki metini yazınız. 


```bash 
[asterisk]
enabled => yes
dsn => ast
username => Kullanıcı_adı 
password => Kullanıcı Şifresi
pre-connect => yes
sanitysql => select 1
max_connections => 20
connect_timeout => 5
negative_connection_cache => 600
```
- Asterisk yeniden başlatmanız gerekiyor. 

```bash 
asterisk -rx "core restart now"
```

- daha sonra Asterisk bağlantısını kontrol etmek için asterisk Clı giriş yapalım
```bash 
asterisk -vvvrrrr
```
```bash 
 odbc show
 ```

- odbc show komutunda sonra aşğıdaki bağlantıyı gördüğünüzde işlem tamamlanmıştır. 

```bash 
 ODBC DSN Settings
-----------------

  Name:   asterisk
  DSN:    ast
    Number of active connections: 1 (out of 20)
    Logging: Disabled

 ```

