## Asterisk 20 Setup Adımları 


-	   1  ``` sudo apt update ```
-	   2  ``` sudo apt upgrade -y ```
-	   3  ``` cd /usr/src/ ```
-	   4  ``` sudo wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-20-current.tar.gz ```
-	   5  ``` sudo tar xvf asterisk-20-current.tar.gz ```
-	   6  ``` cd asterisk-20* ```
-	   7  ``` sudo git clone  https://github.com/felipem1210/asterisk-res_json.git ```
-	   8  ``` sudo ./asterisk-res_json/install.sh ```
-	   9  ``` sudo contrib/scripts/install_prereq  install ```
-	  10  ``` sudo contrib/scripts/get_mp3_source.sh ```
-	  11  ``` sudo contrib/scripts/get_swagger_ui.sh ```
-	  12  ``` sudo ./configure ```
-	  13  ``` sudo make menuselect ```
-	  14  ``` sudo make ```
-	  15  ``` sudo make install ```
-	  16  ``` sudo make samples ```
-	  17  ``` sudo make config ```
-	  18  ``` sudo service asterisk status ```
-	  19  ``` sudo service asterisk start ```
-	  20  ``` sudo service asterisk status ```
-	  21  ``` sudo asterisk -rvvvvv ```