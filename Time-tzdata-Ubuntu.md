# TZDATA PAKETİ KURULUMU

- Bu rehber, Ubuntu üzerinde `tzdata` paketini kurmak için adımları içermektedir. `tzdata` paketi, sistem saat dilimini ayarlamak için kullanılır.

## Adım 1: Paketleri Güncelleme

- Öncelikle sistemdeki paketleri güncelleyerek başlayalım. Aşağıdaki komutları sırasıyla çalıştırın:

```sh
sudo apt update
sudo apt upgrade -y

```


 ##  Adım 2: tzdata Paketini Kurma
 
- tzdata paketini kurmak için aşağıdaki komutu kullanabilirsiniz:

```sh
sudo apt install tzdata -y
```



 ## Adım 3: Zaman Dilimini Ayarlama
 
- tzdata paketi kurulduktan sonra, zaman dilimini ayarlamak için aşağıdaki komutu çalıştırabilirsiniz:

```sh
sudo dpkg-reconfigure tzdata

```

Bu komutu çalıştırdığınızda, bir grafik kullanıcı arayüzü (GUI) ortaya çıkacaktır. Bu arayüzde saat dilimini seçmek için ok tuşlarını kullanabilir ve Enter tuşuna 
basabilirsiniz. "Europe" bölgesini seçtikten sonra "Istanbul" saat dilimini seçin ve Enter tuşuna basın.
