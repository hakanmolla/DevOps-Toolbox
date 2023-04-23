# Linux'da Servis Oluşturma

Merhaba! Linux'ta kendi özel servisinizi oluşturmak mı istiyorsunuz? Harika! Aşağıda, Linux sisteminizde bir Python betiğini servis olarak çalıştırmak için nasıl 
bir yapılandırma yapabileceğinizi adım adım öğreneceksiniz. Hadi başlayalım

## Adım 1: Servis Dosyası Oluşturma

Öncelikle, yeni bir servis dosyası oluşturacağız. Servis dosyası, servisinizin çalışma düzenini ve yapılandırmasını belirleyen bir yapıdır. Bir metin düzenleyici kullanarak **/etc/systemd/system/** dizin içine  aşağıdaki içeriği içeren bir dosya oluşturun ve `.service` uzantısı ekleyerek dosyaya bir isim verin: 

```bash

sudo vim /etc/systemd/system/myservice.service




[Unit]
Description=My Awesome Service
After=network.target

[Service]
User=myuser
Group=mygroup
ExecStart=/usr/bin/python3 /path/to/myscript.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```



**Description:** Servisiniz için heyecan verici bir açıklama metni yazın! 
**After:** Servisinizin ne zaman başlamasını istediğinizi belirleyin. Örneğin, network.target ağ hizmetlerinin başlamasını beklemek için kullanılabilir.
**User ve Group:** Servisinizin hangi kullanıcı ve grup kimlikleri ile çalışacağını belirleyin.
**ExecStart:** Servisinizin başlatılmasını tetikleyen komut veya betiği belirtin.
**Restart ve RestartSec:** Servisinizin otomatik olarak yeniden başlatılması gerektiğinde ne zaman ve nasıl yeniden başlatılacağını belirleyin.
**WantedBy:** Servisinizin hangi hedefe bağlanacağını belirleyin. multi-user.target genellikle kullanıcı modunda çalışan hedeftir.

##  Adım 2: Servis Dosyasını Kaydetme ve İzinlerini Güncelleme

Servis dosyasını kaydetme ve izinlerini güncelleme zamanı geldi! Servis dosyasını kaydedin ve ardından izinlerini güncelleyin:
```bash
sudo chmod 644 /etc/systemd/system/myservice.service
```
## Adım 3: Systemd'ye Servisi Tanıtma

Şimdi, oluşturulan servis dosyasını Systemd'ye tanıtarak yapılandırmayı yeniden yükleyeceğiz:
```bash
sudo systemctl daemon-reload
```

## Adım 4: Servisi Başlatma ve Etkinleştirme

```bash
sudo systemctl start myservice.service
```

Artık betiğiniz, oluşturulan servis dosyası aracılığıyla Linux sisteminizde bir servis olarak çalıştırılacaktır. Servisi durdurmak, yeniden başlatmak veya 
durumunu kontrol etmek için systemctl komutunu kullanabilirsiniz. Örneğin:

```bash
sudo systemctl stop myservice
sudo systemctl restart myservice
sudo systemctl status myservice
```

Artık servisimizi başlatabilir ve etkinleştirebiliriz: Kolay Gelsin 😎
