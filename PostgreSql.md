## Postgresql setup 

```bash
sudo apt update 
```

```bash 
sudo apt upgrade -y 
```

```bash 
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
```

```bash 
sudo apt-get update
```

```bash 
sudo apt-get -y install postgresql
```
```bash 
systemctl status postgresql.service
```
- Veritabanı etc altında dosyasına gidiniz. postgresql.conf dosyasında listen_Addresses satını değiştirin bu adım erişim için gerekli


```bash 
cd /etc/postgresql/veritabanı sürümü/main/postgresql.conf

```

```bash 
listen_addresses='*'
```
-  Veritabanı etc altında dosyasına gidiniz.pg_hba.conf dosyasının altın aşağıdaki satırı ekleyiniz.


```bash 
host all all 0.0.0.0/0 md5

```
**------------------------------------Database && Kullanıcı Ayarları && Yetkileri--------------------------------------------------------------------**
- **sudo -u postgres psql** komutu ile postgresql giriş yapınız.
- **\l** bu komut Databasse listesini gösteriyor
- **\du** bu komut Kullanıcı listesini gösteriyor

- Kullanıcı Oluşturmak için 
```bash 
CREATE ROLE User_name WITH LOGIN SUPERUSER CREATEDB CREATEROLE REPLICATION BYPASSRLS PASSWORD 'User_password';

```
- Database oluşturmak için 
```bash 
 CREATE DATABASE asterisk;
```
 
 - Kullanıcın Database
  yetkisi için 

```bash 
GRANT ALL PRIVILEGES ON DATABASE db_name TO user_name;
```

- Kullanıcnın Database sahiplik hakkı için 
```bash
 ALTER DATABASE asterisk OWNER TO molla;
 ```