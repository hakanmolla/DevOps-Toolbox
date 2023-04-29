## Sip Nedir ?


SIP, bir iletişim oturumunun başlatılması, sürdürülmesi ve sonlandırılması için kullandığı mesaj tabanlı bir protokoldür. Bu mesajlar, kullanıcının isteği doğrultusunda, belirli bir cihaza yönlendirilir ve bu cihazdan diğer cihazlara gönderilir.

SIP paketleri, bu mesajların taşınması için kullanılır. Bu paketler, UDP (User Datagram Protocol) veya TCP (Transmission Control Protocol) protokollerinden biri üzerinden gönderilir. SIP paketleri, bir başlık ve bir gövde içerir. Başlık, SIP paketinin türü, hedef ve kaynak adresleri, zaman damgası ve diğer bilgileri içerir. Gövde ise, mesajın içeriğini taşır.

SIP paketleri, bir iletişim oturumunun farklı aşamalarında gönderilir ve alınır. Örneğin, bir kullanıcı bir telefon görüşmesi başlatmak istediğinde, bir "INVITE" (Davet) mesajı gönderir. Bu mesaj, hedef cihaza bir çağrı yapma isteği iletilir. Hedef cihaz, bu çağrı isteğini kabul ederse, bir "200 OK" mesajı ile yanıt verir ve iletişim oturumu başlar.

SIP paketleri, iletişim oturumlarının yönetiminde ve işlevselliğinde önemli bir rol oynar. Örneğin, "ACK" (Onaylama) mesajları, bir mesajın başarıyla alındığını onaylamak için kullanılır. "BYE" (Veda) mesajları, bir iletişim oturumunun sonlandırılması için kullanılır.

SIP paketleri, ayrıca güvenliği ve kimlik doğrulamayı da sağlayabilir. Örneğin, SIP paketleri, Transport Layer Security (TLS) protokolü ile şifrelenebilir. Ayrıca, SIP paketleri, kimlik doğrulama protokolleri (örneğin, Digest Authentication) ile kimlik doğrulama işlemleri gerçekleştirebilir.