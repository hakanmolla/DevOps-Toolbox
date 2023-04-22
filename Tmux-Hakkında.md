## Linux'da tmux Komutları - Terminalde Oturum Yönetimi**

# Ubuntu Setup 

**sudo apt-get update**

**sudo apt-get install tmux**

## Giriş:
Linux'ta terminal oturum yönetimi, kullanıcıların birden fazla pencere veya oturumda çalışmasına olanak tanır ve tmux (terminal multiplexer) bu amaca hizmet eden güçlü bir araçtır. Tmux, birden fazla terminal penceresi, paneller (split windows) ve seanslar (sessions) oluşturarak, terminalde çoklu görevler gerçekleştirmeyi sağlar. İşte tmux komutlarını kullanarak tmux'u kullanmaya başlamanıza yardımcı olacak bir rehber:

# Tmux'u Başlatma:
Tmux'i başlatmak için terminalde tmux komutunu kullanabilirsiniz. Tmux başladığında, varsayılan olarak bir oturum (session) oluşturulur ve tek bir pencere (window) ile açılır.
Komut: tmux

# Oturum Yönetimi:
Tmux'ta oturumlar, birden fazla pencereyi ve panelleri bir araya getiren en üst düzey yapıdır. Oturumları oluşturabilir, listeyebilir, yeniden adlandırabilir ve aralarında geçiş yapabilirsiniz.
Oturum Oluşturma:
Yeni bir oturum oluşturmak için tmux new-session komutunu kullanabilirsiniz.
Komut: **tmux new-session** -s <oturum_adı>

Örneğin: **tmux new-session -s mysession** komutu, "mysession" adında bir oturum oluşturacaktır.

# Oturumları Listeleme:
Açık oturumları listelemek için tmux ls veya tmux list-sessions komutunu kullanabilirsiniz.
Komut: **tmux ls**

# Oturum Arasında Geçiş Yapma:
Birden fazla oturum arasında geçiş yapmak için tmux switch-client veya kısa haliyle tmux switch komutunu kullanabilirsiniz.
Komut:** tmux switch-client -n **(sonraki oturuma geçmek için)
Komut:** tmux switch-client -p** (önceki oturuma geçmek için)

# Pencere Yönetimi:
Pencereler, tmux içinde çalışan farklı uygulamaları temsil eder ve birden fazla pencere oluşturabilir, yeniden adlandırabilir, aralarında geçiş yapabilir ve pencereleri düzenleyebilirsiniz.
Yeni Pencere Oluşturma:
Yeni bir pencere oluşturmak için **Ctrl-b c** tuş kombinasyonunu kullanabilirsiniz.

# Pencere Arasında Geçiş Yapma:
Farklı pencereler arasında geçiş yapmak için **Ctrl-b n** (sonraki pencere), Ctrl-b p (önceki pencere) veya Ctrl-b l (son kullanılan pencere) tuş kombinasyonlarını
