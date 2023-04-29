## Asterisk 20 Setup Adımları 


-	   1  ```sh sudo apt update ```
-	   2  ```sh sudo apt upgrade -y ```
-	   3  ```sh cd /usr/src/ ```
-	   4  ```sh sudo wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-20-current.tar.gz ```
-	   5  ```sh sudo tar xvf asterisk-20-current.tar.gz ```
-	   6  ```sh cd asterisk-20* ```
-	   7  ```sh sudo git clone  https://github.com/felipem1210/asterisk-res_json.git ```
-	   8  ```sh sudo ./asterisk-res_json/install.sh ```
-	   9  ```sh sudo contrib/scripts/install_prereq  install ```
-	  10  ```sh sudo contrib/scripts/get_mp3_source.sh ```
-	  11  ```sh sudo contrib/scripts/get_swagger_ui.sh ```
-	  12  ```sh sudo ./configure ```
-	  13  ```sh sudo make menuselect ```
-	  14  ```sh sudo make ```
-	  15  ```sh sudo make install ```
-	  16  ```sh sudo make samples ```
-	  17  ```sh sudo make config ```
-	  18  ```sh sudo service asterisk status ```
-	  19  ```sh sudo service asterisk start ```
-	  20  ```sh sudo service asterisk status ```
-	  21  ```sh sudo asterisk -rvvvvv ```