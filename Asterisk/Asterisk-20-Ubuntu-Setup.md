## Asterisk 20 Setup Adımları 



	```bash
		sudo apt update 
	```

	```bash 
	   sudo apt upgrade -y 
	```

	```bash 
		cd /usr/src/ 
	```

	```bash 
	  sudo wget https://downloads.asterisk.org/pub/telephony/asterisk/asterisk-20-current.tar.gz 
	```

	```bash 
	   sudo tar xvf asterisk-20-current.tar.gz 
	```

	```bash 
		cd asterisk-20* 
	```

	```bash 
	   sudo git clone  https://github.com/felipem1210/asterisk-res_json.git 
	```

	```bash 
	  sudo ./asterisk-res_json/install.sh 
	```

	```bash 
	  sudo contrib/scripts/install_prereq  install 
	```
 
	```bash 
	sudo contrib/scripts/get_mp3_source.sh 
	```
 
	 ```bash 
	 sudo contrib/scripts/get_swagger_ui.sh 
	 ```

	 ```bash 
	 sudo ./configure 
	 ```

	```bash 
	  sudo make menuselect 
	```

	```bash 
	sudo make 
	```

	```bash
	sudo make install 
	```

	```bash
	    sudo make samples 
	```
 
  	```bash
   	sudo make config 

   	```

  	```bash
   		sudo service asterisk status 
   	```

  	```bash
   		sudo service asterisk start 
   	```
	```bash 
		sudo service asterisk status 
	```

	```bash 
	sudo asterisk -rvvvvv 
	```



```bash
python get-pip.py
```

	```bash
python get-pip.py
```