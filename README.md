# Linux, Asterisk, Python ve Django Komutları

Bu README dosyası, Linux, Asterisk, Python ve Django gibi teknolojilerle ilgili yaygın kullanılan komutları içermektedir.

## Linux Komutları

### Dosya ve Dizin İşlemleri

- Dizin içeriğini listeleme: `ls`
- Dizin değiştirme: `cd`
- Dizin oluşturma: `mkdir`
- Dosya veya dizin silme: `rm`
- Dosya veya dizin taşıma/kopyalama: `mv` / `cp`
- Dosya içeriğini görüntüleme: `cat`
- Dosya oluşturma: `touch`

### Paket Yönetimi

- Paket güncelleme: `sudo apt update`
- Paket yükleme: `sudo apt install`
- Paket kaldırma: `sudo apt remove`
- Paket arama: `sudo apt search`

## Asterisk Komutları

- Asterisk'i başlatma: `asterisk -rvvvv`
- Bir dahili aramak: `dialplan extension_number`
- Bir dış numarayı aramak: `dial SIP/external_number`
- Bir çağrıyı sonlandırmak: `hangup channel`

## Python Komutları

- Python kodunu çalıştırma: `python script.py`
- Python paketi kurma: `pip install`
- Python paketi güncelleme: `pip install --upgrade`
- Python paketi kaldırma: `pip uninstall`

## Django Komutları

- Django projesi oluşturma: `django-admin startproject project_name`
- Django uygulaması oluşturma: `python manage.py startapp app_name`
- Django geliştirme sunucusunu başlatma: `python manage.py runserver`
- Django modeli veritabanına uygulama: `python manage.py makemigrations` ve `python manage.py migrate`
- Django yönetici hesabı oluşturma: `python manage.py createsuperuser`

---

Bu README dosyası, sürekli olarak güncellenen bir kaynak olarak kullanılabilir. Siz de kendi komutlarınızı ekleyerek veya dökümanınızı istediğiniz gibi özelleştirerek kullanabilirsiniz.

