Asterisk Başlıca Conf Files


Asterisk'in yapılandırma dosyaları, sistem davranışını, işlemleri ve telekomünikasyon hizmetlerini yönetmek için kullanılır. İşte Asterisk'te kullanılan bazı önemli yapılandırma dosyaları ve nasıl kullanılacağına dair bir rehber:

-   sip.conf: Bu dosya, Session Initiation Protocol (SIP) kullanarak gelen ve giden çağrıları yapılandırmak için kullanılır. SIP, IP tabanlı sesli iletişim için bir protokoldür ve Asterisk'in temel protokolüdür. sip.conf dosyası, kullanıcıların SIP trafiğini yönlendirmek, kimlik doğrulama ayarlarını yapılandırmak, codec'leri ayarlamak, NAT (Network Address Translation) problemlerini çözmek ve diğer pek çok SIP özelliğini yapılandırmak için kullanılır.

-   extensions.conf: Bu dosya, Asterisk PBX'inin dahili numaralarını ve çağrı yönlendirmelerini yapılandırmak için kullanılır. extensions.conf dosyası, kullanıcıların dahili numaraları, çağrı grupları, çağrı kuyrukları, çağrı yönlendirmeleri, çağrı kaydetme ve diğer çağrı yönlendirme kurallarını yapılandırmalarına olanak tanır.

-   voicemail.conf: Bu dosya, Asterisk'teki sesli posta kutularını yapılandırmak için kullanılır. voicemail.conf dosyası, kullanıcıların sesli posta kutularını oluşturmak, sesli posta kutularını yönetmek, sesli posta kutusu ayarlarını yapılandırmak ve sesli posta mesajlarını e-posta veya başka bir yöntemle iletme gibi sesli posta özelliklerini yapılandırmalarına olanak tanır.

-   cdr.conf: Bu dosya, Asterisk'te çağrı kayıt verilerini (CDR) yapılandırmak için kullanılır. cdr.conf dosyası, kullanıcıların çağrı kaydı tutma ayarlarını yapılandırmak, çağrı kayıt verilerini hangi veritabanına veya dosyaya kaydetmek istediklerini ayarlamak ve diğer çağrı kayıt özelliklerini yapılandırmak için kullanılır.

-   meetme.conf: Bu dosya, Asterisk'teki konferans görüşmelerini yapılandırmak için kullanılır

-   queues.conf: Bu dosya, Asterisk'teki çağrı kuyruklarını yapılandırmak için kullanılır. queues.conf dosyası, kullanıcıların çağrı kuyruklarını oluşturmak, kuyruğa gelen çağrıların yönlendirilme kurallarını ayarlamak, çağrı kuyruğu üyelerini yapılandırmak, müzik ve çağrı bekleme özelliklerini ayarlamak ve diğer çağrı kuyruğu özelliklerini yapılandırmak için kullanılır.

-   logger.conf: Bu dosya, Asterisk'te log (günlük) ayarlarını yapılandırmak için kullanılır. logger.conf dosyası, kullanıcıların log seviyelerini ayarlamak, log dosyalarının konumunu belirlemek, log rotasyonunu yapılandırmak ve log kayıtlarını daha ayrıntılı veya daha az ayrıntılı hale getirmek için kullanılır.

-   iax.conf: Bu dosya, Inter-Asterisk eXchange (IAX) protokolü üzerinden Asterisk sunucuları arasındaki trafiği yapılandırmak için kullanılır. iax.conf dosyası, kullanıcıların IAX trafiğini yönlendirmek, IAX kimlik doğrulama ayarlarını yapılandırmak, IAX codec'leri ayarlamak ve diğer IAX özelliklerini yapılandırmak için kullanılır.