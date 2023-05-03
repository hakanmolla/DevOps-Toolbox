## Asterisk 20 Setup Adımları 



   ``` sudo apt update ```

	   ``` sudo apt upgrade -y ```

	    ``` cd /usr/src/ ```

	    ``` sudo wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-20-current.tar.gz ```

	   ``` sudo tar xvf asterisk-20-current.tar.gz ```

	    ``` cd asterisk-20* ```

	   ``` sudo git clone  https://github.com/felipem1210/asterisk-res_json.git ```

	    ``` sudo ./asterisk-res_json/install.sh ```

	   ``` sudo contrib/scripts/install_prereq  install ```
 
	  ``` sudo contrib/scripts/get_mp3_source.sh ```
 
	  ``` sudo contrib/scripts/get_swagger_ui.sh ```

	  ``` sudo ./configure ```

	  ``` sudo make menuselect ```

   ``` sudo make ```

  ``` sudo make install ```

	   ``` sudo make samples ```
 
  ``` sudo make config ```

  ``` sudo service asterisk status ```

  ``` sudo service asterisk start ```
	  ``` sudo service asterisk status ```

	  ``` sudo asterisk -rvvvvv ```
