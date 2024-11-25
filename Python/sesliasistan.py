from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import random
import os
from datetime import datetime
import aifc
import re

r = sr.Recognizer()


class SesliAsistan():
    global out_program

    def seslendirme(self, metin):
        xtts = gTTS(text=metin, lang='tr')
        dosya = 'dosya'+str(random.randint(0, 12345678954))+".mp3"
        xtts.save(dosya)
        playsound(dosya)
        os.remove(dosya)

    def ses_kayit(self):
        with sr.Microphone() as kaynak:
            print("Sizi dinliyorum")
            listen = r.listen(kaynak)
            voice = ""

            try:
                voice = r.recognize_google(listen, language="tr-TR")
            except sr.UnknownValueError:
                self.seslendirme(
                    'Ne söylediğinizi anlayamadım. Lütfen tekrar ediniz.')

            return voice

    def ses_karsilik(self, gelen_ses):
        if "selam" in gelen_ses:
            self.seslendirme("aleykum selam hacı abi")
        elif "merhaba" in gelen_ses:
            self.seslendirme("merhab dostum ne örüyorsun")
        elif "nasılsın" in gelen_ses:
            self.seslendirme("Ben iyim haci abi sen nasılsın")
        elif "kapat" in gelen_ses:
            self.seslendirme("Programdan cıkılıyor")
            return True
        elif "saat kaç" in gelen_ses:  # Örnek bir kontrol
            su_an = datetime.now()  # Şu anki zamanı al
            self.seslendirme(f"Saat şu an {su_an.hour}:{su_an.minute}")
            print(f"Saat şu an: {su_an.hour}:{su_an.minute}")
        elif "hangi gündeyiz" in gelen_ses:
            gunler = ["Pazartesi", "Salı", "Çarşamba",
                      "Perşembe", "Cuma", "Cumartesi", "Pazar"]
            gun = datetime.now().weekday()
            self.seslendirme(f"bugun {gunler[gun]}")
            
            
        elif "topla" in gelen_ses or "çıkar" in gelen_ses or "çarp" in gelen_ses or "böl" in gelen_ses:
            sayi_listesi = re.findall(r'\d+', gelen_ses)
            print("Bulunan sayılar:", sayi_listesi)
            sayi_listesi = list(map(int, sayi_listesi))
            print("Sayılar (integer formatında):", sayi_listesi)
            
            if '+' in gelen_ses or "topla" in gelen_ses :
                operator = '+'
                print(operator)
            elif '-' in gelen_ses or "çıkar" in gelen_ses:
                operator = '-'
            elif '*' in gelen_ses or 'x' in gelen_ses or "çarp" in gelen_ses:  # Çarpma için alternatif semboller
                 operator = '*'
            elif '/' in gelen_ses or "böl" in gelen_ses:
                operator = '/'
            else:
                return "Geçerli bir operatör bulunamadı."
            if len(sayi_listesi) < 2:
                self.seslendirme(f"Yeterli Sayı bulunanamdı")
                
            sonuc = 0
            
            for sayi in sayi_listesi:
                if operator == '+':
                    sonuc += sayi
                elif operator == '-':
                    sonuc -= sayi
                elif operator == '*':
                    sonuc *= sayi
                elif operator == '/':
                    if sayi == 0:
                     continue
            self.seslendirme(f"bulunan sayı {sonuc}")
                    
                
        elif "menü" in gelen_ses:
            print(''' 
                  Hoş Geldiniz Yapmak istediğiniz işlemi lütfen secinir. 
                  1- login 
                  2- 
                  
                  ''') 
            secim= self.ses_kayit()
            if "login" in secim :
                print("oturum acıldı tebrik ederiz.")
            
            
            
            
            

        elif "bekle" in gelen_ses:  # Örnek bir kontrol
            input("devam etmek için Enter tuşuna basınız")

        return False


asistan = SesliAsistan()

out_program = False

while not out_program:
    ses = asistan.ses_kayit()

    if (ses != " "):
        ses = ses.lower()
        print(ses)
        out_program = asistan.ses_karsilik(ses)
