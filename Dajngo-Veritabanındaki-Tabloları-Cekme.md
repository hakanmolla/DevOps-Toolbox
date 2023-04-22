## Django Veritabanı Tablolarını Otomatik Olarak Modele Dökme

Django, varolan bir veritabanındaki tabloları otomatik olarak modele döken "inspectdb" adlı bir yönetim komutu içermektedir. Bu komut, veritabanındaki tablolara karşılık gelen Django modellerini otomatik olarak oluşturmanıza olanak tanır. Bu, varolan bir veritabanını Django projesine entegre etmek istediğinizde oldukça kullanışlıdır.

İşte "python manage.py inspectdb > models.py" komutunu kullanarak veritabanı tablolarını modele döken bir örnek:

Django projesinizin ana dizininde komut satırını açın.

***Aşağıdaki komutu girin:**

```bash
python manage.py inspectdb > models.py
```


Bu komut, "inspectdb" yönetim komutunu kullanarak veritabanındaki tabloları modele döker ve sonuçları "models.py" adlı bir dosyaya yazar.

Şimdi "models.py" dosyasını açın ve otomatik olarak oluşturulan Django modellerini inceleyin. Her bir veritabanı tablosu için bir model oluşturulmuş olmalıdır.
Örneğin, veritabanındaki "users" adlı bir tablo için aşağıdaki gibi bir model oluşmuş olabilir:

```bash


from django.db import models

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'
        
 ```
        
Bu model, "Users" adında bir Django modelini temsil eder ve "users" adlı veritabanı tablosuna karşılık gelir. Modelde, tablonun alanları ("id", "username", "email", "password") ve bunların veri türleri (örneğin, "CharField" ve "IntegerField") bulunur.

"models.py" dosyasındaki modelleri projenizin ilgili uygulamalarına ekleyerek veritabanı tablolarınızı Django projenize entegre edebilirsiniz.
Bu, "python manage.py inspectdb > models.py" komutunu kullanarak veritabanı tablolarını modele dökme işlemini basit bir örnek olarak anlatan bir makaledir. Bu yöntemle, varolan bir veritabanınızı Django projenize kolayca entegre edebilir ve Django modellerini kullanarak veritabanı işlemlerini gerçekleştirebilirsiniz.
