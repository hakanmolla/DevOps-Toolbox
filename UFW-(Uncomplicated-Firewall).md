## UFW (Uncomplicated Firewall), 

Ubuntu ve diğer Debian tabanlı işletim sistemlerinde kullanılan bir firewall yönetim aracıdır. UFW, IP tabanlı bir firewall kurulumunu
basitleştirir ve kullanıcıların IP tabanlı trafiği kontrol etmelerine olanak tanır. UFW, Ubuntu 8.04 ve sonraki sürümlerde varsayılan olarak yüklüdür.

UFW, arka planda iptables ile çalışır ve kullanıcıların iptables kurulumunu daha kolay bir şekilde yönetmelerini sağlar. UFW, iptables kurulumunun karmaşıklığını
gizler ve kullanıcıların birkaç temel komut kullanarak hızlı bir şekilde kurulum yapmalarını sağlar.

UFW'nin en yaygın kullanılan komutları şunlardır:

**UFW Kurulumu:**
```bash
sudo apt-get install ufw
```
 
**UFW'yi Etkinleştirme:**
```bash
sudo ufw enable 
 ```
**UFW'yi Devre Dışı Bırakma:**
```bash
sudo ufw disable
 ```
**Geçerli Durumu Görüntüleme:**
```bash
sudo ufw status
```
 
**Tüm Trafikleri Engelleme:**
```bash
sudo ufw default deny incoming
sudo ufw default deny outgoing
```
 
**Belirli Bir Portu Açma:**
```bash
sudo ufw allow <port number>/<optional: protocol>
 ```
**Örneğin:**, HTTP bağlantı noktasını açmak için:
```bash
sudo ufw allow 80/tcp
```
 

**Belirli Bir IP Adresini Engelleme:**
```bash
sudo ufw deny from <ip-address>
 ```
**Örneğin:**, IP adresi 192.168.1.100'ü engellemek için:
```bash
sudo ufw deny from 192.168.1.100
  ```
 

**Belirli Bir IP Adresine İzin Verme:**
 ```bash
sudo ufw allow from <ip-address>
   ```
**Örneğin:**, IP adresi 192.168.1.100'ye izin vermek için:
  ```bash
sudo ufw allow from 192.168.1.100
  ```
 

**Belirli Bir IP Adresindeki Belirli Bir Porta İzin Verme:**
  ```bash
sudo ufw allow from <ip-address> to any port <port number>/<optional: protocol>
  ```
 
**Örneğin**, IP adresi 192.168.1.100'deki HTTP bağlantı noktasına izin vermek için:
  ```bash
sudo ufw allow from 192.168.1.100 to any port 80/tcp
  ```


UFW, IP tabanlı trafiği yönetmenin basit bir yoludur ve Linux sunucularında önemli bir güvenlik aracıdır. Yukarıdaki komutlar, UFW'yi başlatmak için yararlıdır ve 
bu makale, bir Ubuntu sunucusunda UFW'nin nasıl kullanılacağına dair temel bilgiler sağlar
